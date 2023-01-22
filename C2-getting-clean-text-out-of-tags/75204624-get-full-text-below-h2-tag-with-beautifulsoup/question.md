---
title: "Get full text below h2 tag with BeautifulSoup"
site: stackoverflow
question_id: 75204624
url: https://stackoverflow.com/q/75204624
asked: 2023-01-22T23:26:26Z
asked_by: "Iván Grzegorczyk"
asked_by_url: https://stackoverflow.com/users/21062528
last_edited: never
tags: [python, html, web-scraping, beautifulsoup, dataset]
score: 1
views_at_snapshot: 809
answer_count: 2
accepted_answer_id: 75204878
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 78d4ef8dedc14bf32dac3b58fc02f0cd1bf65c83cd87cdcde66bcb859217e098
---

# Get full text below h2 tag with BeautifulSoup

Asked by [Iván Grzegorczyk](https://stackoverflow.com/users/21062528) on Stack Overflow, <https://stackoverflow.com/q/75204624>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to obtain different character's descriptions and habilities for a dataset.
The problem I've encountered is that there seems to be a span tag within the h2 tag and in some cases a figure before de p tags. This is the format I'm facing:
```
<h2><span class="mw-headline" id="Apariencia">Apariencia</span></h2>
<figure class="thumb tleft " style="width: 100px"> 
<p>...</p>
<p>...</p>
<p>...</p>
<h2><span class="mw-headline" id="Personalidad">Personalidad</span></h2>
<p>...</p>
<p>...</p>
<p>...</p>
```
I need to obtain the text in those paragraphs. 

I have tried something like this but it obviously does not work.
```
import urllib.request
from bs4 import BeautifulSoup

fp = urllib.request.urlopen("https://jojo.fandom.com/es/wiki/Star_Platinum")
mybytes = fp.read()

html_doc = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(html_doc, 'html.parser')

spans = soup.find_all('span', {"class": "mw-headline"})
for s in spans:
    print(s.nextSibling.getText)
```
