---
title: "BeautifulSoup parsed HTML: strange NBSP string, how to get rid of them?"
site: stackoverflow
question_id: 76855339
answer_id: 76867902
url: https://stackoverflow.com/a/76867902
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-08-09T12:42:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76867902/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0be25fc08e72da8522349133026df4b71b22335b30155435abbd70c08129148a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-08-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76867902>, 2023-08-09; **accepted**; score 1. Text as retrieved 2026-10-12.

From the question itself:

> **EDIT ANSWER FOUND**
>
> I tried Claude and it gave me the right answer. I post here below, hopefully it is useful for others. 
>
> In short, these 'NBSP' (I also had ZWNJ in another) are unicode characters that show up as white spaces after parsing HTML. The are NOT html entities so soup does not parse them. One reason these appear in your HTML is possibly the authors copied content from Word and inherited whitespaces - obviously that is not good practice.
>
> To get rid of such content, do 
>
>     import string
>     text = tagobject.getText() #'tagobject' is whichever soup tag object you want to process    
>     text=''.join(filter(lambda x: x in string.printable, text))
>
> Alternatively, if you know the unicode for the character you want to rid of, you can use `text.replace(u'\xa0', ' ')`
