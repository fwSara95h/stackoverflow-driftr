---
title: "How do I get the weather icon from the google weather service using BeautifulSoup?"
site: stackoverflow
question_id: 75565352
answer_id: 75567640
url: https://stackoverflow.com/a/75567640
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-25T18:46:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75567640/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 81a75d09bc0f05cf0a5f9ab59a31a28a3442353c2105a129192d92d9be4d8046
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75567640>, 2023-02-25; score 0. Text as retrieved 2026-10-12.

I have to agree with this:
> *Why scrape google in stead of using an open weather api? – [RJ Adriaansen](https://stackoverflow.com/users/11380795/rj-adriaansen)*

But if you still want to get the proper image data for `dimg_1`, it's actually inside a `script` tag<sup>([view example][1])</sup> and the `src` attribute from the source html is updated with JavaScript. You can extract the full image data from the `script` tag:

```py
dimg_id = 'dimg_1'
dimg_tag = soup.find('img', id=dimg_id)
print(dimg_tag)

dimg_script = soup.find('script', string=lambda s: s and "'dimg_1'" in s)
if dimg_script: 
    dimg_data = dimg_script.string.split("var s='",1)[-1].split("'",1)[0] 
```

However, `dimg_...` IDs are usually used for **thumbnails**, no the weather icons, which (as far as I can see) have **`id='wob_tci'`**<sup>([view example][2])</sup>, so maybe you should be getting the link first

```py
wi_src = soup.find('img', id='wob_tci', src=True)['src']
```

so that you can do [something like this](https://stackoverflow.com/a/69578583/6146136).

  [1]: https://i.sstatic.net/XZ5SC.png
  [2]: https://i.sstatic.net/wbDD2.png
