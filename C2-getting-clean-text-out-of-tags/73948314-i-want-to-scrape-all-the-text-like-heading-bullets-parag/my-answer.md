---
title: "I want to scrape all the text like heading, bullets paragraph from article acept some <p> tags from start of the article and from end of the article"
site: stackoverflow
question_id: 73948314
answer_id: 73952457
url: https://stackoverflow.com/a/73952457
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-04T18:57:38Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73952457/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b5a965a512b9c83849ccffa6a8c5aa8ad27af29b620e3b44c836bab223f4ffcb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73952457>, 2022-10-04; **accepted**; score 1. Text as retrieved 2026-10-12.

You could filter within the list comprehension and then find where to slice of the unwanted parts at the end:

    for items in soup.select('article.article'):
    tags = [
          t for t in items.find_all(["h6","h5","h4","h3","h2","h1","p","li"]) 
          if not (t.name in ['p', 'li'] and (
              ('class' in t.attrs and t.attrs['class']) or
              ('id' in t.attrs and t.attrs['id'])
          ))
      ] # filtered out "Share..." and "Last Updated..."
      tLen = len(tags)
      for i in list(range(tLen))[::-1]: #counting down from last tag
        if tags[i].name == 'h3': 
          tags = tags[:i]
          break
      
      articleText = '\n'.join([t.text for t in tags])
      print(articleText)

with that, you'll be able to get rid of [the paragraph with the list of links][1] for further reading. If you want up to just before the *"↓ Join the community ↓"* part like in your code, just change to  `if tags[i].name == 'h5':` instead of `h3`, and if you want all the way to the end only skipping [the "subscribe..." section][2] , you'd just need to change that `if` block to

    if tags[i].name == 'h5':
        tags = tags[:i] + tags[i+1:]
        break

  [1]: https://i.sstatic.net/M3wkj.png
  [2]: https://i.sstatic.net/gqTVm.png
