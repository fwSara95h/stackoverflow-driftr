---
title: "How to make a dictionary from 2 lists from web scraping"
site: stackoverflow
question_id: 74596046
answer_id: 74596094
url: https://stackoverflow.com/a/74596094
author: "Kris"
author_url: https://stackoverflow.com/users/995052
posted: 2022-11-28T04:46:07Z
last_edited: 2022-11-28T04:52:41Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e62e6d2cb6f38cfd5e6a6ee523cea9acad8c5bc4f9c94ab6788d332cddd75bd2
role: another answer on the same question, kept as context; not my work
---

# Answer by [Kris](https://stackoverflow.com/users/995052) — 2022-11-28

Posted on Stack Overflow, <https://stackoverflow.com/a/74596094>, 2022-11-28, last edited 2022-11-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You have the column values, just build the `DataFrame`

Eg., 


    from pandas import DataFrame
    
    category = ["Aircraft", 'Type of Traveller', 'Seat Type']
    rating = ['A320', 'Solo', 'Business Class']
    
    # Create the records from both list, using zip and dict calls.
    data_dict = dict(zip(category, rating))
    
    # Build the dataframe from the dictionary.
    df = DataFrame.from_records(data_dict, columns=category, index=[0])
    
    print(df)

Looks like this. [![enter image description here][1]][1]



  [1]: https://i.sstatic.net/15C3J.png
