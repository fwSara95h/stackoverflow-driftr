---
title: "beautifulsoup - how to get data from within self closing tag"
site: stackoverflow
question_id: 75050816
url: https://stackoverflow.com/q/75050816
asked: 2023-01-08T19:52:17Z
asked_by: "BenKen10"
asked_by_url: https://stackoverflow.com/users/15878316
last_edited: never
tags: [python, python-3.x, beautifulsoup]
score: 1
views_at_snapshot: 113
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f270e81451ed7b1f78ba963918bf6c3871146a9d794cc6090d16db327265dac7
---

# beautifulsoup - how to get data from within self closing tag

Asked by [BenKen10](https://stackoverflow.com/users/15878316) on Stack Overflow, <https://stackoverflow.com/q/75050816>, 2023-01-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to use beautifulsoup to retain the value "XXXXX" in the self closing html tag below (apologies if my terminology is incorrect)

Is this possible? All the questions I can find are around getting data out that is between div tags, rather than an attribute in a self closing tag.

`<input name="nonce" type="hidden" value="XXXXX"/>`

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-08): `soup.select_one('input[name="nonce"]')['value']` ?
