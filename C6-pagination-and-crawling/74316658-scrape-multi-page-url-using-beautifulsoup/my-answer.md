---
title: "Scrape multi page URL using Beautifulsoup"
site: stackoverflow
question_id: 74316658
answer_id: 74334463
url: https://stackoverflow.com/a/74334463
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T09:00:12Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74334463/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9208f3886cf07f9a3aedfee8a681b5b9fbd05059f1ce0bfcb4da6f141f70ccd3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74334463>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

You can use a while loop to go through all the pages
```python
# import urllib.parse

url = "https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p=1&selectedItem=viewAllAwardedContracts.do&T01_ps=100"

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

i = 0 
while url:
    html = session.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    
    #######  EXTRACT AND SAVE THE DATA YOU WANT  #######

    nxtBtn = soup.select_one('button.SearchBtn[title="Next"][href]')
    if nxtBtn:
        url = urllib.parse.urljoin(url, nxtBtn.get('href'))
        print('going to next page', url)
    else: url = None
```
`nxtBtn` gets the tag for the button that takes the user to the next page; as long as that can be found, the `href` is extracted from the tag to update `url` and continue to the next iteration - once it can't be found, `url` is set to `None` so that the `while` condition is no longer upheld and the loop terminates.
