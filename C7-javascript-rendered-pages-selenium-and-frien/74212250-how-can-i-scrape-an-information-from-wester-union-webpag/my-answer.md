---
title: "How can I scrape an information from Wester Union webpage?"
site: stackoverflow
question_id: 74212250
answer_id: 74216513
url: https://stackoverflow.com/a/74216513
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-27T03:35:03Z
last_edited: 2022-10-27T03:52:02Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74216513/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [curlconverter request, linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: de59a5510f723e5849342081a6775a518ecb5df38ea49d7a9e6ae50e4b3ea1a6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74216513>, 2022-10-27, last edited 2022-10-27; score 0. Text as retrieved 2026-10-12.

WU loads that bit with javascript, all you're scraping with requests is a loading page full of placeholders
[![screenshot][1]][1]

The [POST request][2] they seem to be using to populate that field looks very difficult to replicate (see [this code](https://gist.github.com/Driftr95/25f57259086fabce6f929974c6f2f7c6) which I copied from [curlconverter](https://curlconverter.com/))

<hr>

You might consider using [selenium](https://medium.com/featurepreneur/an-introduction-to-web-automation-using-selenium-python-2ad84814b11c). I have [a function](https://gist.github.com/Driftr95/cbae6710c134df708f44ade8503f6638) for cases like this; if you copy it to your code, you can simply call it
```python
soup = linkToSoup_selenium(url, tmout='3')
# YOU MIGHT NEED TO ADJUST tmout - it sets the wait time for loading
# (3sec seems to be more that enough for me, but it can vary)

if soup is not None: 
    convSpan = soup.select_one('span#smoExchangeRate')
    if convSpan is not None:
        print(convSpan.get_text(strip=True))

# output:
# 1.00 BRL = 56.5617Argentine Peso(ARS)
```

[Yes, the conversion in the printed line is to Pesos - when I manually open the link in your code, I see the same thing; I believe you have to set set [ReceiveCountry=GB&ISOCurrency=GBP](https://www.westernunion.com/br/pt/web/send-money/start?ReceiveCountry=GB&ISOCurrency=GBP&SendAmount=100.00&FundsOut=BA&FundsIn=WUPay) in the link to get `1.00 BRL = 0.1576British Pound(GBP)` as output.] 


  [1]: https://i.sstatic.net/mZ8Wj.png
  [2]: https://i.sstatic.net/aYIJ2.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Vinícius](https://stackoverflow.com/users/11453261)** (2022-10-27): Amazing!! Really amazing!! Thank you for your big help. It worked nicely.
