---
title: "How to make a \"RequestsCookieJar\" object for a GET request from an existing cookie as \"dictionary\" type in Python"
site: stackoverflow
question_id: 75495979
answer_id: 75496595
url: https://stackoverflow.com/a/75496595
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-18T21:47:37Z
last_edited: 2023-02-18T21:55:55Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75496595/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8515309b8e97a08be795c46fadfd1377cfcbcbb7b5387107ba3035788887a5c6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75496595>, 2023-02-18, last edited 2023-02-18; score 0. Text as retrieved 2026-10-12.

If you first alter the structure a bit with

```python
cookieList = [  {'domain': 'x.com', 'httpOnly': True, 'name': 'Username_COOKIE', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676724072, 'httpOnly': False, 'name': 'ASP.NET_SessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676810425, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'}  ]

for ci, c in enumerate(cookieList):
    if 'httpOnly' in c: 
        cookieList[ci]['rest'] = {'HttpOnly': c['httpOnly']}
        del cookieList[ci]['httpOnly']
    if 'expiry' in c:
        cookieList[ci]['expires'] = c['expiry']
        del cookieList[ci]['expiry']
```

so that `cookieList` looks like 

>```python
> [{'domain': 'x.com',
>   'name': 'Username_COOKIE',
>   'path': '/',
>   'sameSite': 'Lax',
>   'secure': False,
>   'value': 'some value',
>   'rest': {'HttpOnly': True}},
>  {'domain': 'x.com',
>   'name': 'ASP.NET_SessionId',
>   'path': '/',
>   'sameSite': 'Lax',
>   'secure': False,
>   'value': 'some value',
>   'rest': {'HttpOnly': False},
>   'expires': 1676724072},
>  {'domain': 'x.com',
>   'name': '_gid',
>   'path': '/',
>   'sameSite': 'Lax',
>   'secure': False,
>   'value': 'some value',
>   'rest': {'HttpOnly': False},
>   'expires': 1676810425}]
>```

then you can turn it into a [RequestsCookieJar](https://requests.readthedocs.io/en/latest/api/#requests.cookies.RequestsCookieJar) object with

```python
# import requests
cKeys = ['version', 'name', 'value', 'port', 'domain', 'path', 'secure', 
         'expires', 'discard', 'comment', 'comment_url', 'rest', 'rfc2109']

jar = requests.cookies.RequestsCookieJar()
for c in cookieList: jar.set(**{k:v for k,v in c.items() if k in cKeys})
```

You can now [use](https://requests.readthedocs.io/en/latest/user/quickstart/#cookies) `jar` like **<kbd>requests.get(url, cookies=jar)</kbd>**, or view it with `print(repr(jar))` which should output something like 

>```python
> <RequestsCookieJar[
>   Cookie(version=0, name='ASP.NET_SessionId', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1676724072, discard=True, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False), 
>   Cookie(version=0, name='Username_COOKIE', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': True}, rfc2109=False), 
>   Cookie(version=0, name='_gid', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1676810425, discard=True, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
> ]>
>```


----

You *might* also be able to just get away with 

```python
cookieList = [  {'domain': 'x.com', 'httpOnly': True, 'name': 'Username_COOKIE', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676724072, 'httpOnly': False, 'name': 'ASP.NET_SessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676810425, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'}  ]

cookiesDict = {c['name']:c['value'] for c in cookieList if 'name' in c and 'value' in c}
resp = requests.get(url, cookies=cookiesDict)
```
