---
title: "How to get the text inside a tag using BeautifulSoup in Python"
site: stackoverflow
question_id: 74319795
url: https://stackoverflow.com/q/74319795
asked: 2022-11-04T15:59:27Z
asked_by: "yuttokb2"
asked_by_url: https://stackoverflow.com/users/19953142
last_edited: 2022-11-04T16:01:17Z
tags: [python, html, web-scraping, beautifulsoup]
score: -3
views_at_snapshot: 105
answer_count: 1
accepted_answer_id: 74334353
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9fc682a24f9c67596675b3267b9a259a4fe1c0d32400059bf8a0ff95e7f8abbf
---

# How to get the text inside a tag using BeautifulSoup in Python

Asked by [yuttokb2](https://stackoverflow.com/users/19953142) on Stack Overflow, <https://stackoverflow.com/q/74319795>, 2022-11-04, last edited 2022-11-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am stucked at scraping some content from a website where I need to retrieve from this html code all the text that are between 
```
<p class = some_string> Text I want to Retrieve </p>.
```
 
I need to use BeautifulSoup to retrieve all the text elements. The html code is attached below as a image:

[![enter image description here](https://i.sstatic.net/dhM3v.png)](https://i.sstatic.net/dhM3v.png)


As you can see there are many rows of the body that has text and I would like to get all that information. There is no table class or id for the body I am trying to scrape, so I can`t find the elements inside the table (as far as I know, but my knowledge of BS is pretty shallow so far, so if there are other ways around to tackle this problem I would appreciate a lot different approachment).

It is important to see that the class for each p element can change.

So far, the code I have tried to use to get this text to no avail is the following:



```

from bs4 import BeautifulSoup
import requests
link = 'http://agence-prd.ansm.sante.fr/php/ecodex/frames.php?specid=61350428&typedoc=R&ref=R0390743.htm'
req = requests.get(link)
soup = BeautifulSoup(req.content)
text_elements = soup.findAll('p')

for text_element in text_elements:

    text = text_element.text

    print(text)
```

Any suggestion on how to resolve this issue?

Thanks a lot in advance for the help!!!
