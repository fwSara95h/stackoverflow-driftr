---
title: "I want to extract article text and article title from list of URL's"
site: stackoverflow
question_id: 74136255
answer_id: 74147483
url: https://stackoverflow.com/a/74147483
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-21T00:10:37Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74147483/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ffda318a97f3e1642fe08513efb3bb925ecd64434a5c5738b661470c07387a97
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74147483>, 2022-10-21; score 0. Text as retrieved 2026-10-12.

You need to add some checks and error handling in your code. 

```python
for i in range(0,len(df)):
    j = df.iloc[i].values
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    page = requests.get(j[0],headers = headers)#loading text in url

    if page.status_code != 200 or not page.content:
        cMsg = '' if page.content else 'Empty content - '
        print(f'{cMsg}{page.status_code} {page.reason} - with url {j[0]}')
        break

    soup = BeautifulSoup(page.content,'html.parser')#parsing url text
    content = soup.findAll(attrs = {'class':'td-post-content'})#extracting only text part

    # empty content if not td-post-content found
    content = content[0].text if len(content) > 0 else '' 

    title = soup.findAll(attrs = {'class':'entry-title'})#extracting title of website
    #title = title[16].text
    print(content)
```

Before getting `soup`, this checks whether your request worked, and then for `content`, it only tries to get the text if `findAll` returned anything at all - otherwise it just sets as `''`; this avoids the index error.

If `findAll` *should* be returning something, you should set a `break` at this point as well and examine your `soup` and/or `page.content` - you might not be getting the html you are expecting. While blockers should trigger the `if page.status_code != 200` part, many sites require login, or require you to confirm some thing/s or render parts of the page dynamically with js, so that data would be missing from the request response...
