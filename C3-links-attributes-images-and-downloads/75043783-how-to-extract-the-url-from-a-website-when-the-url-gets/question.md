---
title: "How to extract the url from a website when the url gets abbreviated in the chrome console?"
site: stackoverflow
question_id: 75043783
url: https://stackoverflow.com/q/75043783
asked: 2023-01-07T21:06:18Z
asked_by: "almostbeautifulsoup"
asked_by_url: https://stackoverflow.com/users/20945348
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 51
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d4dc17e93cbb450eebb19cf5f37baa3126505d6e2a9aa9f718cfa970ec49efdd
---

# How to extract the url from a website when the url gets abbreviated in the chrome console?

Asked by [almostbeautifulsoup](https://stackoverflow.com/users/20945348) on Stack Overflow, <https://stackoverflow.com/q/75043783>, 2023-01-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

BeautifulSoup Python Question:

Hello all, webscraping beginner here! I am trying to extract the url of an element on a specific website. I click inspect, and it only shows the abbreviated version of the url on the Chrome inspect element area. If it's shorter, the link will show in full. When I click the url on the html on Chrome's inspect element area, it takes me to the desired link on Chrome.

When I try to extract it as an a.['href'] it only returns the abbreviated link. (Fake example: 'https://pizza.com/pepperonis/mozzarella/../onions'.)

You can see how the fake link above has those dots and it gives me an error when I  the   which doesn't work when I try to use it in my python program.
 
Anyone encountered this and can help?

I tried to use a f string and it didn't work to estimate what the string would be.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ronin](https://stackoverflow.com/users/2316519)** (2023-01-07): add simplified code that represent problem
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2023-01-07): Help us to help you - Please improve your question, so that we can reproduce your issue easily. Take a minute to check - How to create [mcve] Thanks
