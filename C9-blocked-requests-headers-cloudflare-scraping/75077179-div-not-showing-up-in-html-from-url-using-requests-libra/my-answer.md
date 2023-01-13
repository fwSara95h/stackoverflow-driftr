---
title: "div not showing up in html from url using requests library and bs4"
site: stackoverflow
question_id: 75077179
answer_id: 75104039
url: https://stackoverflow.com/a/75104039
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-13T01:37:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75104039/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 028516ffd71e370e99ec21c7f7170e2d9dbb93d1de49ba8e7147473cdbcf5fbb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75104039>, 2023-01-13; score 0. Text as retrieved 2026-10-12.

> I just logged out from my browser and it showed me a different page. However, my script has no login part at all. Not even sure how that would work

[It doesn't work with all sites, but it seems to be enough for this site so far.] You can login with `request.Session`.

```python
# import requests

sess = requests.Session()
headers = {'user-agent': 'Mozilla/5.0'}
data = {'username': 'YOUR_EMAIL/USERNAME', 'password': 'YOUR_PASSWORD'}

loginResp = sess.post('https://untappd.com/login', headers=headers, data=data)
print(loginResp.status_code, loginResp.reason, 'from', loginResp.url) ## should print 200 OK...

response = sess.get(venue_url, headers = {'User-agent': 'Mozilla/5.0'})
## CAN CONTINUE AS BEFORE ##
```

---

I've edited my [solution](https://pastebin.com/RywJxpbM) to one of your previous questions about this site to include cookies so that the site will treat you as logged in. For example:

```python
# venue_url = 'https://untappd.com/v/glory-days-grill-of-ellicott-city/3329822'
gloryMenu = scrape_untappd_menu(venue_url, cookies=sess.cookies)
```

will collect the following data:

[![op][1]][1]

---

**Note:** They have a captcha when logging in so I was worried it would be too hard to automate; if it becomes an issue, you can [probably] still login on your browser before going to the page and then paste the request from your network log to [curlconverter](https://curlconverter.com/) to get the cookies as a dictionary. Ofc the process is then no longer fully automated since you'll have to repeat this manual login every time the cookies expire (which could be as fast as a few hours). If you wanted to automate the login at that point, you might have to use some kind of browser automation like [with selenium](https://medium.com/ymedialabs-innovation/2f8ad15efe25).  


  [1]: https://i.sstatic.net/cHHCv.png
