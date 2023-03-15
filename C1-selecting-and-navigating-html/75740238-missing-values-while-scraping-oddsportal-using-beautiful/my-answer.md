---
title: "missing values while scraping Oddsportal using beautifulsoup"
site: stackoverflow
question_id: 75740238
answer_id: 75747651
url: https://stackoverflow.com/a/75747651
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-15T16:39:56Z
last_edited: 2023-03-15T16:53:29Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75747651/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ecfca2b9cee0cdf07a93af521bd9764ca13348e7fbb8c610953ae630e7bc916e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75747651>, 2023-03-15, last edited 2023-03-15; **accepted**; score 0. Text as retrieved 2026-10-12.

For `urls`, try using CSS selector as below:

```py
            # a_cont # <-- no longer necessary
            ac_sel = 'div:has(>a.active-item-calendar)' # a_cont selector
            a_sel = f'{ac_sel}>a[href]:not([href^="#"]):not(.active-item-calendar)'
            a_tags = soup.select(a_sel)
            urls = ['https://www.oddsportal.com'+a_tag['href'] for a_tag in a_tags]
```

---

And for the score, just change `evtSel['score']` selector to **`'a a[title]+div:has(+a[title])'`**; but note that the `score` field will now contain `–` instead of `None`/`nan` for future games...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PyNoob](https://stackoverflow.com/users/14833958)** (2023-03-16): Thanks for this. Also, is there any way you can 'teach me' the scraping? I am unable to get it. Any other platform would do. I am ready to share my credentials if thats alright with you for that.
- **me** (2023-03-20): @PyNoob It's mostly just getting familiar [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) (and [soupsieve](https://facelessuser.github.io/soupsieve/selectors/) which [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) uses to search) and a lot of practice with the inspect tab. I'm not really very good at explaining things outside of an example, but I could take you step by step for the selectors used in this solution [and/or for scraping another site, if you prefer]. Do you use discord?
