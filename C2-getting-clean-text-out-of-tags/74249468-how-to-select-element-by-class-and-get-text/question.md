---
title: "How to select element by class and get text?"
site: stackoverflow
question_id: 74249468
url: https://stackoverflow.com/q/74249468
asked: 2022-10-29T23:05:46Z
asked_by: "Ömer Sevban Tümer"
asked_by_url: https://stackoverflow.com/users/20368508
last_edited: 2022-10-30T07:30:24Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 106
answer_count: 1
accepted_answer_id: 74251254
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2fe6913e4cf5f07e6349bc2ae22e0f41c2f403c0f1f2950366e846ece09f742a
---

# How to select element by class and get text?

Asked by [Ömer Sevban Tümer](https://stackoverflow.com/users/20368508) on Stack Overflow, <https://stackoverflow.com/q/74249468>, 2022-10-29, last edited 2022-10-30 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have been trying to scrape addresses in this page: https://www.worldometers.info/coronavirus/#news

How can I get values which under `class=sorting_1`? It is difficult for me. I'm completely new to `Beautifulsoup`.

![1]


  [1]: https://i.sstatic.net/I0g8Y.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[αԋɱҽԃ αмєяιcαη](https://stackoverflow.com/users/7658985)** (2022-10-29): `soup.select_one(".sorting_1").text`
- **[EvensF](https://stackoverflow.com/users/2387806)** (2022-10-30): Can you show us what you tried? And instead of linking to an image of some text, can you copy that text in your question description?
