---
title: "Adding +1 to a URL whilst scraping"
site: stackoverflow
question_id: 74343136
url: https://stackoverflow.com/q/74343136
asked: 2022-11-07T07:19:00Z
asked_by: "user19476773"
asked_by_url: (account no longer exists)
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 79
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e53ad36e1fca05f24ac78dcfde11bcedbf5443131f786045323ef0661354c282
---

# Adding +1 to a URL whilst scraping

Asked by user19476773 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/74343136>, 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

If I have a url called youtube.com/user/1/ and I want the number to incrament to youtube.com/user/2/
whilst scraping the whole page, how would I do so? I've been trying to think of some ways to do this but I can't seem to find anything?

BeautifulSoup

It should work like this:
youtube.com/user/1/
You scrape the page and then it moves to
youtube.com/user/2/

If you could find the solution in beautiful soup that would be cool :)
etc.
