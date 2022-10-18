---
title: "Scraping a.href returns blank value?"
site: stackoverflow
question_id: 74114161
answer_id: 74114732
url: https://stackoverflow.com/a/74114732
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-18T16:57:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74114732/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3338751cef9a00cd75c9a86d55029ae54bec6edfb0462b262f26b1dccd1658b7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74114732>, 2022-10-18; score 0. Text as retrieved 2026-10-12.

The correct way to get the link [or `href` attributes] from every `a` tag is not `find_all('a.href')` as you have used it. You can instead do something like

```python
test = [s for s in soup.find_all('a') if s.get('href')]

#for just the links:
#test = [s.get('href') for s in soup.find_all('a') if s.get('href')]
```
and get the `a` tags that have `href` and are *available*  in the html you fetched.

I then printed with
```python
print(f'{len(test)} results:\n')
for t in test: print(f'[{t.get_text(strip=True)}]({t.get("href")})') 
```
to [view both the text and the link][1] in each tag.

<br>

**However** that will still not get you the data you mentioned wanting

> the name of each item plus the product code

because that has not been loaded in the html you fetched (you can check with a `print(soup.text)`...and also, if you try `print(soup.find('ul', {"id":"product-listing-container"}).prettify())` you will [see][2] that `ul#product-listing-container` is filled with "skeleton products" instead of having the `article` tag filled with attributes [as on the page after products have loaded][3]).

But I also noticed you have selenium in your imports, so it's easily resolved with that (you'll just have to have it confirm you're an adult and then wait for products to load and *then* use bs4 or just directly call selenium's `find_elements`...)


  [1]: https://i.sstatic.net/FaneL.png
  [2]: https://i.sstatic.net/2lu34.png
  [3]: https://i.sstatic.net/mkoDS.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Mark Tolonen](https://stackoverflow.com/users/235698)** (2022-10-18): Where possible, paste text into the answer itself instead of links to images.
- **me** (2022-10-19): @MarkTolonen I worried about the output adding to what already felt like a long answer...I'll try to start pasting the text more often. Thanks for the feedback
