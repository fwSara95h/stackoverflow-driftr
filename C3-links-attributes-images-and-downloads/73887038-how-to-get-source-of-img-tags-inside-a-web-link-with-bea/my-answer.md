---
title: "how to get source of img tags inside a web link with beautiful soup 4"
site: stackoverflow
question_id: 73887038
answer_id: 73887424
url: https://stackoverflow.com/a/73887424
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T20:27:01Z
last_edited: 2022-09-28T21:02:14Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73887424/revisions
accepted: true
score: 1
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4af2b7e18c8bcda8ae4d7cd3a35ccae3de2b895d86e7ba21bdca14c7f79ba96d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73887424>, 2022-09-28, last edited 2022-09-28; **accepted**; score 1. Text as retrieved 2026-10-12.

The actual image link is in the `data-original` attribute but it has to be accessed via proxy, so they set the `src` as the loading gif (that you kept getting) until they have fetched the image and can update `src`. But you can form that link for fetching the actual page image by altering your code to:

    from bs4 import BeautifulSoup
    import requests
    
    r = requests.get("https://welovemanga.one/2777/92578/")
    soup = BeautifulSoup(r.content, "html.parser")
    thumbnail_elements = soup.find_all("img", class_ = "chapter-img")
    proxyRoot = 'https://welovekai.com/proxy.php?link='
    
    for element in thumbnail_elements:
        print(proxyRoot+''.join(element['data-original'].split()))
        
[There's some whitespaces breaking up the link, so `split`ting and then `join`ing cleans it up.]
