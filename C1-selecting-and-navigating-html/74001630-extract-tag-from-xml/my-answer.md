---
title: "Extract Tag from XML"
site: stackoverflow
question_id: 74001630
answer_id: 74019286
url: https://stackoverflow.com/a/74019286
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-10T18:27:42Z
last_edited: 2022-10-10T18:31:18Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74019286/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ed64313258bf9d394cdf62e0cbc9ccc81c43af835c66cf5faaf3ef5cc217db6e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74019286>, 2022-10-10, last edited 2022-10-10; score 0. Text as retrieved 2026-10-12.

As you've already realized by now, you're getting the data as json, so doing something like:
```python
fact_sheet_links = [d['fact_sheet'] for d in Data.json()['data']]
```
would get you the data you want.

<br>

**But also**, if you'd prefer to work with the xml, you can add headers to the request:
```python
Data = requests.get(URL, headers={ 'Accept': 'application/xml' })
```
and get an xml response. When I did this, `Soup.find_all('fact_sheet')`  still did not work (although I've seen this method used in some tutorials, so it might be a version problem - and it *might* still work for you), but it *did* work when I used `find_all` [with lambda](https://stackoverflow.com/questions/49840504/using-lambda-functions-in-beautiful-soup):
```python 
tags = Soup.find_all(lambda t: 'fact_sheet' in t.name)
```
and the results after altering your code looked like [this][1]. That just gives you the tags though, so if you want a list of the contents instead, one way would be to use list comprehension:
```python
fact_sheet_links = [t.text for t in tags]
```
so that you get them like [this][2].


  [1]: https://i.sstatic.net/nSxi9.png
  [2]: https://i.sstatic.net/ft2f0.png
