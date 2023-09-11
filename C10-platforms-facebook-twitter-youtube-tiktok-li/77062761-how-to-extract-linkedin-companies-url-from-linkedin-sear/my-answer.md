---
title: "How to extract linkedin companies URL from linkedin search using python"
site: stackoverflow
question_id: 77062761
answer_id: 77084197
url: https://stackoverflow.com/a/77084197
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-11T19:02:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77084197/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6c0bf5091206ab2bff34c0898945863121def15822e5819ebc642b75aa789f97
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77084197>, 2023-09-11; score 0. Text as retrieved 2026-10-12.

I think the main issue here might be that `driver.implicitly_wait(5)` inside the *`for keyword in keywords:`* block isn't enough and you need to use some kind of [explicit wait](https://selenium-python.readthedocs.io/waits.html#explicit-waits) instead. For example, I tried with simply `time.sleep(5)` as below:

```py
for keyword in ['Meta', 'IBM']:
    URL = 'https://www.linkedin.com/search/results/companies/?keywords=' + keyword
    driver.get(url=URL)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    a_href = soup.select('span.entity-result__title-text a.app-aware-link')
    if a_href:
        link = a_href[0].get('href')
        print(f"Keyword: {keyword}, linkedin: {link}")
    else:
        print(f"Keyword: {keyword}, linkedin: Not found")
```

and that printed 

```lang-none
Keyword: Meta, linkedin: https://www.linkedin.com/company/meta/
Keyword: IBM, linkedin: https://www.linkedin.com/company/ibm/
```

Note that I removed the csv parts to focus on the search issue, and also, I used chrome instead of edge. Also, I changed how `a_href` is searched for by using [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) because the *`.find_all('a', {'class':'app-aware-link '})`* will always give you `href="https://www.linkedin.com/feed/?nis=true"` instead of the first search result.
