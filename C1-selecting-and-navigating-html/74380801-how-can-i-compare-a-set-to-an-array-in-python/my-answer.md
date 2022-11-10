---
title: "How can I compare a set to an array in Python?"
site: stackoverflow
question_id: 74380801
answer_id: 74384000
url: https://stackoverflow.com/a/74384000
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-10T04:03:21Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74384000/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 41fdabc29b310245ce1d562401303f4d8aafdce8eca989013322c538c91da6d1
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74384000>, 2022-11-10; **accepted**; score 1. Text as retrieved 2026-10-12.

> I thought I could append unique URLs to a list then to a set and then to a tuple to compare against the array but that doesn't seem to be working.

Instead, you could just only add URLs that haven't been added already by adding maintaining and checking against a list of URLs that *have* been added already. Try
```python
prev_links = [r[2] for r in sh.get_all_values()]
ar = []

# (I prefer to define constants outside loop) 
abs_url = "https://www.ig.com" 
h_selector = 'h3[class="article-category-section-title"]'
link_selector = f'{h_selector} a[class="primary js_target"][href]'

for url in urls:
    my_url = requests.get(url)
    html = my_url.content
    soup = BeautifulSoup(html, "html.parser")

    date_today = str(datetime.date.today())
    for arLink in soup.select(link_selector):
        rel_url = arLink.get("href")
        full_url = urllib.parse.urljoin(abs_url, rel_url)
        article = str(full_url.replace("https://",""))
        if article in prev_links: 
            continue # skip if already added

        title = arLink.text.strip()
        pub_date = rel_url[-6:]
        pub_date = f"{pub_date[4:6]} {pub_date[2:4]} {pub_date[0:2]}"

        ar.append([date_today, title, article, pub_date]) # no need for str() - they're all strings already
        prev_links.append(article) # maintain list of already-added-urls

if ar != []:
    sh.append_rows(ar, value_input_option="USER_ENTERED")
```
