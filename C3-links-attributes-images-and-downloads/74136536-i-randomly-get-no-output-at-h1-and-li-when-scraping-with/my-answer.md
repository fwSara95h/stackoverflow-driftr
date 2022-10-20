---
title: "I randomly get no output at <h1> and <Li> when scraping with beautifulsoup"
site: stackoverflow
question_id: 74136536
answer_id: 74146125
url: https://stackoverflow.com/a/74146125
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-20T20:44:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74146125/revisions
accepted: true
score: 1
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d6d1c6deb07aa1a3bcabe9bc976cd351328c986a7501afa02f6ae4bfd4ce7b31
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74146125>, 2022-10-20; **accepted**; score 1. Text as retrieved 2026-10-12.

When I tried to reproduce the *"no output possible"* scenario, I got it about 2% of the time; it was nearly always due to [503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) error; occasionally, status was 200 [OK], but content was empty - and I don't really know what might be causing that. (Btw, when working with requests, you should generally check that `status_code==200` before proceeding.)

One way to handle this would be to append , something like
```python
repeats = 0  # initiate
maxRepeats = 10 # limit allowed errors

abl_copy = audiobooklinks[:] # preserve original
for link in abl_copy:
    r = requests.get(link) #headers=headers)

    soup = BeautifulSoup(r.content, "lxml")

    if r.status_code != 200 or not r.content:
        print(f'! {r.status_code} {r.reason} - for {link} !')
        repeats += 1
        if maxRepeats < repeats: 
            print('! Stopping because of too many bad responses !')
            break
        abl_copy.append(link)
        continue
    
    soup = BeautifulSoup(r.content, "lxml")

    # rest of your for loop
```

There are many other ways to handle it as well - you could add a [wait](https://www.programiz.com/python-programming/time/sleep) every time you get 503, you could add all the bad responses [`r`] to a list and explore/handle them after the loop, etc...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[flexyflash](https://stackoverflow.com/users/20110941)** (2022-10-21): Thanks! This solved my problem. After appending your code, there have been no further issues!
