### 一、HTTP请求（http request）

**请求格式：**

客户端发送一个HTTP请求到服务器的请求消息由 `请求行`、`请求头`、`空行` 和 `请求数据` 四个部分组成。

```
<request-line>
<general-headers>
<request-headers>
<entity-headers>
<empty-line>
[<message-body>]
```

**1. 请求行**

请求行是请求消息的第一行，由三部分组成：

- 请求方法（GET/POST/DELETE/PUT/HEAD/···)
- 请求资源的 URI 路径
- HTTP 的版本号

```
GET http://www.ruanyifeng.com/blog/2016/08/http.html HTTP/1.1
```

**2. 请求头（request headers）**

请求头中的信息有和缓存相关的头（Cache-Control，If-Modified-Since）、客户端身份信息（User-Agent）等等

```
Host: www.ruanyifeng.com
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://www.google.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.1313673471.1541381842; _gid=GA1.2.803875058.1541381842; Hm_lvt_f89e0235da0841927341497d774e7b15=1541381843,1541382227; Hm_lpvt_f89e0235da0841927341497d774e7b15=1541382227
If-None-Match: "19f22-579cff38d24b0-gzip"
If-Modified-Since: Sun, 04 Nov 2018 05:22:14 GMT
```

**3. 消息体**

请求体是客户端发给服务端的请求数据，这部分数据并不是每个请求必须的。

#### http请求方法（HTTP Request Method）

http的请求行由：**请求方法** + **请求资源的 URI 路径** + **HTTP 版本号**组成。

根据HTTP标准，HTTP请求可以使用多种请求方法

- HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法。
- HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。

**GET**
请求指定的页面信息，并返回实体主体
```
curl -i -v http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 93.184.216.34...
* TCP_NODELAY set
* Connected to example.com (93.184.216.34) port 80 (#0)
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Cache-Control: max-age=604800
Cache-Control: max-age=604800
< Content-Type: text/html; charset=UTF-8
Content-Type: text/html; charset=UTF-8
< Date: Mon, 05 Nov 2018 02:39:45 GMT
Date: Mon, 05 Nov 2018 02:39:45 GMT
< Etag: "1541025663+ident"
Etag: "1541025663+ident"
< Expires: Mon, 12 Nov 2018 02:39:45 GMT
Expires: Mon, 12 Nov 2018 02:39:45 GMT
< Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
< Server: ECS (sjc/4EC1)
Server: ECS (sjc/4EC1)
< Vary: Accept-Encoding
Vary: Accept-Encoding
< X-Cache: HIT
X-Cache: HIT
< Content-Length: 1270
Content-Length: 1270

<
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 50px;
        background-color: #fff;
        border-radius: 1em;
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        body {
            background-color: #fff;
        }
        div {
            width: auto;
            margin: 0 auto;
            border-radius: 0;
            padding: 1em;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is established to be used for illustrative examples in documents. You may use this
    domain in examples without prior coordination or asking for permission.</p>
    <p><a href="http://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
* Connection #0 to host example.com left intact
```

**HEAD**
类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头

```
* Rebuilt URL to: http://example.com/
*   Trying 93.184.216.34...
* TCP_NODELAY set
* Connected to example.com (93.184.216.34) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Accept-Ranges: bytes
Accept-Ranges: bytes
< Cache-Control: max-age=604800
Cache-Control: max-age=604800
< Content-Type: text/html; charset=UTF-8
Content-Type: text/html; charset=UTF-8
< Date: Mon, 05 Nov 2018 02:43:33 GMT
Date: Mon, 05 Nov 2018 02:43:33 GMT
< Etag: "1541025663"
Etag: "1541025663"
< Expires: Mon, 12 Nov 2018 02:43:33 GMT
Expires: Mon, 12 Nov 2018 02:43:33 GMT
< Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
< Server: ECS (oxr/83B7)
Server: ECS (oxr/83B7)
< X-Cache: HIT
X-Cache: HIT
< Content-Length: 1270
Content-Length: 1270
```

**POST**
向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改
```
curl -d "a=123" http://example.com -v
* Rebuilt URL to: http://example.com/
*   Trying 93.184.216.34...
* TCP_NODELAY set
* Connected to example.com (93.184.216.34) port 80 (#0)
> POST / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
> Content-Length: 5
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 5 out of 5 bytes
< HTTP/1.1 200 OK
< Accept-Ranges: bytes
< Cache-Control: max-age=604800
< Content-Type: text/html; charset=UTF-8
< Date: Mon, 05 Nov 2018 02:46:28 GMT
< Etag: "1541025663"
< Expires: Mon, 12 Nov 2018 02:46:28 GMT
< Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
< Server: EOS (vny006/044F)
< Content-Length: 1270
<
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 50px;
        background-color: #fff;
        border-radius: 1em;
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        body {
            background-color: #fff;
        }
        div {
            width: auto;
            margin: 0 auto;
            border-radius: 0;
            padding: 1em;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is established to be used for illustrative examples in documents. You may use this
    domain in examples without prior coordination or asking for permission.</p>
    <p><a href="http://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
* Connection #0 to host example.com left intact
```

**PUT**
从客户端向服务器传送的数据取代指定的文档的内容

**DELETE**
求服务器删除指定的页面

**CONNECT**
HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器

**OPTIONS**
客户端询问服务器可以提交哪些请求方法

```
curl -I -X OPTIONS http://example.com
HTTP/1.1 200 OK
Allow: OPTIONS, GET, HEAD, POST
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Mon, 05 Nov 2018 02:56:12 GMT
Expires: Mon, 12 Nov 2018 02:56:12 GMT
Server: EOS (vny006/044E)
Content-Length: 0
```

**TRACE**
客户端可以对请求消息的传输路径进行追踪，回显服务器收到的请求，主要用于测试或诊断

**PATCH**
实体中包含一个表，表中说明与该URI所表示的原内容的区别

**MOVE**
请求服务器将指定的页面移至另一个网络地址

**COPY**
请求服务器将指定的页面拷贝至另一个网络地址

**LINK**
请求服务器建立链接关系

**UNLINK**
断开链接关系

**WRAPPED**
允许客户端发送经过封装的请求

**Extension-mothed**
在不改动协议的前提下，可增加另外的方法

### 二、HTTP响应（http response）

**响应格式**

服务器接收处理完请求后返回一个 HTTP 相应消息给客户端。HTTP 响应消息的格式包括：`状态行`、`响应头`、`空行`、`消息体`

```
<status-line>
<general-headers>
<response-headers>
<entity-headers>
<empty-line>
[<message-body>]
```

**状态行**

状态行位于相应消息的第一行，有 HTTP 协议版本号，状态码和状态说明三部分构成

```
HTTP/1.1 200 OK
```

**响应头**

响应头是服务器传递给客户端用于说明服务器的一些信息，以及将来继续访问该资源时的策略

```
Connection:keep-alive
Content-Encoding:gzip
Content-Type:text/html; charset=utf-8
Date:Fri, 24 Jun 2016 06:23:31 GMT
Server:nginx/1.9.12
Transfer-Encoding:chunked
```

**响应体**

响应体是服务端返回给客户端的 HTML 文本内容，或者其他格式的数据，比如：视频流、图片或者音频数据。

### HTTP响应状态码

**状态码类别**
状态代码由三位数字组成，第一个数字定义了响应的类别，共分五种类别:

- 1xx：指示信息
表示请求已接收，继续处理

- 2xx：成功
表示请求已被成功接收、理解、接受

- 3xx：重定向
要完成请求必须进行更进一步的操作

- 4xx：客户端错误
请求有语法错误或请求无法实现

- 5xx：服务器端错误
服务器未能实现合法的请求

**常见状态码**
- 200 OK
客户端请求成功

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:03:49 GMT
< Content-Type: application/octet-stream
< Content-Length: 0
< Connection: keep-alive

<
* Connection #0 to host example.com left intact
```
- 400 Bad Request
客户端请求有语法错误，不能被服务器理解

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 400 Bad Request
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:02:37 GMT
< Content-Type: text/html
< Content-Length: 173
< Connection: close

<
* Closing connection 0
```

- 401 Unauthorized
请求未经授权，该状态码和WWW-Authenticate报头域一起使用

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 401 Unauthorized
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:04:33 GMT
< Content-Type: text/html
< Content-Length: 195
< Connection: keep-alive

<
* Connection #0 to host example.com left intact
```

- 403 Forbidden
服务器收到请求，但拒绝提供服务

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:06:08 GMT
< Content-Type: text/html
< Content-Length: 169
< Connection: keep-alive

<
* Connection #0 to host example.com left intact
```

- 404 Not Found
请求资源不存在

```
$ curl -v -I http://example.com/1.jpg
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD /1.jpg HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 404 Not Found
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:07:21 GMT
< Content-Type: text/html
< Content-Length: 169
< Connection: keep-alive

<
* Connection #0 to host example.com left intact
```

- 500 Internal Server Error
服务器发生了非预期错误

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:07:56 GMT
< Content-Type: text/html
< Content-Length: 193
< Connection: close

<
* Closing connection 0
```

- 503 Server Unavailable
服务器当前不能处理客户端的请求

```
$ curl -v -I http://example.com
* Rebuilt URL to: http://example.com/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to example.com (127.0.0.1) port 80 (#0)
> HEAD / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 503 Service Temporarily Unavailable
< Server: nginx/1.10.3
< Date: Fri, 30 Mar 2018 07:08:34 GMT
< Content-Type: text/html
< Content-Length: 213
< Connection: keep-alive

<
* Connection #0 to host example.com left intact
```
