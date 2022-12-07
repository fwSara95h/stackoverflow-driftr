---
title: "Trying to isolate URL suffix's from list of href tags"
site: stackoverflow
question_id: 74723173
url: https://stackoverflow.com/q/74723173
asked: 2022-12-07T21:49:18Z
asked_by: "MrPigsWorth"
asked_by_url: https://stackoverflow.com/users/20717275
last_edited: 2022-12-07T21:50:22Z
tags: [python, list, beautifulsoup, web-crawler]
score: 0
views_at_snapshot: 54
answer_count: 1
accepted_answer_id: 74752087
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a1c1297905e7854c20ed46dadd47a1407443fe04a09f0edf0891723310eb000
---

# Trying to isolate URL suffix's from list of href tags

Asked by [MrPigsWorth](https://stackoverflow.com/users/20717275) on Stack Overflow, <https://stackoverflow.com/q/74723173>, 2022-12-07, last edited 2022-12-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm currently working on a simple web crawling program that will crawl the SCP wiki to find links to other articles in each article. So far I have been able to get a list of href tags that go to other articles, but can't navigate to them since the URL I need is embedded in the tag:

```
[ <a href="/scp-1512">SCP-1512</a>, 
<a href="/scp-2756">SCP-2756</a>, 
<a href="/scp-002">SCP-002</a>, 
<a href="/scp-004">SCP-004</a> ]
```

**Is there any way I would be able to isolate the "/scp-xxxx" from each item in the list so I can append it to the parent URL?**

The code used to get the list looks like this:

```
import requests
import lxml
from bs4 import BeautifulSoup
import re

def searchSCP(x):
    url = str(SCoutP(x))
    c = requests.get(url)
    crawl = BeautifulSoup(c.content, 'lxml')

    #Searches HTML for text containing "SCP-" and href tags containing "scp-"
    ref = crawl.find_all(text=re.compile("SCP-"), href=re.compile("scp-",))

    param = "SCP-" + str(SkateP(x)) #SkateP takes int and inserts an appropriate number of 0's.
    for i in ref: #Below function is for sorting out references to the article being searched
        if str(param) in i:
            ref.remove(i)

    if ref != []:
         print(ref)
```


The main idea I've tried to use is finding every item that contains items in quotations, but obviously that just returned the same list. What I want to be able to do is select a specific item in the list and take out ONLY the "scp-xxxx" part or, alternatively, change the initial code to only extract the href content in quotations to the list.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2022-12-07): You can do `find_all` to fetch all of the `"a"` tags, then pull the `href` attribute from that.
