---
title: "Print text of anchor link using BeautifulSoap library | python"
site: stackoverflow
question_id: 74213614
answer_id: 74214171
url: https://stackoverflow.com/a/74214171
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T21:00:56Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74214171/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 53e266f22d99060f561323d043378b6cf5afccd27dd325fb1743f2c2ebeba0bf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74214171>, 2022-10-26; score 1. Text as retrieved 2026-10-12.

You can extract the `a` tag using `select_one` with the [css selector](https://www.w3schools.com/cssref/css_selectors.php) `'span.engine-icon.year + p > a'` and then get the text using `get_text`.

For example, if you were looking at a car from [pakwheels.com](https://www.pakwheels.com/used-cars/suzuki-cultus-2018-for-sale-in-lahore-6596122) [the html in your screenshot looks like just like this site's], then
```python
r = requests.get('https://www.pakwheels.com/used-cars/suzuki-cultus-2018-for-sale-in-lahore-6596122')
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')

    hlYear = soup.select_one('span.engine-icon.year + p > a')
    if hlYear is not None:
        print(hlYear.get_text(strip=True))    
```
would print `2018`.
