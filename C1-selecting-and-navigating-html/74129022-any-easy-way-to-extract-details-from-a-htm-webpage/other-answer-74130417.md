---
title: "Any easy way to extract details from a HTM webpage?"
site: stackoverflow
question_id: 74129022
answer_id: 74130417
url: https://stackoverflow.com/a/74130417
author: "Andrew Hicks"
author_url: https://stackoverflow.com/users/13084623
posted: 2022-10-19T18:45:33Z
last_edited: 2022-10-19T20:03:23Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 24231d3ea839c226f5ae78f35f1b4f3814f2c9367365e9badf6dde446ebbbf52
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrew Hicks](https://stackoverflow.com/users/13084623) — 2022-10-19

Posted on Stack Overflow, <https://stackoverflow.com/a/74130417>, 2022-10-19, last edited 2022-10-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Unfortently, because I am running this on DataBricks, using Selenium isn't an immediate solution I can take. However, it does look like this method works!

    r = requests.get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber.replace("-", "")}/{accessionNumber}.txt', headers=headers)
    raw_10k = r.text
    city = raw_10k.split('Entity Address, City or Town</a></td>\n<td class="text">')[1].split('<span></span>')[0]
    print(city)
