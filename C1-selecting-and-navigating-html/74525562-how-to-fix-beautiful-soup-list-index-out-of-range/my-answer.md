---
title: "How to fix beautiful soup list index out of range"
site: stackoverflow
question_id: 74525562
answer_id: 74570856
url: https://stackoverflow.com/a/74570856
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-25T09:45:40Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74570856/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [extractAttr]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 911e724e3cf31b0e514244d440151e32ac19ad7eee4c31a7c284dd7a707f9a72
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74570856>, 2022-11-25; score 0. Text as retrieved 2026-10-12.

Generally, it's safer to check that `select`/`find` returns something before applying `.get...`. When you have to select-and-get from multiple elements, it's more convenient to use a function on loop.

<sub>[This is a simplified version of another function I often use when scraping; if interested, [see an example with the full version](https://pastebin.com/SGQN5pYd).]</sub>
```python
def extractAttr(tag, sel, attr='', defVal=None):
    s = tag.select_one(sel)
    if s is None: return defVal
    if attr == '': 
        stxt = s.get_text(' ').strip()
        return stxt if stxt else defVal
    return s.get(attr, defVal)
```
then you just need to create a reference list with selectors for all the information you need:
```python
selRef = [ # key, selector, attribute, default
    ('Title', '.jobTitle', '', '?'),
    ('Company', '.companyName', '', '?'),
    ('Location', '.companyLocation', '', '?'),
    ('Rating', '.ratingNumber', '', 'NaN'),
    ('Date', '.date', '', 'NaN'),
    ('Salary', '.salary-snippet-container', '', 'NaN'),
    ('Description', '.job-snippet', '', ''),
    ('Links', 'a[href]', 'href', None)
] # be careful to have exactly 4 items in each tuple
```
and you can just simplify your loop to
```python
    for job in jobs:
        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser') 
        jn += 1

        jDict = {k: extractAttr(soup, s, a, d) for k, s, a, d in selRef}
        dataframe = pd.concat([dataframe, pd.DataFrame([jDict])])
        print("Job number {0:4d} added - {1:s}".format(jn, jDict['Title']))
```
