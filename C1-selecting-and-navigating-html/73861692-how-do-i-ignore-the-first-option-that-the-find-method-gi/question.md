---
title: "How do I ignore the first option that the find method gives me?"
site: stackoverflow
question_id: 73861692
url: https://stackoverflow.com/q/73861692
asked: 2022-09-27T02:16:02Z
asked_by: "Alf West"
asked_by_url: https://stackoverflow.com/users/19605137
last_edited: 2022-09-27T05:48:22Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 46
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 35df4a0e57a556d2e7338a092c5073953b795193ab0ae98946c4a22ab8e0d19c
---

# How do I ignore the first option that the find method gives me?

Asked by [Alf West](https://stackoverflow.com/users/19605137) on Stack Overflow, <https://stackoverflow.com/q/73861692>, 2022-09-27, last edited 2022-09-27 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have to scrape a page that records the date twice in a row with the same method. The first time it registers it only with the year, the second with the complete date.

I need how to scrape over the entire date, but the find method only shows me the first one (which doesn't interest me).

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/KxJrq.jpg

```
root_items = soup.find_all("div", class_="asset-full-content clearfix mb-5 no-title")

for root in root_items:
    response = root.find("input", class_="field form-control").get('value')
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-09-27): Help us to help you - Please improve your question, so that we can reproduce your issue easily. Provide foucsed HTML example as text not as image and take a minute to check - How to create [mcve] Thanks
