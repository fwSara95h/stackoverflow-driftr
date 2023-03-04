---
title: "How to transform a DataFrame with a complicated series in a new DataFrame"
site: stackoverflow
question_id: 75636296
url: https://stackoverflow.com/q/75636296
asked: 2023-03-04T14:27:44Z
asked_by: "pedrosjo"
asked_by_url: https://stackoverflow.com/users/20278443
last_edited: 2023-03-04T14:47:15Z
tags: [python, arrays, list, dictionary, series]
score: -1
views_at_snapshot: 46
answer_count: 2
accepted_answer_id: 75636599
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 620be384b1b13b2b626955a32dc5c5eddf44725d12729446c40b9d4f2234ee3a
---

# How to transform a DataFrame with a complicated series in a new DataFrame

Asked by [pedrosjo](https://stackoverflow.com/users/20278443) on Stack Overflow, <https://stackoverflow.com/q/75636296>, 2023-03-04, last edited 2023-03-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm going through a hard time trying to transform a dataframe with 2 columns into another DataFrame. The first column is my index (ints) and the another column is a complicated series. For what i'm able to see the structure of the series goes like this:

A dictionary with one key and one value. The value is a list of simple dictionaries with key/value pairs.

My DataFrame looks like that:

[![enter image description here][1]][1]

Series:

    {
    "CashFlowDto": [
        {
            "TicketId": None,
            "Type": "Amrt",
            "Amount": 560.61,
            "PercentualAmount": 0.0494481,
            "MaturityDate": datetime.datetime(2023, 7, 10, 0, 0),
            "PaymentDate": datetime.datetime(2023, 7, 10, 0, 0),
        },
        {
            "TicketId": None,
            "Type": "Amrt",
            "Amount": 552.05,
            "PercentualAmount": 0.048693,
            "MaturityDate": datetime.datetime(2023, 8, 10, 0, 0),
            "PaymentDate": datetime.datetime(2023, 8, 10, 0, 0),
        }
    ]}

My desired output:

[![enter image description here][2]][2]


Could you guys help me, please?

Thanks

  [1]: https://i.sstatic.net/SfjDF.png
  [2]: https://i.sstatic.net/3Souc.png
