---
title: "operate over values of a dictionary when values are lists"
site: stackoverflow
question_id: 75284350
url: https://stackoverflow.com/q/75284350
asked: 2023-01-30T12:25:53Z
asked_by: "Wiliam"
asked_by_url: https://stackoverflow.com/users/9720696
last_edited: never
tags: [python, dictionary, nltk]
score: 0
views_at_snapshot: 66
answer_count: 1
accepted_answer_id: 75343141
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e1b7e8764e0be8fd8c6512fc8dedd97fdb26ba97e740a5909c4252a141767ebf
---

# operate over values of a dictionary when values are lists

Asked by [Wiliam](https://stackoverflow.com/users/9720696) on Stack Overflow, <https://stackoverflow.com/q/75284350>, 2023-01-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Suppose I have the following dictionary: 

    data = {'ACCOUNT_CLOSURE': ['account closure',
      'close account',
      'close bank',
      'terminate account',
      'account deletion',
      'cancel account',
      'account cancellation'],
     'ACCOUNT_CHANGE': ['change my account',
      'switch my account',
      'change from private into savings',
      'convert into family package',
      'change title of the account',
      'make title account to family',
      'help me access the documentation']}

I want to go through each key and subsequently the elements of the values and drop the stopwords, so I do: 

    stop_words = set(stopwords.words("english"))
    
    for key, values in data.items():
        data[key] = [value for value in values if value not in stop_words]

but this returns the exact same dictionary as my original one. I wonder what am I doing wrong?
