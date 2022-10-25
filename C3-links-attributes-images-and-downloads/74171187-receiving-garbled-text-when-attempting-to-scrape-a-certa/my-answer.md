---
title: "Receiving garbled text when attempting to scrape a certain website with Python using bs4"
site: stackoverflow
question_id: 74171187
answer_id: 74190308
url: https://stackoverflow.com/a/74190308
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-25T07:16:40Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74190308/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dced104a3df05be58c47b7de30419d9ee50349b6d978c1a215e0152da002a2a7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74190308>, 2022-10-25; score 0. Text as retrieved 2026-10-12.

As @SharuzzamanAhmatRaslan commented, *"that is not a garbled text. that is an image encoded in base64"* - the `href` value of that `link` tag just happens to be that long.

If you wish to quickly view the overall structure of the html tree, you could use `prettify` with this custom [formatter](https://tedboy.github.io/bs4_doc/8_output.html):
```python
def truncateIfLong(str, maxLen=15):
    if type(maxLen) != int: maxLen = 15 # [just in case]
    if maxLen < 4: maxLen = 5
    return str if len(str) < maxLen else str[:maxLen-3]+'...'
```
It will cut any long string down to 15 characters so that 
```python
print(soup.prettify(formatter=truncateIfLong))
```
only prints like

[![enter image description here][1]][1]

<hr>

However, it's still a huge output to be printing; probably better to save to a file with
```python
with open('x.html', 'w', encoding="utf8") as f:
    f.write(str(soup))
```

and then you can open x.html and view what has been retrieved, without any truncations.


  [1]: https://i.sstatic.net/Id9FJ.png
