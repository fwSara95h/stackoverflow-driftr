---
title: "Facebook Post Shares Scrapping"
site: stackoverflow
question_id: 73951098
answer_id: 73956514
url: https://stackoverflow.com/a/73956514
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-05T06:19:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73956514/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 79d812e304aaf142b92b7cae87d0611fe23e0813e1be2f97f51ce19c360cc1ce
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73956514>, 2022-10-05; score 0. Text as retrieved 2026-10-12.

As according to a comment on [this issue](https://github.com/kevinzg/facebook-scraper/issues/814), adding `'sharers': True` to the `options` parameter will have the generator include a list of sharers. 

However, when I tried it, the list had the names and profile URLs of the people who shared, but not the times at which the post was shared. If you ***really*** want the time, I suppose you could scrape each sharer and see the time for a post with a matching `shared_post_id`...

Another issue I noticed was that the sharers are also not included every time - sometimes some specific sharers are missing even though they were returned in a previous call, and sometimes there is only an empty list; but then, as the [documentation](https://pypi.org/project/facebook-scraper/) mentioned:

> There is no guarantee that every field will be extracted

It's still possible that you might get more consistent results, so it's definitely worth a try.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Brahim Darham](https://stackoverflow.com/users/20061848)** (2022-10-21): Yeah that is the problem I faced
