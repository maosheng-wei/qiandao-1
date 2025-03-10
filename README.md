<p align="center">
   <a href="https://github.com/qiandao-today/qiandao">
   <img style="border-radius:50%" width="150" src="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/web/static/img/icon.png">
   </a>
</p>

<h1 align="center">QianDao for Python3</h1>

<div align="center">
签到 —— 一个<b>自动签到框架</b> base on an HAR editor

[![HomePage][HomePage-image]][HomePage-url] 
[![Github][Github-image]][Github-url] 
[![Gitee][Gitee-image]][Gitee-url] 
[![license][github-license-image]][github-license-url] 
[![Build Image][workflow-image]][workflow-url] 
[![last commit][last-commit-image]][last-commit-url] 
[![commit activity][commit-activity-image]][commit-activity-url] 
[![docker version][docker-version-image]][docker-version-url] 
[![docker pulls][docker-pulls-image]][docker-pulls-url] 
[![docker stars][docker-stars-image]][docker-stars-url] 
[![docker image size][docker-image-size-image]][docker-image-size-url] 
![repo size][repo-size-image] 
![python version][python-version-image] 


[HomePage-image]: https://img.shields.io/badge/HomePage-qiandao--today-brightgreen
[HomePage-url]: https://qiandao.a76yyyy.cn
[Github-image]: https://img.shields.io/static/v1?label=Github&message=qiandao-today&color=brightgreen
[Github-url]: https://github.com/qiandao-today/qiandao/
[Gitee-image]: https://img.shields.io/static/v1?label=Gitee&message=a76yyyy&color=brightgreen
[Gitee-url]: https://gitee.com/a76yyyy/qiandao/
[github-license-image]: https://img.shields.io/github/license/qiandao-today/qiandao
[github-license-url]: https://github.com/qiandao-today/qiandao/blob/main/LICENSE
[last-commit-image]: https://img.shields.io/github/last-commit/qiandao-today/qiandao
[last-commit-url]: https://github.com/qiandao-today/qiandao/
[commit-activity-image]: https://img.shields.io/github/commit-activity/m/qiandao-today/qiandao
[commit-activity-url]: https://github.com/qiandao-today/qiandao/
[docker-version-image]: https://img.shields.io/docker/v/a76yyyy/qiandao?style=flat
[docker-version-url]: https://hub.docker.com/r/a76yyyy/qiandao/tags?page=1&ordering=last_updated
[docker-pulls-image]: https://img.shields.io/docker/pulls/a76yyyy/qiandao?style=flat
[docker-pulls-url]: https://hub.docker.com/r/a76yyyy/qiandao
[docker-stars-image]: https://img.shields.io/docker/stars/a76yyyy/qiandao?style=flat
[docker-stars-url]: https://hub.docker.com/r/a76yyyy/qiandao
[docker-image-size-image]: https://img.shields.io/docker/image-size/a76yyyy/qiandao?style=flat
[docker-image-size-url]: https://hub.docker.com/r/a76yyyy/qiandao
[repo-size-image]: https://img.shields.io/github/repo-size/qiandao-today/qiandao
[python-version-image]: https://img.shields.io/github/pipenv/locked/python-version/qiandao-today/qiandao
[workflow-image]: https://github.com/qiandao-today/qiandao/actions/workflows/Build%20Image.yml/badge.svg
[workflow-url]: https://github.com/qiandao-today/qiandao/actions/workflows/Build%20Image.yml

</div>

<p align="center">
   <img width="45%" style="border:solid 1px #DCEBFB" src="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/web/static/img/login.png" >
   <img width="45%" style="border:solid 1px #DCEBFB" src="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/web/static/img/index.png">
</p>

操作说明
==========
<a href="https://github.com/qiandao-today/qiandao/blob/master/docs/har-howto.md">HAR editor 使用指南</a>

**操作前请一定要记得备份数据库**

**请勿同时运行新旧版签到框架, 或将不同运行中容器的数据库映射为同一文件, 更新后请重启容器或清空浏览器缓存**

使用Docker部署站点
==========

1. docker地址 : [https://hub.docker.com/r/a76yyyy/qiandao](https://hub.docker.com/r/a76yyyy/qiandao)

2. docker部署命令

   ``` docker run -d --name qiandao -p 8923:80 -v $(pwd)/qiandao/config:/usr/src/app/config   a76yyyy/qiandao ```

- 默认Redis已随容器启动: (该命令与上一条命令等效)

   ``` docker run -d --name qiandao -p 8923:80 -v $(pwd)/qiandao/config:/usr/src/app/config   a76yyyy/qiandao sh -c "redis-server --daemonize yes && python /usr/src/app/run.py" ```

3. 数据库备份指令 : ```docker cp 容器名:/usr/src/app/config/database.db . ```
 
- 数据库恢复指令 : ```docker cp database.db 容器名:/usr/src/app/config/ ```

4. docker配置邮箱(强制使用SSL)

   ```docker run -d --name qiandao -p 8923:80 -v $(pwd)/qiandao/config:/usr/src/app/config --env MAIL_SMTP=STMP服务器 --env MAIL_PORT=邮箱服务器端口 --env MAIL_USER=用户名 --env MAIL_PASSWORD=密码  --env DOMAIN=域名 a76yyyy/qiandao ```

5. docker 使用MySQL

   ```docker run -d --name qiandao -p 8923:80 -v $(pwd)/qiandao/config:/usr/src/app/config --ENV DB_TYPE=mysql --ENV JAWSDB_MARIA_URL=mysql://用户名:密码@hostname:port/数据库名 a76yyyy/qiandao ```

6. 其余可参考 Wiki : <a href="https://github.com/qiandao-today/qiandao/blob/master/docs/Docker-howto.md">Docker部署签到站教程</a>

7. DockerHub : [介绍](http://mirrors.ustc.edu.cn/help/dockerhub.html)

8. **Docker已预装Curl环境, 默认安装pycurl模组**

```bash
# 如需使用Proxy功能请安装PyCurl
# Windows源码运行, 请执行 pip install pycurl==7.43.0.5 
pip install pycurl # pip3 install pycurl
# 如因curl导致500或599错误, 请卸载PyCurl或修改环境变量USE_PYCURL为False
# pip uninstall pycurl
```

Web源码部署
===========

## 1. Version: python3.8

```bash
# 请先cd到框架源码根目录
pip3 install -r requirements.txt
```

## 2. 可选 redis, Mysql

```
mysql < qiandao.sql
```

## 3. 修改相关设置

```bash
# 请先在框架根目录下新建local_config.py, 在linux环境下可执行以下命令
cp config.py local_config.py
# 修改local_config.py文件的内容不受通过git更新源码的影响
```

## 4. 启动

```bash
python ./run.py
```

数据不随项目分发, 去 [https://github.com/qiandao-today/templates](https://github.com/qiandao-today/templates) 查看你需要的模板, 点击下载。
在你自己的主页中 「我的模板+」 点击 + 上传。模板需要发布才会在「公开模板」中展示, 你需要管理员权限在「我的发布请求」中审批通过。


## 5. 设置管理员

```
python ./chrole.py your@email.address admin
```

## 6. qiandao.py-CMD操作

```
python ./qiandao.py tpl.har [--key=value]* [env.json]
```

config.py-配置变量
===========

变量名|是否必须|默认值|说明
:-: | :-: | :-: | :-: 
BIND|否|0.0.0.0|监听地址
PORT|否|8923|监听端口
QIANDAO_DEBUG|否|False|是否启用Debug模式
MULTI_PROCESS|否|False|是否启用多进程模式, <br>Windows平台无效
AUTO_RELOAD|否|False|是否启用自动热加载, <br>MULTI_PROCESS=True时无效
COOKIE_DAY|否|5|Cookie在客户端保留天数
DB_TYPE|否|sqlite3|需要使用MySQL时设置为'mysql'
JAWSDB_MARIA_URL|否|''|需要使用MySQL时, <br>设置为 mysql://用户名:密码@hostname:port/数据库名
REDISCLOUD_URL|否|''|需要使用Redis或RedisCloud时, <br>设置为 http://rediscloud:密码@hostname:port
REDIS_DB_INDEX|否|1|默认为1
PUSH_PIC_URL|否|<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/web/static/img/push_pic.png">push_pic.png</a>|默认为<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/web/static/img/push_pic.png">push_pic.png</a>
ENABLE_HTTPS|否|False|发送的邮件链接启用HTTPS, <br>非程序使用HTTPS, 需要HTTPS需要使用反向代理
DOMAIN|否|qiandao.today|指定访问域名, <br>建议修改, 否则邮件重置密码等功能无效
MAIL_SMTP|否|""|邮箱SMTP服务器
MAIL_PORT|否|""|邮箱SMTP服务器端口
MAIL_USER|否|""|邮箱用户名
MAIL_PASSWORD|否|""|邮箱密码
MAIL_DOMAIN|否|mail.qiandao.today|邮箱域名,没啥用, 使用的DOMAIN
AES_KEY|否|binux|AES加密密钥, **强烈建议修改**
COOKIE_SECRET|否|binux|cookie加密密钥, **强烈建议修改**
PROXIES|否|""|全局代理域名列表,用"|"分隔
PROXY_DIRECT_MODE|否|""|全局代理黑名单模式,默认不启用 <br>"url"为网址匹配模式;"regexp"为正则表达式匹配模式
PROXY_DIRECT|否|""|全局代理黑名单匹配规则
USE_PYCURL|否|True|是否启用Pycurl模组
ALLOW_RETRY|否|True|在Pycurl环境下部分请求可能导致Request错误时, <br>自动修改冲突设置并重发请求
CURL_ENCODING|否|True|是否允许使用Curl进行Encoding操作
CURL_CONTENT_LENGTH|否|True|是否允许Curl使用Headers中自定义Content-Length请求
NOT_RETRY_CODE|否|<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/config.py">详见配置</a>...|<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/config.py">详见配置</a>...
EMPTY_RETRY|否|True|<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/config.py">详见配置</a>...

> 详细信息请查阅<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/config.py">config.py</a>

## 旧版local_config.py迁移
|  Line  |  Delete  |  Modify  |
|  ----  | ----  | ----  |
|10|~~```import urlparse```~~|```from urllib.parse import urlparse```|
|18|~~```mysql_url = urlparse.urlparse(os.getenv('JAWSDB_MARIA_URL', ''))```~~|```mysql_url = urlparse(os.getenv('JAWSDB_MARIA_URL', ''))```|
|19|~~```redis_url = urlparse.urlparse(os.getenv('REDISCLOUD_URL', ''))```~~|```redis_url = urlparse(os.getenv('REDISCLOUD_URL', ''))```|
|43|~~```aes_key = hashlib.sha256(os.getenv('AES_KEY', 'binux').encode('utf-8')).digest()```~~|```aes_key = hashlib.sha256(os.getenv('AES_KEY', 'binux')).digest()```|
|44|~~```cookie_secret = hashlib.sha256(os.getenv('COOKIE_SECRET', 'binux').encode('utf-8')).digest()```~~|```cookie_secret = hashlib.sha256(os.getenv('COOKIE_SECRET', 'binux')).digest()```|

更新方法
===========
## 1. 源码部署更新
``` 
sh ./update.sh # 先cd到源码所在目录, 执行命令后重启进程 
```

## 2. Docker容器部署更新
``` 
sh /usr/src/app/update.sh # 先进入容器后台, 执行命令后重启进程 
```


更新日志
===========
## 2021.10.16 更新
1. 添加Tg Bot 和 DingDing Bot推送
2. 修复并优化日志推送功能
3. 日志推送允许'\r\n'换行
4. 修复验证邮箱bug
5. 允许开启热加载功能
6. 允许开启多进程功能(性能及存在问题未知)
7. 优化前端文件结构
8. 修复更新公共模板导致订阅空白的bug
9. 点击关于页面不再301重定向
10. 修复编辑模板页面显示序号问题

<details>

<summary>
历史更新日志
</summary>

## 2021.10.10 更新
1. 修复数据库aip字段类型
2. 修复并优化公共模板添加、更新的性能
3. 关于页面优化并添加RSA加解密介绍
4. 修复不满足成功条件断言时显示OK的bug
5. 允许设置任务重试次数及重试间隔时间
6. Select控件支持搜索
7. 基于CoffeeScript重新编译js脚本
8. 优化框架文件结构

## 2021.09.28 更新
1. 更新并优化fetcher脚本
2. 更新输入提示(by [cxk000](https://github.com/qiandao-today/qiandao/commits?author=ckx000))
3. 修复{{unicode(arg)}}不能正常转换unicode的bug
4. 修复重复添加'|urlencode'的bug
5. 优化fetcher重试逻辑

## 2021.09.17 更新
1. 修复变量名冲突时自动添加'_'失效的bug
2. 支持socks5h代理
3. 添加har时可见postdata的text控件
4. 修复Proxies的bug

> **Tips: Socks5说明**
> 
> Socks5h代理: socks5代理通过服务端进行域名解析. 
> 
> 如通过代理请求返回500或599错误时, 可尝试将 `socks5://host:port` 改为 `socks5h://host:port`, 以使用Socks5h方式请求

## 2021.09.16 更新
1. 代理允许添加账户密码
2. 修复unicode转换时不间断空格输出乱码的bug
3. 修复修改任务分组时分组名为中文导致的乱码bug
4. 支持socks5代理
5. 分别构建Pycurl与Qiandao容器
6. 优化登录页面,"我的"首页和"多任务操作"页面(by [acooler15](https://github.com/acooler15/qiandao))

## 2021.09.10 更新
1. 添加全局代理黑名单机制
2. 完善时间戳API
3. 修复重置密码功能
4. 修复前端正则表达式全局匹配和匹配为空时的bug
5. 允许正则表达式匹配修饰符'/s'和'/u'
6. 添加参数时在末尾添加(by [billypon](https://github.com/billypon/qiandao/commit/243220407809863ddf7805be193954021eea65ce))
7. 修复header['name']为空时报错的bug(20210912)

> **Tips: 全局代理黑名单机制说明**
```python
# 以下为全局代理域名列表相关设置
# proxies为全局代理域名列表, 默认为空[], 表示不启用全局代理; 
# 代理格式应为'scheme://username:password@host:port',例如:proxies = ['http://admin:admin@127.0.0.1:8923','https://proxy.com:8888']; 
# 任务级代理请在新建或修改任务时添加,任务级代理优先级大于全局代理; 
proxies = os.getenv('PROXIES', '').split('|')               # 若希望部分地址不走代理, 请修改proxy_direct_mode及proxy_direct 
proxy_direct_mode = os.getenv('PROXY_DIRECT_MODE', '')      # 默认为空, 可选输入:'url'为网址匹配模式;'regexp'为正则表达式匹配模式;''空则不启用全局代理黑名单 
# proxy_direct_mode = os.getenv('PROXY_DIRECT_MODE', 'url')进入网址完全匹配模式, 在proxy_direct名单的url均不通过代理请求, 以'|'分隔url网址, url格式应为scheme://domain或scheme://domain:port 
# 例如: proxy_direct = os.getenv('PROXY_DIRECT', 'http://127.0.0.1:80|https://localhost'); 
# proxy_direct_mode= os.getenv('PROXY_DIRECT_MODE', 'regexp')进入正则表达式匹配模式, 满足正则表达式的网址均不通过代理请求; 
# 启用regexp模式后自动采用以下默认匹配正则表达式, 如无特别需求请勿修改
proxy_direct = os.getenv('PROXY_DIRECT', r"""(?xi)\A
                ([a-z][a-z0-9+\-.]*://)?                                                        # Scheme
                (0(.0){3}|127(.0){2}.1|localhost|\[::([\d]+)?\])                                # Domain/Hostname/IPv4/IPv6
                (:[0-9]+)? """                                                                  # :Port
                ) 
```

## 2021.09.08 更新
1. 修复提取变量处输入正则表达式频繁卡顿的bug
2. 修复提取变量处正则表达式错误导致500的bug
3. 输入变量名与API变量冲突时自动添加 '_'
4. 修复导入har自动提取API函数名作为变量导致500报错的bug
5. 前端更新

> **Tips: 20210906 -> 20210908版本更新了Python相关特性和前端脚本, 不再与旧版python兼容, 请升级至Python 3.6及以上**

## 2021.09.07 更新
1. 修复单独调用worker脚本时的异常bug
2. 允许设置新建任务后准备延时时间
3. 更新代码以适配python3的async/await特性
4. 更新API和关于页面

## 2021.09.06 更新
1. 签到日志支持使用 '\r\n' 进行换行
2. 面板备份还原数据失败添加提示
3. 修复我的模板分组按钮不显示已有分组的bug
4. 修复新建任务时分组名为中文导致的乱码bug

## 2021.09.05 更新
1. 优化任务前值显示方案
2. 修复IPv6访问时的bug
3. 管理用户界面添加用户最后登录IP显示
4. 我的页面添加分组任务“全选/反选”复选框

## 2021.09.03 更新
1. 修复更新新版框架后因旧版框架cookie缓存导致的500错误
2. 修复util编解码问题
3. 添加368和armv6架构容器构建
4. 优化插入请求功能
5. 修复pycurl导致若干500和599错误
6. 更新需求模块



## 2021.09.02 更新
1. 修复Image解码失败的bug
2. 添加请求时限设置
3. 修复延时API超过请求时限导致的bug
4. 查看任务的模板数据时自动导入任务变量(by [billypon](https://github.com/billypon/qiandao))
5. 默认去除pycurl模组, 解决部分500和599错误

## 2021.08.07 更新
1. 更新Wiki
2. 修复网页编码导致的Body解析bug

## 2021.07.31 更新
1. 修复旧版数据库导致的编码bug
2. 添加部分说明
3. 优化docker配置
4. 允许headers中文编码
5. 修复不间断空格导致的编解码bug
6. 修复delay延时功能
7. 增加log的详细错误显示

## 2021.07.29 更新
1. 修复异常抛出时泄露源码路径的bug
2. 修复原sql的groups字段bug
3. 优化DockerFile及配置文件

## 2021.07.28 更新
1. 适配python版本至python3.8

## 2021.06.28 更新
1. 修改Dockfile,采用密钥更新

## 2021.06.26 更新
1. 公共仓库添加评论功能, 跳转到github, 国内打不开的问题自行解决
2. 公共仓库添加强制更新按钮
3. 修复mysql创建数据库错误
4. 修复about页面打开500错误

## 2021.06.21 更新
1. 重写公共模板仓库的订阅方法, 允许添加第三方库(具体规范参考)
2. 模板使用缓存的方式, 默认是每隔一天重新读取, 可以手动刷新缓存
3. 新增多任务禁用/启用/删除/定时/分组
4. 任务和模板分组栏修改颜色
5. 修复注册用户时没有创建md5密码的bug

## 2021.04.13 更新
1. 添加proxy功能, 目前暂时不可用(By billypon)

## 2021.02.20 更新
1. 完善MD5
2. 修复部分站点500的问题
3. 公共模板添加清缓存功能

## 2021.02.20 更新
1. 修复容忍错误推送的失效的BUG
2. 主循环修改为0.5s, 使定时运行更准确
3. 修复/register没有注册按钮的BUG
4. 密码验证修改为md5
5. 更换默认微信推送图片

## 2021.01.22 更新
1. 整合推送模块
2. 添加定时cron支持
3. ENABLE_HTTPS 使能时邮件链接为https

## 2021.01.17 更新
1. 添加企业微信支持
2. 支持在用户管理里修改密码

## 2021.01.16 更新
1. 修复点击登陆失败后注册按钮消失的问题

## 2021.01.13 更新
1. 启用邮箱验证前必须验证管理员邮箱

## 2021.01.08 更新
1. 修复20210122注册按钮丢失的BUG
2. 添加记事本访问接口
3. 添加自定义推送示例
4. sqlite3_db_task_converter放在web启动之前

## 2021.01.07 更新
1. 底部添加本项目链接
2. 禁止注册时隐藏注册按钮
3. 显示注册推送的前值
4. 添加记事本功能, 用户可以将数据保存在本地
5. 推送注册和推送设置按钮移动到工具箱
6. 定时时间以任务起始时间为依据
7. 新增自定义推送功能
8. bark推送改为POST, 可以推送日志

## 2020.12.24 更新
1. 修复模板编辑中'{{变量}}'自动urlencode的问题

## 2020.12.23 更新
1. 添加EMAIL发送开关

## 2020.12.22 更新
1. 修复任务运行结束后'logDay'报错
2. 邮箱变量设置为环境变量获取

## 2020.12.04 更新
1. 修复任务运行结束后'logDay'报错

## 2020.11.20 更新
1. 修复模板订阅时url太长报错的问题, 模板按照修改时间来排序
2. 支持网站设置仅保留一定天数的日志, 日志清理时间在任务成功完成之后,默认365天
3. 手动清除一定天数的日志
4. 分组折叠/展开 支持记忆
5. 修复模板编辑页面反选错误的bug

## 2020.11.05 更新
1. 用户管理, 备份, 网站管理, 密码不显示明文, 不输入账号密码返回页面显示中文

## 2020.10.31 更新
1. 允许普通用户备份/恢复
2. 模板编辑页显示请求排序
3. 模板编辑页可以同时删除多个请求
4. 主页允许多项操作删除/分组, 取消分组的勾选框, 改为点击即可显示隐藏
5. 公共仓库打开失败时使用本地仓库

## 2020.09.18 更新
1. 允许备份/恢复 用户的所有任务和模板
2. 修复模板编辑时, 变量作为url会自动url转码的bug
3. 模板编辑时允许拖拽请求
4. 模板订阅添加错误显示, 避免500

## 2020.09.14 更新(By liubei121212)
1. 添加 unicode 函数
2. 优化 api 页样式
3. 在模板编辑页中测试时也可以复制错误信息了
4. 优化日志页复制错误信息的实现方式
5. 添加常用 api/过滤器
6. 修复主页和推送设置中长用户名的显示
7. 前值、edit 页面的错误信息增加复制按钮


## 2020.09.10 更新
1. 鉴于github 污染严重, 使用gitee代替作为订阅源, 地址 : [https://gitee.com/qiandao-today/templates](https://gitee.com/qiandao-today/templates)
2. 首页的检查模板更新取消, 打开公共模板仓库会自动检查更新
3. 修复邮箱验证, 注册后未验证可以再次点击注册验证
4. 修改任务时显示前值

本次更新有js脚本更新, 请开启chrome 的 “disable cache”功能更新js脚本

## 2020.09.07 更新
1. 在数据库管理中增加一键备份/恢复所有模板的功能

## 2020.09.01 更新
1. 正则提取支持post方式
2. 取消getcookie插件提示(By powersee)
3. 管理员可以查看用户是否验证邮箱, 可以设置不验证邮箱无法登陆
4. 支持任务分组
5. 推送带上任务备注

## 2020.07.19更新
1. 修改按钮“推送通知开关”为“推送设置”
2. 添加错误提醒容忍。在自动签到到一定次数错误后, 才推送提醒。

## 2020.07.17更新
1. 使报错显示中文, 添加点击复制错误日志按钮(by [liubei121212](https://github.com/liubei121212/qiandao))
2. 主页版本从alpha修改为20200717

## 2020.07.09更新
1. 添加 管理员 备份数据库功能
2. 添加任务日志清空功能
3. 修复定时的随机延时取消失败的BUG
4. 添加任务禁用功能
5. 为了提高兼容性, 请求不验证SSL

## 2020.6.22 更新
1. 修复检查公共模板更新功能；
2. 美化左侧三按钮(By 十六君)
3. 修复插入RSA加密实际是字符串替换的BUG
4. 修改请求为不验证SSL, 提升兼容性
   
## 2020.6.14 更新
1. 添加RSA加密/解密
2. 用户管理页面添加用户最后登陆时间
3. 字符串替换功能可以返回纯文本, 避免有转义'\\'的出现,需要替换参数r=text

## 2020.6.12 更新
1. 定时日志BUG太多, 修不过来, 取消此功能
2. 修复用户不存在时登录500错误

## 2020.6.11 更新
1. 修复MySQL的支持, 不需要手动更新Mysql数据库

## 2020.6.10 更新
1. 添加管理员管理用户功能, 可以将用户禁用/启用/删除
2. 添加关闭/开启注册功能
3. 修改主页的'检查更新'为'检查模板更新'

使用前需要进入容器, 将对应已注册邮箱设置为管理员 : 
```
docker exec -it 容器名 /bin/bash
python ./chrole.py 邮箱 admin
```
被禁用的账户将不能登录网站,所有任务将被禁用。
被删除的账户, 会删除该用户的所有任务, 模板和日志

如果使用mysql 在 20200604 请使用以下命令 : 
```
ALTER TABLE `user` ADD `status`  VARBINARY(1024) NOT NULL DEFAULT 'Enable';
CREATE TABLE IF NOT EXISTS `site` (
          `id` INTEGER NOT NULL PRIMARY KEY,
          `regEn` INT UNSIGNED NOT NULL DEFAULT 1
        );
INSERT INTO `site` VALUES(1,1);
```

## 2020.6.6 更新
1. 修复用户不存在依然能登陆的BUG(具体表现为 : 新用户新建模板保存时500错误, 注册推送时提示NoneType) 
2. 完善注册推送的注册消息
3. 修复自动完成不推送的bug
4. 添加定时 “今日已签过” 选项, 可以直接定时第二天
5. 修复公共模板的HAR订阅功能

## 2020.6.5 更新
1. 修复 sqlite3 数据库初始值错误的问题, 仅影响新建数据库的用户 

## 2020.6.4 更新
1. 根据反馈, HAR编辑里插入链接修改默认地址为localhost
2. 修复2020601版, 插入请求后修改为localhost地址, 点击测试的500错误的问题
3. 支持定时后 随机延时

__本次更新会把之前的定时设置全部取消, 介意请勿更新__

如果使用mysql 在 20200601 请使用以下命令 : 
```
ALTER TABLE  `task` ADD `newontime`  VARBINARY(256) NOT NULL DEFAULT '{\"sw\":false,\"time\":\"00:10:10\",\"randsw\":false,\"tz1\":0,\"tz2\":0 }'
```
延时的另一种用法, 间隔定时运行 : 如果要实现每1周定时运行一次, 设置最大最小值都是604800, 即可

## 2020.6.1 更新
1. 时间显示修改为具体时间, 取消之前的 "1小时后"等模糊显示(By 戏如人生)
2. 新建任务时可以选择分组
3. Bark推送支持保存历史信息, 需要升级APP。
4. HAR编辑里添加添加插入unicode解码, url解码, 正则表达式, 字符串替换的功能

## 2020.5.31 更新
1. 修复定时 ‘day out of month’ 的BUG
2. 取消定时界面的今日运行选项, 自动判断当前时间是今天还是第二天
3. 集成了时间戳获取、unicode转换、url转换功能(By [gxitm](https://github.com/gxitm))
4. 集成了正则表达式、字符串替换功能。

## 2020.5.30 更新
1. 修改 任务失败时 推送的消息内容为 任务日志；
2. 因浏览器支持不好, 取消 2020.5.18更新的 ‘模板上传指定格式为.har’；
3. 新增模板编辑 追加HAR 的功能；
4. 新增模板请求删除功能。

## 2020.5.26 更新
1. 修复定时日志发送的最后一条日志的bug
2. 修复定时日志出错影响程序运行的bug

## 2020.5.25 更新
1. Bark, S酱, WXPusher 注册合并为一个按钮
2. 任务推送支持注册后也能关闭
3. 支持分任务开/关推送
4. 新增每日日志功能, 可以将每日定时前的最后一个日志推送到S酱和WXPusher
5. 修复“↓”按钮定位不准的bug

如果使用mysql 在 5.22 请使用以下命令 : 
```
ALTER TABLE `task` ADD `pushsw` VARBINARY(128) NOT NULL DEFAULT '{\"logen\":false,\"pushen\":true}';
ALTER TABLE `user` ADD `logtime` VARBINARY(128) NOT NULL DEFAULT '{\"en\":false,\"time\":\"20:00:00\",\"ts\":0,\"schanEn\":false,\"WXPEn\":false}';
```

## 2020.5.22 更新
1. 分组增加折叠/展开功能
2. 左侧增加新建模板按钮, “↑”回到顶部,  “↓”表示跳转到模板页面
3. 修复删除任务时日志不删除bug

## 2020.5.19 更新
1. 添加手动检查模板更新的按钮。

如果使用mysql 在 5.18 请使用以下命令 : 
```
ALTER TABLE `tpl` ADD `tplurl` VARCHAR(1024) NULL DEFAULT '' ;
ALTER TABLE `tpl` ADD `updateable` INT UNSIGNED NOT NULL DEFAULT 0;
```

## 2020.5.18 更新
1. 定时的 "今日是否运行" 修改 为 "今日运行"
2. 添加模板订阅功能, 仓库地址在[https://github.com/qiandao-today/templates](https://github.com/qiandao-today/templates)

   主页打开公共模板按钮, 点击订阅后自动导入模板, 需要自己确认保存
3. 模板上传指定格式为.har

## 2020.5.16 更新
1. 添加任务分类功能

如果使用mysql 请使用以下命令 : 
```
ALTER TABLE `task` ADD `_groups` VARBINARY(128) NOT NULL DEFAULT 'None' ;
```
2. 定时功能显示之前的定时值

## 初始版本
基于quchaonet的蓝调主题签到增加了:


1. 设置任务最低间隔时间及任务request最高100限制 (by 戏如人生)

http://cordimax.f3322.net:5558/381.html

2. 增加了server酱、bark推送, WXPusher推送, 并可以设置推送开关（by AragonSnow）
需要推送的 : 登录账号以后点击注册bark/s酱/WXPusher, 测试推送没有问题以后,再点击提交


3. 增加定时功能, 在新建任务以后会出现定时按钮, 设置每天的定时时间。<br>
**不兼容旧版的数据库,  旧版数据库导入会自动转换, 旧版将无法使用**<br>
**使用SQLite3的, 默认路径改为config文件夹里面, 方便挂载后备份**<br>
**使用Mysq的,请使用一下命令更新数据库:**
```
ALTER TABLE `task` ADD `ontimeflg` INT UNSIGNED NOT NULL DEFAULT 0;
ALTER TABLE `task` ADD `ontime` VARCHAR(256) NOT NULL DEFAULT '00:10:00';
ALTER TABLE `user` ADD `skey` VARBINARY(128) NOT NULL DEFAULT '' ;
ALTER TABLE `user` ADD `barkurl` VARBINARY(128) NOT NULL DEFAULT '' ;
ALTER TABLE `user` ADD `wxpusher` VARBINARY(128) NOT NULL DEFAULT '' ;
ALTER TABLE `user` ADD `noticeflg` INT UNSIGNED NOT NULL DEFAULT 1;
```
</details>

鸣谢
===========

[Mark  https://www.quchao.net/](https://www.quchao.net/) 

[戏如人生 https://49594425.xyz/](https://49594425.xyz/)

[AragonSnow https://hexo.aragon.wang/](https://hexo.aragon.wang/)

[buzhibujuelb](https://github.com/buzhibujuelb) 

[billypon](https://github.com/billypon) 

[powersee](https://github.com/powersee) 

[AragonSnow/qiandao](https://github.com/aragonsnow/qiandao) 

[a76yyyy/qiandao](https://github.com/a76yyyy/qiandao) 

<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/version.json">……</a>

个人项目精力有限, 仅保证对Chrome浏览器的支持。如果测试了其他浏览器可以pull request。

许可
===========

<a href="https://cdn.jsdelivr.net/gh/qiandao-today/qiandao@master/LICENSE">MIT</a>