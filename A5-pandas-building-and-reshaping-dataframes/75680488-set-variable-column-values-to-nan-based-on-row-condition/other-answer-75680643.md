---
title: "Set variable column values to nan based on row condition"
site: stackoverflow
question_id: 75680488
answer_id: 75680643
url: https://stackoverflow.com/a/75680643
author: "rajendra"
author_url: https://stackoverflow.com/users/2105924
posted: 2023-03-09T05:10:01Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 552a5d577a572d0c8ccc1c7b11783fe33bf431ae644b47c279820fa395a19dd5
role: another answer on the same question, kept as context; not my work
---

# Answer by [rajendra](https://stackoverflow.com/users/2105924) — 2023-03-09

Posted on Stack Overflow, <https://stackoverflow.com/a/75680643>, 2023-03-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You an use `apply` with `result_type='broadcast'`. (Edit: borrowing @marcelo-paco's code)

    def make_nan(row):
        row[-row[0]:] = np.nan
        return row
    
    df = pd.DataFrame({'col_ind': [3, 2, 1], 'col_1': ['a', 'd', 'g'], 'col_2': ['b', 'e', 'h'], 'col_3': ['c', 'f', 'i']})
    df[:] = df.apply(make_nan, axis=1, result_type='broadcast')
    df

This will give:

    col_ind	col_1	col_2	col_3
    	3	NaN	     NaN	NaN
    	2	d	     NaN	NaN
    	1	g	      h	    NaN

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[thefrollickingnerd](https://stackoverflow.com/users/10339757)** (2023-03-09): Is `row[-row[0]:]' pseudo code? Do you not need to specify iloc?
- **[rajendra](https://stackoverflow.com/users/2105924)** (2023-03-09): It's not a pseudo code. It is using the first element to index the rest of the elements.
- **[thefrollickingnerd](https://stackoverflow.com/users/10339757)** (2023-03-09): This method crashes the kernal of my notebook. Also in my code I want to use a named column, I've replaced 0 with 'col name', I assume that is fine?
- **[rajendra](https://stackoverflow.com/users/2105924)** (2023-03-09): This assumes the values in col_ind are between 1 and 3. Not sure what you mean by "replaced 0 with 'col name'. You can make an edit and update your question.
- **[thefrollickingnerd](https://stackoverflow.com/users/10339757)** (2023-03-09): I used a mock df for my example but my actual df is larger, so instead of using the column index for the condition column, I used the column name. Presumably the same syntax.
