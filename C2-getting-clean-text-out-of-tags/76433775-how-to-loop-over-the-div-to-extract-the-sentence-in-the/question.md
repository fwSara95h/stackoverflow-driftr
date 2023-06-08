---
title: "How to loop over the div to extract the sentence in the paragraph from a webpage?"
site: stackoverflow
question_id: 76433775
url: https://stackoverflow.com/q/76433775
asked: 2023-06-08T16:04:50Z
asked_by: "LaurenLai"
asked_by_url: https://stackoverflow.com/users/19086016
last_edited: 2023-06-09T19:10:37Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, html, web-scraping, beautifulsoup, nlp]
score: 0
views_at_snapshot: 107
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6f10c0af5ea0a9f0c8c57ea117046fa887e68ef06782f460b01da39cfaadf357
---

# How to loop over the div to extract the sentence in the paragraph from a webpage?

Asked by [LaurenLai](https://stackoverflow.com/users/19086016) on Stack Overflow, <https://stackoverflow.com/q/76433775>, 2023-06-08, last edited 2023-06-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am practicing web scraping to extract comments (which is highlighted by red line) from a post in reddit using BeautifulSoup.
[HTML code](https://i.sstatic.net/vXwjL.png)
Initially when I ran

```
for a in soup.findAll('div', {'class': 'py-0 xs:ml-xs inline-block max-w-full'}):
  print(a.find('p').text)
```

it runs without error but no outputs were shown. Then I tried

```
every_review = soup.findAll('shreddit-comment-tree', {'id':'comment-tree'})
for rev in every_review.find('div', {'class':'md pl-[28px] xs:pl-xl text-14'}):
  for d in rev.find('div', {'id':'-post-rtjson-content'}):
    print(d.find('p').text)
```

It started to show error as below:

```
AttributeError: ResultSet object has no attribute 'find'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```

Does any professional have any idea how to solve this issue? And I wonder why it showed no output on my first run?

The output should be a list containing all sentences like *`[sent1, sent2, sent3...]`*

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Campbell](https://stackoverflow.com/users/8890114)** (2023-06-08): findAll returns a list, try replacing `soup.findAll` in your first line with `soup.find` (this should work since there is only one shreddit-comment-tree in your HTML).  If there are multiple shreddit-comment-trees, you will need to put another for loop in to iterate over the list.
