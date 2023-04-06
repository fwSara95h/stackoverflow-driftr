---
title: "requests.get Missing Schema Invalid URL error"
site: stackoverflow
question_id: 75934425
answer_id: 75951865
url: https://stackoverflow.com/a/75951865
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-06T16:42:05Z
last_edited: 2023-04-07T01:36:07Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75951865/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 66534128b6c956ffd4c6145504875532cae37ea532020ed7534a77278e328096
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75951865>, 2023-04-06, last edited 2023-04-07; **accepted**; score 0. Text as retrieved 2026-10-12.

> *"but i keep getting a Missing Schema error at the `data = requests.get(team_url)` line"*
> 
> <kbd>`MissingSchema: Invalid URL 'https//fbref.com/en/squads/18bb7c10/Arsenal-Stats': No scheme supplied. Perhaps you meant http://https//fbref.com/en/squads/18bb7c10/Arsenal-Stats?`</kbd>

As the error message explains, URLs should start with `https://` (or `http://`, just **NOT** `https//`, but they don't check that far), but you have in your code 

> ```py
>     team_urls = [f"https//fbref.com{I}" for I in links] # <-- ?TYPO? HERE
>     for team_url in team_urls:
> ```
> ```py
>         data = requests.get(team_url) # <-- error bc team_url has typo
> ```

It's probably just a typo, but you need to add the `:` in and change the line to 

```py
    team_urls = [f"https://fbref.com{I}" for I in links] 
```

and hopefully that will be enough to resolve this issue.
