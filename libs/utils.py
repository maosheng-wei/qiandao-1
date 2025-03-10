﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-08-07 22:00:27

import socket
import struct
import ipaddress
from tornado import gen

def ip2int(addr):
    try:
        return struct.unpack("!I", socket.inet_aton(addr))[0]
    except:
        return int(ipaddress.ip_address(addr))

def ip2varbinary(addr:str, version:int):
    if version == 4:
        return socket.inet_aton(addr)
    if version == 6:
        return socket.inet_pton(socket.AF_INET6,addr)

def int2ip(addr):
    try:
        return socket.inet_ntoa(struct.pack("!I", addr))
    except:
        return str(ipaddress.ip_address(addr))

def varbinary2ip(addr:bytes or int or str):
    if isinstance(addr, int):
        return int2ip(addr)
    if isinstance(addr, str):
        addr = addr.encode('utf-8')
    if len(addr) == 4:
        return socket.inet_ntop(socket.AF_INET,addr)
    if len(addr) == 16:
        return socket.inet_ntop(socket.AF_INET6,addr)

def isIP(addr = None):
    if addr:
        p = re.compile(r'''
         ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) # IPv4
         |::ffff:(0:)?((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) # IPv4 mapped / translated addresses
         # |fe80:(:[0-9a-fA-F]{1,4}){0,4}(%\w+)? # IPv6 link-local
         |([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4} # IPv6 full
         |(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?::(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})? # IPv6 with ::
         ''', re.VERBOSE)
        tmp = p.match(addr)
        if tmp and tmp[0] == addr:
            if ':' in tmp[0]:
                return 6
            else:
                return 4
        else:
            return 0
    return 0

def urlmatch(url):
    reobj = re.compile(r"""(?xi)\A
                ([a-z][a-z0-9+\-.]*://)?                            # Scheme
                ([a-z0-9\-._~%]+                                    # domain or IPv4 host
                |\[[a-z0-9\-._~%!$&'()*+,;=:]+\])                   # IPv6+ host
                (:[0-9]+)? """                                      # :port
                )
    match = reobj.search(url)
    return match.group()

def getLocalScheme(scheme):
    if scheme in ['http','https']:
        if config.https:
            return 'https'
        else:
            return 'http'
    return scheme

import umsgpack
import functools

def func_cache(f):
    _cache = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        key = umsgpack.packb((args, kwargs))
        if key not in _cache:
            _cache[key] = f(*args, **kwargs)
        return _cache[key]

    return wrapper

def method_cache(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_cache'):
            self._cache = dict()
        key = umsgpack.packb((args, kwargs))
        if key not in self._cache:
            self._cache[key] = fn(self, *args, **kwargs)
        return self._cache[key]

    return wrapper

import datetime

#full_format=True，的时候是具体时间，full_format=False就是几秒钟几分钟几小时时间格式----此处为模糊时间格式模式
def format_date(date, gmt_offset=-8*60, relative=True, shorter=False, full_format=True):
    """Formats the given date (which should be GMT).

    By default, we return a relative time (e.g., "2 minutes ago"). You
    can return an absolute date string with ``relative=False``.

    You can force a full format date ("July 10, 1980") with
    ``full_format=True``.

    This method is primarily intended for dates in the past.
    For dates in the future, we fall back to full format.
    """
    if not date:
        return '-'
    if isinstance(date, float) or isinstance(date, int):
        date = datetime.datetime.utcfromtimestamp(date)
    now = datetime.datetime.utcnow()
    local_date = date - datetime.timedelta(minutes=gmt_offset)
    local_now = now - datetime.timedelta(minutes=gmt_offset)
    local_yesterday = local_now - datetime.timedelta(hours=24)
    local_tomorrow = local_now + datetime.timedelta(hours=24)
    if date > now:
        later = u"后"
        date, now = now, date
    else:
        later = u"前"
    difference = now - date
    seconds = difference.seconds
    days = difference.days

    format = None
    if not full_format:
        if relative and days == 0:
            if seconds < 50:
                return u"%(seconds)d 秒" % {"seconds": seconds} + later

            if seconds < 50 * 60:
                minutes = round(seconds / 60.0)
                return u"%(minutes)d 分钟" % {"minutes": minutes} + later

            hours = round(seconds / (60.0 * 60))
            return u"%(hours)d 小时" % {"hours": hours} + later

        if days == 0:
            format = "%(time)s"
        elif days == 1 and local_date.day == local_yesterday.day and \
                relative and later == u'前':
            format = u"昨天" if shorter else u"昨天 %(time)s"
        elif days == 1 and local_date.day == local_tomorrow.day and \
                relative and later == u'后':
            format = u"明天" if shorter else u"明天 %(time)s"
        #elif days < 5:
            #format = "%(weekday)s" if shorter else "%(weekday)s %(time)s"
        elif days < 334:  # 11mo, since confusing for same month last year
            format = "%(month_name)s-%(day)s" if shorter else \
                "%(month_name)s-%(day)s %(time)s"

    if format is None:
        format = "%(year)s-%(month_name)s-%(day)s" if shorter else \
            "%(year)s-%(month_name)s-%(day)s %(time)s"

    str_time = "%d:%02d:%02d" % (local_date.hour, local_date.minute, local_date.second)

    return format % {
        "month_name": local_date.month,
        "weekday": local_date.weekday(),
        "day": str(local_date.day),
        "year": str(local_date.year),
        "time": str_time
    }

def utf8(string):
    if isinstance(string, str):
        return string.encode('utf8')
    return string

def conver2unicode(string):
    if not isinstance(string,str):
        try:
            string = string.decode()
        except :
            string =  str(string)
    tmp = bytes(string,'unicode_escape').decode('utf-8').replace(r'\u',r'\\u').replace(r'\\\u',r'\\u')
    tmp = bytes(tmp,'utf-8').decode('unicode_escape')
    return tmp.encode('utf-8').replace(b'\xc2\xa0',b'\xa0').decode('unicode_escape')

import urllib
import config
from tornado import httpclient


async def send_mail(to, subject, text=None, html=None, shark=False, _from=u"签到提醒 <noreply@{}>".format(config.mail_domain)):
    if not config.mailgun_key:
        subtype = 'html' if html else 'plain'
        _send_mail(to, subject, html or text or '', subtype)
        return

    httpclient.AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
    if shark:
        client = httpclient.AsyncHTTPClient()
    else:
        client = httpclient.HTTPClient()

    body = {
        'from': utf8(_from),
        'to': utf8(to),
        'subject': utf8(subject),
    }

    if text:
        body['text'] = utf8(text)
    elif html:
        body['html'] = utf8(html)
    else:
        raise Exception('need text or html')

    req = httpclient.HTTPRequest(
        method="POST",
        url="https://api.mailgun.net/v2/%s/messages" % config.mail_domain,
        auth_username="api",
        auth_password=config.mailgun_key,
        body=urllib.parse.urlencode(body)
    )
    res = await gen.convert_yielded(client.fetch(req))
    return res


import smtplib
from email.mime.text import MIMEText
import logging

logger = logging.getLogger('qiandao.util')


def _send_mail(to, subject, text=None, subtype='html'):
    if not config.mail_smtp:
        logger.info('no smtp')
        return
    msg = MIMEText(text, _subtype=subtype, _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = config.mail_user
    msg['To'] = to
    try:
        logger.info('send mail to {}'.format(to))
        s = config.mail_ssl and smtplib.SMTP_SSL(config.mail_smtp) or smtplib.SMTP(config.mail_smtp)
        s.connect(config.mail_smtp)
        s.login(config.mail_user, config.mail_password)
        s.sendmail(config.mail_user, to, msg.as_string())
        s.close()
    except Exception as e:
        logger.error('send mail error {}'.format(str(e)))
    return


import chardet
from requests.utils import get_encoding_from_headers, get_encodings_from_content


def find_encoding(content, headers=None):
    # content is unicode
    if isinstance(content, str):
        return 'utf-8'
    
    encoding = None

    # Try charset from content-type
    if headers:
        encoding = get_encoding_from_headers(headers)
        if encoding == 'ISO-8859-1':
            encoding = None

    # Fallback to auto-detected encoding.
    if not encoding and chardet is not None:
        encoding = chardet.detect(content)['encoding']
    
    # Try charset from content
    if not encoding:
        try:
            encoding = get_encodings_from_content(content)
            encoding = encoding and encoding[0] or None
        except:
            if isinstance(content,bytes):
                return encoding or 'utf-8'

    if encoding and encoding.lower() == 'gb2312':
        encoding = 'gb18030'

    return encoding or 'latin_1'


def decode(content, headers=None):
    encoding = find_encoding(content, headers)
    if encoding == 'unicode':
        return content
    
    try:
        return content.decode(encoding, 'replace')
    except Exception as e:
        print('utils.decode:',e)
        return None


def quote_chinese(url, encodeing="utf-8"):
    if isinstance(url, str):
        return quote_chinese(url.encode("utf-8"))
    if isinstance(url,bytes):
        url = url.decode()
    res = [b if ord(b) < 128 else urllib.parse.quote(b) for b in url]
    return "".join(res)


import hashlib
md5string = lambda x: hashlib.md5(utf8(x)).hexdigest()


import random
def get_random(min_num, max_mun, unit):
    random_num = random.uniform(min_num, max_mun)
    result = "%.{0}f".format(int(unit)) % random_num
    return result


import datetime
def get_date_time(date=True, time=True, time_difference=0):
    if isinstance(date,str):
        date=int(date)
    if isinstance(time,str):
        time=int(time)
    if isinstance(time_difference,str):
        time_difference = int(time_difference)
    now_date = datetime.datetime.today() + datetime.timedelta(hours=time_difference)
    if date:
        if time:
            return str(now_date).split('.')[0]
        else:
            return str(now_date.date())
    elif time:
        return str(now_date.time()).split('.')[0]
    else:
        return ""

import time
def timestamp(type='int'):
    if type=='float':
        return time.time()
    else:
        return int(time.time())

def add(a:str,b:str):
    if is_num(a) and is_num(b):
        return '{:f}'.format(float(a)+float(b))
    return

def sub(a:str,b:str):
    if is_num(a) and is_num(b):
        return '{:f}'.format(float(a)-float(b))
    return

def multiply(a:str,b:str):
    if is_num(a) and is_num(b):
        return '{:f}'.format(float(a)*float(b))
    return

def divide(a:str,b:str):
    if is_num(a) and is_num(b):
        return '{:f}'.format(float(a)/float(b))
    return

def is_num(s:str=''):
    s = str(s)
    if s.count('.') ==1:
        tmp = s.split('.')
        return tmp[0].isdigit() and tmp[1].isdigit()
    else:
        return s.isdigit()

jinja_globals = {
    'md5': md5string,
    'quote_chinese': quote_chinese,
    'utf8': utf8,
    'unicode': conver2unicode,
    'timestamp': timestamp,
    'random': get_random,
    'date_time': get_date_time,
    'is_num':is_num,
    'add':add,
    'sub':sub,
    'multiply':multiply,
    'divide':divide,
}

import re
def parse_url(url):
    if not url:
        return None
    result = re.match('((?P<scheme>(https?|socks5h?)+)://)?((?P<username>[^:@/]+)(:(?P<password>[^@/]+))?@)?(?P<host>[^:@/]+):(?P<port>\d+)', url)
    return None if not result else {
        'scheme': result.group('scheme'),
        'host': result.group('host'),
        'port': int(result.group('port')),
        'username': result.group('username'),
        'password': result.group('password'),
    }
