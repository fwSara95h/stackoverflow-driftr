---
title: "Payload to scrape data not working anymore"
site: stackoverflow
question_id: 74280152
answer_id: 74280997
url: https://stackoverflow.com/a/74280997
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T19:38:17Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74280997/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f65d7a088ea219a403c6920a85c6def7a72ebc8ed3ecfa1ff709b9e291e79b8a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74280997>, 2022-11-01; **accepted**; score 0. Text as retrieved 2026-10-12.

The error just means that the response wasn't proper json format. You can check for it by splitting up that `data = requests.post(url, json=payload).json()` line to something like 
```python
res = requests.post(url, json=payload)
# res.raise_for_status() # just in case

if 'application/json' in res.headers['Content-Type']: 
    data = res.json()
else:
    print('unexpected format')
    break # or however else you want to handle it
```

<hr>

(If I try running your code with this change and then I try exploring `res.content`, it's just a html with text that boils down to *"Printables This site requires JavaScript enabled"*.)

As for *why* the response isn't json, are you **sure** you're using the right url? I get json responses if I send the same requests to "https://**api**.printables.com/graphql/" (instead of "https://**www**.printables.com/graphql/")...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ablam](https://stackoverflow.com/users/11981271)** (2022-11-01): Thank you. I retrieved the URL from the developer tools section. If I may ask, how did you know changing it to "api" as supposed to "www" would be a mitigation/solution?
- **me** (2022-11-01): @ablam I didn't know, actually - I wasn't sure *exactly* which page you got the payload from, but I went to https://www.printables.com/model to look at network traffic involving graphql [[screenshot](https://i.sstatic.net/8WPXy.png)]. I wanted to check if maybe there was an api key or some important part of the headers that you were missing, but what I noticed instead was that all graphql request urls seemed to start with "api" rather than "www"...hope this helped :)
