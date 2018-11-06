### HTTP身份验证

HTTP 提供一个用于权限控制和认证的通用框架。最常用的HTTP认证方案是HTTP Basic authentication

**通用的 HTTP 认证框架**
`RFC 7235` 定义了一个 HTTP 身份验证框架，服务器可以用来针对客户端的请求发送 `challenge` （质询信息），客户端则可以用来提供身份验证凭证。质询与应答的工作流程如下：服务器端向客户端返回 401 状态码，并在 `WWW-Authenticate` 首部提供如何进行验证的信息，其中至少包含有一种质询方式。之后有意向证明自己身份的客户端可以在新的请求中添加 `Authorization` 首部字段进行验证，字段值为身份验证凭证信息。通常客户端会弹出一个密码框让用户填写，然后发送包含有恰当的 `Authorization` 首部的请求。信息交换须通过 `HTTPS(TLS)` 连接来保证安全

![](/picture/2018-11-06-11-24-10.png)

**WWW-Authenticate 与 Proxy-Authenticate 首部**
`WWW-Authenticate` 与 `Proxy-Authenticate` 响应消息首部指定了为获取资源访问权限而进行身份验证的方法。它们需要明确要进行验证的方案，这样希望进行授权的客户端就知道该如何提供凭证信息

语法形式：
```html
WWW-Authenticate: <type> realm=<realm>
Proxy-Authenticate: <type> realm=<realm>
```
`<type>` 指的是验证的方案。realm 用来描述进行保护的区域，或者指代保护的范围。它可以是类似于 "Access to the staging site" 的消息，这样用户就可以知道他们正在试图访问哪一空间。

#### 验证方案
通用 HTTP 身份验证框架可以被多个验证方案使用。不同的验证方案会在安全强度以及在客户端或服务器端软件中可获得的难易程度上有所不同。

最常见的验证方案是基本验证方案（Basic）。常见的验证方案包括：

- Basic
- Bearer
- Digest
- HOBA
- Mutual
- AWS4-HMAC-SHA256
