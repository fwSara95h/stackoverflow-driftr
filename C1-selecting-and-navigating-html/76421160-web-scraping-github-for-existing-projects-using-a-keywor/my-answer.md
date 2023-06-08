---
title: "Web Scraping Github for existing projects using a keyword"
site: stackoverflow
question_id: 76421160
answer_id: 76431395
url: https://stackoverflow.com/a/76431395
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-08T11:28:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76431395/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a6014f715db23a24e5fe4e9e66f2095f5e869aeea4aeac2146703b5440c6bdb6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76431395>, 2023-06-08; score 0. Text as retrieved 2026-10-12.

[As baduker commented, it's better to use the [ GitHub Search API](https://docs.github.com/en/rest/search?apiVersion=2022-11-28) for this; but also,] you should be using different `attrs` for each column -  you need to inspect `soup` more thoroughly to figure out which attributes are common to *all* the sections you want each column value from. 

<sup>**(Keep in mind that the `r.text` you request can be different from what you inspected on your browser and attributes that seem to be randomly generated - like *`Box-sc-g0xbh4-0 jUbAHB`*/*`Link__StyledLink-sc-14289xe-0 bJBoUI`*/*`Text-sc-17v1xeu-0 kWPXhV`*/*`Text-sc-17v1xeu-0 gPDEWA`* - are prone to changing and are therefore not reliable for scraping; look for more human-readable attributes which are less likely to change.)**</sup>

---

If you edit your `for` loop to something like 

```py
for repo in soup.findAll('li', attrs={'class': 'repo-list-item'}):
    rep = repo.find('a', attrs={'href': True, 'class':'v-align-middle'})
    descp = repo.find('p', attrs={'class': 'mb-1'})
    dt = repo.find('relative-time', attrs={'datetime': True}) 

    date.append(dt['datetime']) 
    rep_link.append(rep['href'])
    description.append(None if descp is None else descp.text.strip()) 
    ## not all repos have description
```

then `df` might look something like

[![opdf][1]][1]


  [1]: https://i.sstatic.net/XZvln.png
