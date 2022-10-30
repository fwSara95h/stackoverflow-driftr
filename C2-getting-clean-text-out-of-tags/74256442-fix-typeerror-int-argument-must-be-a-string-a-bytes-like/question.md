---
title: "Fix TypeError: int() argument must be a string, a bytes-like object or a number, not 'Response'"
site: stackoverflow
question_id: 74256442
url: https://stackoverflow.com/q/74256442
asked: 2022-10-30T20:15:11Z
asked_by: "user15316630"
asked_by_url: https://stackoverflow.com/users/15316630
last_edited: never
tags: [python, web-scraping, beautifulsoup, global-variables, typeerror]
score: 0
views_at_snapshot: 1209
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 00e19e49ab839b6ce8a6734238b994437996a1e17adfd8dded5ba5e73b3f5b05
---

# Fix TypeError: int() argument must be a string, a bytes-like object or a number, not 'Response'

Asked by [user15316630](https://stackoverflow.com/users/15316630) on Stack Overflow, <https://stackoverflow.com/q/74256442>, 2022-10-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Trying to scrap text from different pages using a while loop.
but getting 
TypeError: int() argument must be a string, a bytes-like object or a number, not 'Response'

I am using beautiful soup and global variable to increase the page number.


```
import re
from bs4 import BeautifulSoup , Comment
import requests

page = 1
total = 3
def get_chapter():
    global page
    c_page = int(page)
    if c_page < 10:
        chapter = f"0{page}"
    else:
        chapter = page
    page += 1
    return chapter


def filter_text(element):
if element.parent.name in ['style' , 'script' , 'head' , 'title' , 'meta' , '[document]']:
return False
if isinstance(element , Comment):
return False
elif re.match(r"[\s\r\n]+" , str(element)):
return False
return True


def run():
    global page
    c_page = int(page)
    while c_page < total:
        chapter = get_chapter()
        # book url altered
        url = f"https://wod.ng/wol/d/r1/lp-e/11020212{chapter}"
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # get text only
        texts = soup.find_all(text=True)
        visible_texts = filter(filter_text, texts)
        print(u" ".join(t.strip() for t in visible_texts))

run()
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MattDMo](https://stackoverflow.com/users/1426065)** (2022-10-30): Please fix your indentation.
- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2022-10-30): Did you not notice `page = requests.get(url)`?  This is why it is such a bad practice to use global variables.  Part of your code thinks `page` is an integer page number, and part of it thinks `page` is the returned HTML page, and they are stepping on each other.  The short term answer is to use a different variable for your `request.get(url)` response.
- **[juanpa.arrivillaga](https://stackoverflow.com/users/5014455)** (2022-10-30): post the full error message including the stack trace, the Pyhton runtime goes to great lengths to create that error message with lots of helpful information, why would you just *omit it* from your question?
- **[tdelaney](https://stackoverflow.com/users/642070)** (2022-10-30): When you get an error like this, it means a variable didn't hold the value you think it should. So, go back to the places its assigned (especially the _last_ place its assigned). That's where the problem is.
