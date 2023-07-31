---
title: "Unable to find anchor tag for href link on goolge search page"
site: stackoverflow
question_id: 76800098
answer_id: 76803168
url: https://stackoverflow.com/a/76803168
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-07-31T11:25:54Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76803168/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c2575394a708542164d2e4f85ff295b3e108e9948cbe2f2d7e061d920dd51ee0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-07-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76803168>, 2023-07-31; **accepted**; score 0. Text as retrieved 2026-10-12.

The `q=SALT-2000.6` search does not contain a result with `https://www.sundownaudio.com`, just `https://sundownaudio.com` (note that the `www` is missing), so you need to account for that in your pattern.

[![ss][1]][1]


Maybe just search for `sundownaudio.com`?

  [1]: https://i.sstatic.net/AmbL6.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Cryptic ](https://stackoverflow.com/users/8656115)** (2023-08-01): OMG, i just cannot believe I spent  hours for this stupid mistake and all this time I thought my code is wrong. I just picked up on python after like a year so I doubt myself !  Thanks a lot ! Btw, I am trying to gauge my scripting skills so if you do not mind how do you see this script
- **me** (2023-08-01): @Cryptic happy to help! I can't really comment on your code structure since my own isn't very clean, but it works, and is not too hard to debug, so that has to be some kind of good (right?); on a very small and rather pedantic note: you don't need to check *`if "&sa" in href:`* before `href = href.split("&sa")[0]` since `.split` will return an array of length 1 even if the parameter isn't there in the main string
