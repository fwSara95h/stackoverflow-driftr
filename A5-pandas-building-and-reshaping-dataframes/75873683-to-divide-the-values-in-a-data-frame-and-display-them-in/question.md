---
title: "To divide the values in a data frame and display them in the row below"
site: stackoverflow
question_id: 75873683
url: https://stackoverflow.com/q/75873683
asked: 2023-03-29T06:08:36Z
asked_by: "ghost_like"
asked_by_url: https://stackoverflow.com/users/21084140
last_edited: never
tags: [python, pandas, dataframe]
score: 1
views_at_snapshot: 76
answer_count: 2
accepted_answer_id: 75873715
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d152dca9322ad04f3fe598909ce19c3c13b5b98457f0bb33b0084e2ddd72e81a
---

# To divide the values in a data frame and display them in the row below

Asked by [ghost_like](https://stackoverflow.com/users/21084140) on Stack Overflow, <https://stackoverflow.com/q/75873683>, 2023-03-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

There is a data frame with three columns: model, kind, and feature.

    df = pd.DataFrame({'model':['animal','anmimal','plants','plants'],
           'kind':['cat','dog','mushroom','gingseng'],
           'feature'['cute/small','reliable/kind/big','delicious/dark','healthy/bitter/expensive']})


[![enter image description here][1]][1]


In feature, several feature values are lumped together with '/' in between.

I'd like to mark it in the below row separately with '/' like below

[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/HLMr4.png
  [2]: https://i.sstatic.net/wiwiE.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user459872](https://stackoverflow.com/users/6699447)** (2023-03-29): Do you want the model and kind column as empty or the data from previous row?
