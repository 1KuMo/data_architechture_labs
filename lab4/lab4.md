1.1 ) the loopback interface name is ' lo ' and the IPv4 address assigned to it is 127.0.0.1

```

[toadmini@toadmini ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether d4:d8:53:2e:4a:be brd ff:ff:ff:ff:ff:ff
    altname wlxd4d8532e4abe
    inet 192.168.1.139/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 41069sec preferred_lft 41069sec
    inet6 2a01:e0a:f84:f910:a168:6fd2:4980:9579/64 scope global dynamic noprefixroute
       valid_lft 86013sec preferred_lft 86013sec
    inet6 fe80::ea95:bc05:5a52:6289/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 0
    link/ether d2:97:94:e3:ca:fe brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
[toadmini@toadmini ~]$```

```



1.2 ) I suppose the command is used to display active ports since port 80 and 8080 are not displayed by the command, I assume they're not occupied by any service at all
```
[sudo] password for toadmini:
Netid State  Recv-Q Send-Q  Local Address:Port    Peer Address:Port
udp   UNCONN 0      0             0.0.0.0:5353         0.0.0.0:*
udp   UNCONN 0      0                [::]:5353            [::]:*
udp   UNCONN 0      0                   *:38706              *:*
udp   UNCONN 0      0                   *:49272              *:*
udp   UNCONN 0      0                   *:34259              *:*
tcp   LISTEN 0      4096        127.0.0.1:37433        0.0.0.0:*
[toadmini@toadmini ~]$
```



PART II 

2.1 ) 
```
[toadmini@toadmini ~]$ curl https://api.github.com/zen
Avoid administrative distraction.[toadmini@toadmini ~]$
```

2.2) 
```
[toadmini@toadmini ~]$ curl -v https://api.github.com/zen
* Host api.github.com:443 was resolved.
* IPv6: (none)
* IPv4: 140.82.121.5
*   Trying 140.82.121.5:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / x25519 / id-ecPublicKey
* ALPN: server accepted h2
* Server certificate:
*   subject: CN=*.github.com
*   start date: Oct 28 00:00:00 2026 GMT
*   expire date: Jan 25 23:59:59 2027 GMT
*   issuer: C=GB; O=Sectigo Limited; CN=Sectigo Public Server Authentication CA DV E36
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA256
*   Certificate level 1: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA384
*   Certificate level 2: Public key type EC/secp384r1 (384/192 Bits/secBits), signed using ecdsa-with-SHA384
*   subjectAltName: "api.github.com" matches cert's "*.github.com"
* OpenSSL verify result: 0
* SSL certificate verified via OpenSSL.
* Established connection to api.github.com (140.82.121.5 port 443) from 192.168.1.139 port 36636
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://api.github.com/zen
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: api.github.com]
* [HTTP/2] [1] [:path: /zen]
* [HTTP/2] [1] [user-agent: curl/8.23.0]
* [HTTP/2] [1] [accept: */*]
> GET /zen HTTP/2
> Host: api.github.com
> User-Agent: curl/8.23.0
> Accept: */*
>
* Request completely sent off
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 200
[toadmini@toadmini ~]$ [toadmini@toadmini ~]$ curl -v https://api.github.com/zen
* Host api.github.com:443 was resolved.
* IPv6: (none)
* IPv4: 140.82.121.5
*   Trying 140.82.121.5:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / x25519 / id-ecPublicKey
* ALPN: server accepted h2
* Server certificate:
*   subject: CN=*.github.com
*   start date: Oct 28 00:00:00 2026 GMT
*   expire date: Jan 25 23:59:59 2027 GMT
*   issuer: C=GB; O=Sectigo Limited; CN=Sectigo Public Server Authentication CA DV E36
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA256
*   Certificate level 1: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA384
*   Certificate level 2: Public key type EC/secp384r1 (384/192 Bits/secBits), signed using ecdsa-with-SHA384
*   subjectAltName: "api.github.com" matches cert's "*.github.com"
* OpenSSL verify result: 0
* SSL certificate verified via OpenSSL.
* Established connection to api.github.com (140.82.121.5 port 443) from 192.168.1.139 port 36636
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://api.github.com/zen
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: api.github.com]
* [HTTP/2] [1] [:path: /zen]
* [HTTP/2] [1] [user-agent: curl/8.23.0]
* [HTTP/2] [1] [accept: */*]
> GET /zen HTTP/2
> Host: api.github.com
> User-Agent: curl/8.23.0
> Accept: */*
>
* Request completely sent off
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 200
< date: Thu, 05 Nov 2026 10:42:01 GMT
< content-type: text/plain;charset=utf-8
< x-github-api-version-selected: 2022-11-28
< access-control-expose-headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset, Warning
< access-control-allow-origin: *
< strict-transport-security: max-age=31536000; includeSubdomains; preload
< x-frame-options: deny
< x-content-type-options: nosniff
< x-xss-protection: 0
< referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
< content-security-policy: default-src 'none'
< vary: Accept-Encoding, Accept, X-Requested-With
< server: github.com
< accept-ranges: bytes
< x-ratelimit-limit: 60
< x-ratelimit-remaining: 58
< x-ratelimit-used: 2
< x-ratelimit-resource: core
< x-ratelimit-reset: 1793878804
< content-length: 39
< x-github-request-id: 4398:167305:971AB66:DE3186C:6AEC5D80
< x-github-edge-region: fra
<
* Connection #0 to host api.github.com:443 left intact
It's not fully shipped until it's fast.[toadmini@toadmini ~]$
```
here the screenshots as asked :
![[Pasted image 20261105114410.png]]![[Pasted image 20261105114424.png]]![[Pasted image 20261105114450.png]]![[Pasted image 20261105114807.png]]


so the content type line is this one ;
```
< content-type: text/plain;charset=utf-8
```
and the HTTP/1.1 200 OK status line is this one  ( appears that the protocol used is different as you said during the course, so it might be unstable );
```
< HTTP/2 200
```


PART III

3.1 ) 
```
[toadmini@toadmini ~]$ curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer mock_token_123" \
  -d '{"sensor_id": "temp_sensor_01", "metric_value": 24.5, "status": "active"}' \
  https://httpbin.org/post
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Authorization": "Bearer mock_token_123",
    "Content-Length": "73",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "curl/8.23.0"
  },
  "method": "POST",
  "origin": "88.190.19.228",
  "url": "https://httpbin.org/post",
  "data": "{\"sensor_id\": \"temp_sensor_01\", \"metric_value\": 24.5, \"status\": \"active\"}",
  "files": {},
  "form": {},
  "json": {
    "metric_value": 24.5,
    "sensor_id": "temp_sensor_01",
    "status": "active"
  }
}
[toadmini@toadmini ~]$
```

3.2 ) 
As I understood,the objective is to test out on a real ( test ) server our requests, to check if they're well written. We send a request to the server via the method POST which is used to send data, and the server send back to us a JSON file containing what we sent to him. In that way we can check if the server 'understood' everything that we gave him
-> by seeing if the body was parsed correctly, no missing data, correct request method etc... 

1- The server well received the POST method (  "method": "POST", )
2 -  in our request, we had 
``` 
-H "Content-Type: application/json" \
-H "Authorization: Bearer mock_token_123" \
```
and in the JSON returned by the server we can see in the headers section : 
```   
	"Content-Type": "application/json",
    "Authorization": "Bearer mock_token_123",
```
3- finally, our datas ( the body ) have been successfully transmitted and parsed by the server
```
"json": {
  "metric_value": 24.5,
  "sensor_id": "temp_sensor_01",
  "status": "active"
}
```


PART IV 

![[Pasted image 20261105120949.png]]