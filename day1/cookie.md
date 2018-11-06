### Cookie
HTTP Cookie（也叫Web Cookie或浏览器Cookie）是服务器发送到用户浏览器并保存在本地的一小块数据，它会在浏览器下次向同一服务器再发起请求时被携带并发送到服务器上。通常，它用于告知服务端两个请求是否来自同一浏览器，如保持用户的登录状态。Cookie使基于无状态的HTTP协议记录稳定的状态信息成为了可能。

Cookie主要用于以下三个方面：

- 会话状态管理（如用户登录状态、购物车、游戏分数或其它需要记录的信息）
- 个性化设置（如用户自定义设置、主题等）
- 浏览器行为跟踪（如跟踪分析用户行为等）

Cookie曾一度用于客户端数据的存储，因当时并没有其它合适的存储办法而作为唯一的存储手段，但现在随着现代浏览器开始支持各种各样的存储方式，Cookie渐渐被淘汰。由于服务器指定Cookie后，浏览器的每次请求都会携带Cookie数据，会带来额外的性能开销（尤其是在移动环境下）。新的浏览器API已经允许开发者直接将数据存储到本地，如使用 Web storage API （本地存储和会话存储）或 IndexedDB 。

#### 创建Cookie
当服务器收到HTTP请求时，服务器可以在响应头里面添加一个Set-Cookie选项。浏览器收到响应后通常会保存下Cookie，之后对该服务器每一次请求中都通过Cookie请求头部将Cookie信息发送给服务器。另外，Cookie的过期时间、域、路径、有效期、适用站点都可以根据需要来指定。

**Set-Cookie响应头和Cookie请求头**

服务器使用Set-Cookie响应头部向用户代理（一般是浏览器）发送Cookie信息

```
Set-Cookie: <cookie名>=<cookie值>
```
服务器通过该头部告知客户端保存Cookie信息。

```
HTTP/1.0 200 OK
Content-type: text/html
Set-Cookie: test_cookie_a=a
Set-Cookie: test_cookie_b=b

[body]
```

**会话期Cookie**

浏览器关闭之后它会被自动删除，仅在会话期内有效。会话期Cookie不需要指定过期时间（Expires）或者有效期（Max-Age）。有些浏览器提供了会话恢复功能，这种情况下即使关闭了浏览器，会话期Cookie也会被保留下来。

**持久性Cookie**
和关闭浏览器便失效的会话期Cookie不同，持久性Cookie可以指定一个特定的过期时间（Expires）或有效期（Max-Age）。

```
Set-Cookie: id=admin; Expires=Wed, 21 Oct 2015 07:28:00 GMT;
```

**Cookie的Secure 和HttpOnly 标记**

安全的Cookie只应通过HTTPS协议加密过的请求发送给服务端。即便设置了 Secure 标记，敏感信息也不应该通过Cookie传输，因为Cookie有其固有的不安全性，Secure 标记也无法提供确实的安全保障。从 Chrome 52 和 Firefox 52 开始，不安全的站点（http:）无法使用Cookie的 Secure 标记。

为避免跨域脚本 (XSS) 攻击，通过JavaScript的 Document.cookie API无法访问带有 HttpOnly 标记的Cookie，它们只应该发送给服务端。如果包含服务端 Session 信息的 Cookie 不想被客户端 JavaScript 脚本调用，那么就应该为其设置 HttpOnly 标记。

```
Set-Cookie: id=admin; Expires=Wed, 21 Oct 2015 07:28:00 GMT; Secure; HttpOnly
```

**Cookie的作用域**

Domain 和 Path 标识定义了Cookie的作用域：即Cookie应该发送给哪些URL。

Domain 标识指定了哪些主机可以接受Cookie。如果不指定，默认为当前文档的主机（不包含子域名）。如果指定了Domain，则一般包含子域名。

例如，如果设置 `Domain=example.com`，则Cookie也包含在子域名中`*.example.com`。

Path 标识指定了主机下的哪些路径可以接受Cookie（该URL路径必须存在于请求URL中）。以字符 `%2F` ("/") 作为路径分隔符，子路径也会被匹配。

例如，设置 `Path=/docs`，则以下地址都会匹配：

- /docs
- /docs/Web/
- /docs/Web/HTTP

**SameSite Cookies**

`SameSite Cookie`允许服务器指定在跨站请求时该Cookie是否会被发送，从而可以阻止跨站请求伪造攻击（CSRF）。但目前SameSite Cookie并不是所有浏览器都支持

**Document.cookies**

通过`Document.cookie`属性可创建新的Cookie，也可通过该属性访问非HttpOnly标记的Cookie。

```
document.cookie = "test_cookie_a=a"; 
document.cookie = "test_cookie_b=b"; 
console.log(document.cookie); 
// logs "test_cookie_a=a; test_cookie_b=b"
```