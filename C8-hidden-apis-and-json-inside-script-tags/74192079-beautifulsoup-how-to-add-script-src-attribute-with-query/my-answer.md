---
title: "BeautifulSoup: How to add script src attribute with querystring without encoding the url?"
site: stackoverflow
question_id: 74192079
answer_id: 74196605
url: https://stackoverflow.com/a/74196605
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-25T15:32:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74196605/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b582db76c43cc1330a4ea1d881cdaff38519f858959d6246f27d336b02cfbd73
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74196605>, 2022-10-25; **accepted**; score 0. Text as retrieved 2026-10-12.

This is not actually a problem - this is valid html. Both `jsmanager.get('src')` and `jsmanager.attrs['src']` will give the same link as you set, and `jsmanager.prettify(formatter=None)` will also show the tag without encoding the ampersand [the '&' character]. 

If you add to a html
```HTML
<script src="https://example.com/myscript.js?data=test&amp;alarm=1"></script>
```
it should behave as intended. In fact, if you render 
```HTML
<a href="https://example.com/myscript.js?data=test&amp;alarm=1"></a>
```
and right-click on the link and then *Copy link address* you will be able to paste the link with the original `&` instead of `&amp;`.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Daniel Vygolov](https://stackoverflow.com/users/1194200)** (2022-11-02): Ok, got it, thank you. But is it possible to add querystring to a link without encoding? Or it can't be done anyway.
- **me** (2022-11-02): @DanielVygolov [just to be clear, the actual link's querystring - as in what gets entered in the address bar of a browser - should have `&` not `&amp;`.] If you're writing your own html manually and you add without encoding, it will still work, but bs4 is more "strict" with itself, so it will always automatically encode [and afaik there's no way to override that]
