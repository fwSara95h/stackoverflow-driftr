---
title: "Adding +1 to a URL whilst scraping"
site: stackoverflow
question_id: 74343136
answer_id: 74343168
url: https://stackoverflow.com/a/74343168
author: "Coollector"
author_url: https://stackoverflow.com/users/18623283
posted: 2022-11-07T07:22:45Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c3b333f9e01e0eda460637c88a684c3230561e9ceff33211e825a5511181931a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Coollector](https://stackoverflow.com/users/18623283) — 2022-11-07

Posted on Stack Overflow, <https://stackoverflow.com/a/74343168>, 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

    while scraping:
        for i in range(amount_of_scrapes):
            scrape(f"youtube.com/user/{i+1}/")
        scraping = False


This is just an example but correct implemented it should work

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user19476773 (account no longer exists)** (2022-11-07): Thank you so much for your answer. Would anyone else like to expand on this?
