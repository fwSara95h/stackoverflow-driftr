---
title: "Python/lxml/BeautifulSoup: using one text string to find another"
site: stackoverflow
question_id: 75538748
url: https://stackoverflow.com/q/75538748
asked: 2023-02-22T22:23:50Z
asked_by: "theactivist"
asked_by_url: https://stackoverflow.com/users/21268647
last_edited: 2023-02-22T22:25:55Z
tags: [python-3.x, beautifulsoup, lxml]
score: 0
views_at_snapshot: 52
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a88bb9b74ff2dade24a7f904d86850d59ad75a08296b5fde437d0ea4be77fcfd
---

# Python/lxml/BeautifulSoup: using one text string to find another

Asked by [theactivist](https://stackoverflow.com/users/21268647) on Stack Overflow, <https://stackoverflow.com/q/75538748>, 2023-02-22, last edited 2023-02-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm using Python's BeautifulSoup library with the lxml parsing engine to iterate through a bunch of docs on the SEC website (sec.gov). All of the docs contain the text string "(Name of Issuer)" beneath the actual name of the issuer, and I'm trying to use "(Name of Issuer)" to find and scrape the actual name of the issuer from each doc. Trouble is, the HTML/CSS is inconsistent from one doc to the next (sometimes the text is in a `<p>` tag, sometimes in a `<td>` tag, etc.). 

I'm trying to use the following try/except block:

```
try:
    issuer = soup.find(string="(Name of Issuer)").parent.find_previous(tag_has_text).string

except Exception as e:
    print(f"Error occurred while 'Name of Issuer' for url: {url}, error: {str(e)}")

    continue
```

to parse, for example, this HTML:

```
<P STYLE="font: 10pt Times New Roman, Times, Serif; margin-top: 0pt; margin-bottom: 0pt; text-align: center">WESTERN MAGNESIUM CORPORATION</P>

<P STYLE="font: 10pt Times New Roman, Times, Serif; margin-top: 0pt; margin-bottom: 0pt; text-align: center"></P>

<P STYLE="font: 10pt Times New Roman, Times, Serif; margin-top: 0pt; margin-bottom: 0pt; text-align: center"></P>

<!-- Field: Rule-Page --><DIV STYLE="margin-top: 0; margin-bottom: 0; width: 100%"><DIV STYLE="font-size: 1pt; border-top: Black 1.5pt solid">&nbsp;</DIV></DIV><!-- Field: /Rule-Page -->

<P STYLE="font: 10pt Times New Roman, Times, Serif; margin-top: 0pt; margin-bottom: 0pt; text-align: center"></P>

<P STYLE="font: 10pt Times New Roman, Times, Serif; margin-top: 0pt; margin-bottom: 0pt; text-align: center">(Name of Issuer)</P>
```

FYI, the "tag_has_text" argument calls a function that checks whether a tag contains text:

```
def tag_has_text(tag):
    return tag.string is not None and len(tag.get_text(strip=True)) > 0
```

I'm expecting to get, for example, `value = "WESTERN MAGNESIUM CORPORATION"`. Instead, I'm getting a lot of these errors: "Error occurred while 'Name of Issuer' for url: https://www.sec.gov/Archives/edgar/data/xxxx/xxxx/xxxx.htm, error: 'NoneType' object has no attribute 'parent'," which may indicate that it's not finding "(Name of Issuer)" or it's not finding a parent. Thanks in advance for suggestions.
