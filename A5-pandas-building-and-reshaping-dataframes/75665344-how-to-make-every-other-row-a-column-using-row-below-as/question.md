---
title: "How to make every other row a column using row below as the value in Pandas?"
site: stackoverflow
question_id: 75665344
url: https://stackoverflow.com/q/75665344
asked: 2023-03-07T17:29:04Z
asked_by: "user3486773"
asked_by_url: https://stackoverflow.com/users/3486773
last_edited: 2023-03-07T17:34:56Z
tags: [python, pandas, dataframe]
score: 1
views_at_snapshot: 82
answer_count: 3
accepted_answer_id: 75665479
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 62e88144c5b2aa17d6ba07b9a4dc1b4e1467c584689828ba9234581df476fa4c
---

# How to make every other row a column using row below as the value in Pandas?

Asked by [user3486773](https://stackoverflow.com/users/3486773) on Stack Overflow, <https://stackoverflow.com/q/75665344>, 2023-03-07, last edited 2023-03-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a pandas dataframe that looks like this:


      df = pd.DataFrame.from_dict({'type': {4: 'Second Product',
      5: 'table',
      6: 'First Product',
      7: 'chair',
      8: 'Second Product',
      9: 'desk',
      10: 'First Product',
      11: 'chair'},
     'id': {4: 'cust1',
      5: 'cust1',
      6: 'cust1',
      7: 'cust1',
      8: 'cust2',
      9: 'cust2',
      10: 'cust2',
      11: 'cust2'}})


But I need the 'type' column broken out into column, value.  So the column names would be 'Second Product', and 'First Product', but the values would be the row below those. Like this:

    df = pd.DataFrame.from_dict({'cust': {4:'cust1', 5:'cust2' },'Second Product': {4: 'table',
      5: 'desk'},
     'First Product': {4: 'chair',
      5: 'chair'}})


the other catch is, there could be more than just first and second products, and I want to get all the columns and fill blanks or nans where they don't exist.  So if there is one customer who has a 'Third Product'  I need that to be a column and where others don't have a third product value, fill that as blank or nans.

I have tried transposing, stacking, unstacking and setting indexes etc...  and I'm just stuck as to how to go about this.

Edit: I am not worried about the index being reset, so it doesn't need to match my example exactly.
