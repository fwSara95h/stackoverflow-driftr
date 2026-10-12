# Code from my Stack Overflow answer https://stackoverflow.com/a/75496595 (posted 2023-02-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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
>

# --- block 3 ---
# import requests
cKeys = ['version', 'name', 'value', 'port', 'domain', 'path', 'secure', 
         'expires', 'discard', 'comment', 'comment_url', 'rest', 'rfc2109']

jar = requests.cookies.RequestsCookieJar()
for c in cookieList: jar.set(**{k:v for k,v in c.items() if k in cKeys})

# --- block 4 ---
> <RequestsCookieJar[
>   Cookie(version=0, name='ASP.NET_SessionId', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1676724072, discard=True, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False), 
>   Cookie(version=0, name='Username_COOKIE', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': True}, rfc2109=False), 
>   Cookie(version=0, name='_gid', value='some value', port=None, port_specified=False, domain='x.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=1676810425, discard=True, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
> ]>
>

# --- block 5 ---
cookieList = [  {'domain': 'x.com', 'httpOnly': True, 'name': 'Username_COOKIE', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676724072, 'httpOnly': False, 'name': 'ASP.NET_SessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'},
                {'domain': 'x.com', 'expiry': 1676810425, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'some value'}  ]

cookiesDict = {c['name']:c['value'] for c in cookieList if 'name' in c and 'value' in c}
resp = requests.get(url, cookies=cookiesDict)
