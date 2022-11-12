---
title: "Scrape webpage element with text or href criteria simultaneously"
site: stackoverflow
question_id: 74410699
url: https://stackoverflow.com/q/74410699
asked: 2022-11-12T05:54:38Z
asked_by: "randomrandom123"
asked_by_url: https://stackoverflow.com/users/19686176
last_edited: 2022-11-12T21:47:11Z
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 47
answer_count: 1
accepted_answer_id: 74417369
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e98b22ea4702259a1871337985d1970c5b77231f47cef93a365e89d12fc27e39
---

# Scrape webpage element with text or href criteria simultaneously

Asked by [randomrandom123](https://stackoverflow.com/users/19686176) on Stack Overflow, <https://stackoverflow.com/q/74410699>, 2022-11-12, last edited 2022-11-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

In the code below I can either write a function to pass to `soup.find_all` to search for regular expressions in the text or search with `href` keyword inside the reference. 


```
from bs4 import BeautifulSoup
import re


# s is an example string. Scraping a webpage in reality.
s = """<tr>
            <td><a href="/-/media/markets-ops/rpm/rpm-auction-info/2023-2024/2023-2024-base-residual-auction-report.ashx" target="_blank">Report&nbsp;<i class="new-pdf">PDF</i></a> | <a href="/-/media/markets-ops/rpm/rpm-auction-info/2023-2024/2023-2024-base-residual-auction-results.ashx" target="_blank">Results&nbsp;<i class="new-xls">XLS</i></a>&nbsp;</td>
            <td style="text-align: right;">6.21.2022</td>
        </tr>
        
    <tr>
            <td><strong>3rd Incremental Auction</strong><br>
            <a href="/-/media/markets-ops/rpm/rpm-auction-info/2021-2022/2021-2022-third-incremental-auction-report.ashx" target="_blank">Report&nbsp;<i class="new-pdf">PDF</i></a>&nbsp;| <a href="/-/media/markets-ops/rpm/rpm-auction-info/2021-2022/2021-2022-third-incremental-auction-results.ashx" target="_blank">Results&nbsp;<i class="new-xls">XLS</i></a><br>
            <a href="/-/media/markets-ops/rpm/rpm-auction-info/2021-2022/2021-2022-third-incremental-auction-pre-auction-credit-calculator.ashx" target="_blank">Capacity Performance Pre-Auction Credit Calculator&nbsp;<i class="new-xls">XLS</i></a><br>
            <a href="/-/media/markets-ops/rpm/rpm-auction-info/2021-2022/2021-2022-third-ia-planning-parameters.ashx" target="_blank">Planning Parameters&nbsp;<i class="new-xls">XLS</i></a></td>
            <td style="text-align: right;"><br>
            3.5.2021<br>
            2.1.2021<br>
            <br>
            3.9.2021</td>
        </tr>"""


soup = BeautifulSoup(s, 'html.parser')

# 1) href search
gr = 'base-residual'
soup.find_all(href = re.compile(gr, re.IGNORECASE | re.DOTALL))

# 2) function search, this doesn't look inside the href  

def find_auction_results(tag):

    return tag.name == "tr" and bool(re.search("3rd Incremental Auction", tag.text, re.IGNORECASE | re.DOTALL))

soup.find_all(find_auction_results)

```

How can I do both in the same call, or in two different calls but with a single joined output? With the latter I can simply use `list.extend()` but what if there is an overlap? How would I in that case return a non-overlapping entity to process further? Can I search for a regular expression both in the text and in href simultaneously?


Expect: unique non-overlapping soup list.
Get: two different calls.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-11-12): which tag do you want? the `a` tag? or the `tr` tag wrapping the `a` tag?
- **me** (2022-11-12): you can do what ever you want in the `find_auction_results`...you don't have to return in one statement - you can check everything [tag name, href, text, parents, children, etc], and set the value of a return variable and then return that
- **me** (2022-11-12): Also, try `soup.select('*[href*="base-residual"], tr:-soup-contains("3rd Incremental Auction")')` [ you might need to use [`html5lib`](https://pypi.org/project/html5lib/) instead of `html.parser` though]. Is that the kind of results you're looking for?
- **[randomrandom123](https://stackoverflow.com/users/19686176)** (2022-11-12): @Driftr95 How to get a unique list (the type that `find_all` returns) that would have all the  `tr` elements either have subpart with a function search of the element text OR hase href containing certain substring?
- **me** (2022-11-12): [`select` can do most of that; afaik it can't handle regex (beyond *starts-with*, *ends-with* and *contains*), and I'm pretty sure it's case sensitive.] I feel like you're not realizing just how much you can do inside `find_auction_results` (although ofc, the more you do, the slower it will get) - please see my answer. I'm curious about which approach you might find useful
