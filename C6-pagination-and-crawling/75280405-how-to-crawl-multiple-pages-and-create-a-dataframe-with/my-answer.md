---
title: "How to crawl multiple pages and create a dataframe with parsing?"
site: stackoverflow
question_id: 75280405
answer_id: 75283337
url: https://stackoverflow.com/a/75283337
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-30T10:48:36Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75283337/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cd1faf96af50046096348ec16a79a19479587c57d261b4816d61b2adaabc2c53
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75283337>, 2023-01-30; **accepted**; score 0. Text as retrieved 2026-10-12.

To expand on my comments, this should work:

```python
maxPage = 9
datePublished = []
headline = []
description =[]
urls = []

for page in range(1, maxPage+1):
    url = f"https://www.consilium.europa.eu/en/press/press-releases/?page={page}"
    res = requests.get(url)
    print(f'[page {page:>3}]', res.status_code, res.reason, 'from', res.url)
    soup = BeautifulSoup(res.content, 'lxml')

    soup_content = soup.find_all('li', {'class':['list-item ceu clearfix','list-item gsc clearfix','list-item euco clearfix','list-item eg clearfix' ]})
    for i in range(len(soup_content)):
        datePublished.append(soup_content[i].find('span', {'itemprop': 'datePublished'}).attrs['content'])
        headline.append(soup_content[i].find('h3', {'itemprop': 'headline'}).get_text().strip())
        description.append(soup_content[i].find('p', {'itemprop': 'description'}).get_text().strip())
        urls.append('https://www.consilium.europa.eu{}'.format(soup.find('a', {'itemprop': 'url'}).attrs['href']))
```

When I ran it, 179 unique rows were collected [20 rows from all pages except the 7th, which had 19].
