---
title: "Is there a 'rowspan' or 'merge two table cells to single table cell' function for pandas tables/dataframes?"
site: stackoverflow
question_id: 75933430
url: https://stackoverflow.com/q/75933430
asked: 2023-04-04T20:07:16Z
asked_by: "Kactaceapengu"
asked_by_url: https://stackoverflow.com/users/21521937
last_edited: 2023-04-04T20:15:50Z
tags: [python, pandas, dataframe]
score: -1
views_at_snapshot: 584
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ae9e20eaf43911f61df573af27f77d31d79f6f839c6842820cc3760c558da057
---

# Is there a 'rowspan' or 'merge two table cells to single table cell' function for pandas tables/dataframes?

Asked by [Kactaceapengu](https://stackoverflow.com/users/21521937) on Stack Overflow, <https://stackoverflow.com/q/75933430>, 2023-04-04, last edited 2023-04-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to create a table with some values spanning over two rows, but I can't find any solution. I have appended two images of what I got from pandas and how I want it to look like.

[output from pandas:](https://i.sstatic.net/R0eG8.png)

[target table form:](https://i.sstatic.net/1aEG0.jpg) 



Here is the code of my testing:

```
import pandas as pd

dict = {'index': [('LCS', 'sequence1'),('LCS', 'sequence2')],
        'columns': ['alignment', 'score', 'pathcoordinates'],
        'data': [['AAAGT', '', ''], ['GGTAC', 5, '[4,5] -> [5,5]']],
        'index_names': ['', ''],
        'column_names': [''],
        }

df1 = pd.DataFrame.from_dict(dict, orient='tight')
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mozway](https://stackoverflow.com/users/16343464)** (2023-04-04): Pandas doesn't do merged cells.
- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-04-04): No.  Remember that a pandas table is just a collection of columns, where each column is an independent numpy array.  There's no relationship between the rows, or the columns.  If you need it printed in a certain way, then you are free to do whatever you need to do.
