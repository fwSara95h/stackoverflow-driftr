---
title: "Python/lxml/BeautifulSoup: using one text string to find another"
site: stackoverflow
question_id: 75538748
answer_id: 75564298
url: https://stackoverflow.com/a/75564298
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-25T08:53:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75564298/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 07e14bf24a56818dbbe87d18c4db3fff86e35169afc5774df96a3a75fae1cc7f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75564298>, 2023-02-25; score 0. Text as retrieved 2026-10-12.

<sub>[Note that you can shorten *`tag.string is not None and len(tag.get_text(strip=True)) > 0`* to <kbd>**`tag.string and tag.get_text(strip=True)`**</kbd> and expect pretty much the same results.]</sub>

If I test the HTML from your question,<sup>([view screenshot][1])</sup> it actually does return *`'WESTERN MAGNESIUM CORPORATION'`*; where's the snippet from? Is it from the actual source that your program is fetching? 

When I try getting [this field][2] from [this link](https://www.sec.gov/Archives/edgar/data/1801762/000149315221018835/form10-12g.htm), I have to normalize whitespace (*`' '.join(s.split())`* but you can also use regex and then you wouldn't need a lambda expression) because there is a line-break after the first word in the "label" after parsing. 

(And btw, I think with some versions you need to pass `text=` instead of `string=`, but I get a `DeprecationWarning` for `text`. Also, I only searched through `p` tags because with some versions of bs4, or with certain parsers, you might end up getting the commented text like *`Field: /Rule-Page`* instead of the name.)

```py
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

url='https://www.sec.gov/Archives/edgar/data/1801762/000149315221018835/form10-12g.htm'
resp = HTMLSession().get(url)
# print(resp.status_code, resp.reason, 'from', resp.url)
soup = BeautifulSoup(resp.content)

fieldLabel = '(Exact name of registrant as specified in its charter)'
try:
    fieldVal = soup.find(
        'p', string=lambda s: s and ' '.join(s.split())==fieldLabel
    ).find_previous(  'p', string=lambda s: s and s.strip()  ).string
except Exception as e:
    print('Error finding', fieldLabel, ':', repr(e))
    fieldVal = None
print(fieldVal)
```

prints 
> ```py
> WESTERN
> MAGNESIUM CORPORATION
> ```

  [1]: https://i.sstatic.net/kUgf7.png
  [2]: https://i.sstatic.net/k6ut4.png
