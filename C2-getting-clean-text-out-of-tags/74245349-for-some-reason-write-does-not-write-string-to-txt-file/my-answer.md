---
title: "For some reason .write() does not write string to .txt file anymore"
site: stackoverflow
question_id: 74245349
answer_id: 74245682
url: https://stackoverflow.com/a/74245682
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-29T13:25:34Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74245682/revisions
accepted: true
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bbd94d64200810519c72e9640a1d72ba1af250d495ac4aa0f0923d4741abac22
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74245682>, 2022-10-29; **accepted**; score 0. Text as retrieved 2026-10-12.

I can't reproduce this, but I've had inexplicable [to me at least] errors with file handling that were resolved when I wrote from inside a `with`.

[Just make sure to remove the lines involving `allurl` in your current code first just in case - or just try this with a different filename while checking if it works]

Since you're appending all the urls to `tested_links` anyway, you could just write it all at once after the while loop
```python
with open('all_urls.txt', 'w') as f:
    f.write('\n'.join('tested_links')+'\n')
```
or, if you have to write link by link, you can append by opening with `mode='a'`:
```python
# before the while, if you're not sure the file exists
# [and/or to clear previous data from file]
# with open('all_urls.txt', 'w') as f: f.write('')

                # and inside the try block: 
                with open('all_urls.txt', 'a') as f:                 
                    f.write(f'{link}\n')
```
