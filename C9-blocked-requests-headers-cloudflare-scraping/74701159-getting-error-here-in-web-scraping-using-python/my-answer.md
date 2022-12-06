---
title: "Getting Error here in web scraping using python"
site: stackoverflow
question_id: 74701159
answer_id: 74709035
url: https://stackoverflow.com/a/74709035
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-06T21:06:19Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74709035/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [error logger]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 741c77c701c6bac85207873fc57d90164f6ac495a814297216c0f88916abca9a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74709035>, 2022-12-06; score 0. Text as retrieved 2026-10-12.

> not able to understand why??? 

It looks like the html in `page` does not contain any tags with `td-post-content` class, so the `content` returned in line 10 is an empty ResultSet (something like `[]`), which is why the `content[0]` part of line 11 raises an `IndexError`. You can simply skip URLs that don't have this class in the fetched html:

```python
   content=soup.findAll(attrs={'class':'td-post-content'})#extracting only text part
   if not content: 
      print('NO .td-post-content CONTENT FROM', j[0])
      continue ## <--- SKIP REST OF LOOP TO NEXT URL'S LOOP
   content=content[0].text.replace('\xa0',"  ").replace('\n',"  ")#replace end line symbol with space 
```

---

If you want to keep track of pages that were skipped, you can use something like [this error logger](https://pastebin.com/cxGH50Mc) instead of just printing

```python
## ADD TO THE BEGINNING OF YOUR CODE:
# import os
# def logError_scrapes... ## PASTE FUNCTION DEFINITION FROM https://pastebin.com/cxGH50Mc

## INSIDE THE LOOP:
   if not content:
      # print('NO .td-post-content CONTENT FROM', j[0])
      logError_scrapes(
           logId=f'row_{i}-url_{url_id}', url=j[0], req=page
         , msg='No .td-post-content in fetched html'
         # , conf={'saveHtml': True} # to save html to file (instead of csv column)

         # if you want to save prettified html in csv column:
         # , rSoup=soup , conf={'saveHtml': True, 'minify': False} 
      )
      continue ## <--- SKIP REST OF LOOP TO NEXT URL'S LOOP
```
(By default, the error log gets saved to "scrape_fails.csv", but you can modify this default in the function or specify another file path through the `conf` argument [with key `'errLogFp'`].)

The logfile contents look something like [![samplop][1]][1]

If `reqStatus` doesn't have `200 OK`, that means something went wrong with `requests.get` [in line 8 of your code]; you can decide what to do next based on the [response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) [like, for 403 you might need better headers, with 503 you might just need to try again later, etc]. 

However, if it *is* `200 OK` then that might mean that the fetched html is just different from what you were expecting. In that case, you should open the html file in a code editor [if you didn't use the `saveHtml` option, copy the html from the last column (`htmlString`) to a .html file]; then you can see what the html looks like and whether the data you want is in a different format from expected, or missing entirely...

---

Btw, there is another line in your code with potential for index error 

```python
   title=title[16].text.replace('\n',"  ").replace('/',"")
```

You could do the same for that line - precede it with `if not title[16:]....continue` (with `msg='page does not have .entry-title[16]'` if you're logging).

(You could also wrap everything in the loop in a `try` block and log error in the `except` block....)


  [1]: https://i.sstatic.net/TfgkO.png
