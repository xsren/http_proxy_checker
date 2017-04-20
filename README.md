最近需要检查HTTP代理的可用性、匿名程度、地区等信息，但是网上没有可用的API，于是自己写了这个服务。

## 一、原理

使用 Nginx 作为 HTTP 服务器，可以将 Headers 转发到 API 层；

使用 Gunicorn 作为 WSGI HTTP 服务器， 连接 Nginx 和 Flask；

使用 Flask 写 API,通过检查 Headers 中的信息判断代理类型。

## 二、部署

参考 http://www.cnblogs.com/Ray-liang/p/4837850.html

#### 1、配置 Nginx
参考项目下的 **default**文件 做修改，放在 Nginx 对应目录下。（Ubuntu 放在 /etc/nginx/sites-enabled/）

#### 2、安装 python 依赖

```
pip install -r requirements.txt
```

#### 3、启动

```
gunicorn -w 4 -b 127.0.0.1:8080 http_proxy_checker:app
```

## 三、API

####