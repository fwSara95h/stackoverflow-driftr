---
title: "Writing csv file - Python-3.x web-scrapping"
site: stackoverflow
question_id: 73858513
answer_id: 73862860
url: https://stackoverflow.com/a/73862860
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-27T05:43:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73862860/revisions
accepted: false
score: 0
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 58aa8a0325eaf80188b23f13632a79e079cbed76c6a9fdcaf97169885466e441
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73862860>, 2022-09-27; score 0. Text as retrieved 2026-10-12.

You can either just [`strip`][3] them right after scraping, or [if you need to deal with it in list form for some reason], you can use a function like this:

    def stripList(l: list, fromEnd='both'): 
      lInd = range(len(l))
      if fromEnd == 'right': 
        lInd = reversed(lInd) 
      for i in lInd:
        if str(l[i]).strip() != '':
          if fromEnd not in ['left', 'right']:
            return stripList(l[i:], 'right')
          return l[i:] if fromEnd == 'left' else l[:i+1] 
      return []
You can call it [like this][1].

If you don't actually want to keep the lists, but that's how you're receiving the data, you can use [`''.join()`][2].


  [1]: https://i.sstatic.net/gDzjl.png
  [2]: https://www.programiz.com/python-programming/methods/string/join
  [3]: https://www.programiz.com/python-programming/methods/string/strip
