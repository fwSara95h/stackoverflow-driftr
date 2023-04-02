---
title: "Split Pandas DF columns based on condition"
site: stackoverflow
question_id: 75909759
url: https://stackoverflow.com/q/75909759
asked: 2023-04-02T02:04:46Z
asked_by: "Aleksei Wolff"
asked_by_url: https://stackoverflow.com/users/21546506
last_edited: never
tags: [python, pandas, dataframe, split]
score: 1
views_at_snapshot: 192
answer_count: 3
accepted_answer_id: 75909936
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fece7744321593450a867da79defd11064f15818083320ad7c7e90b1bef3407a
---

# Split Pandas DF columns based on condition

Asked by [Aleksei Wolff](https://stackoverflow.com/users/21546506) on Stack Overflow, <https://stackoverflow.com/q/75909759>, 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have the below DF I need to manipulate. The problem is the two tags columns can have either none, a Movie title or a Genre. I need to separate the Movie title and Genres into two new separate columns named Movie and Genre respectively and if either column contains none don't even evaluate it.

| VideoId | Tags1 | Tags2 |
| --- | --- | --- |
| 1234 | None | None |
| 3456 | Movie:Rocky | Genre:Drama |
| 5678 | Genre:Romance | Movie:Love Me |
| 7890 | Movie:Scream | Genre:Horror |
| 9012 | Movie:Shrek | None |

So if columns contains Movie: then split the and put the second item of the array into the new Movie Column. If it contains Genre then split and place it in the new Genre column.  I am getting an index out of range for the 'none' columns. And I think I have to reiterate thru each column again to find Genres that are in the Movies DF and vice-versa.  

`Movies = df['Tags1'].apply(lambda x: x.split(':')[1] if 'Movie' in x else x) `

`Genres = df['Tags2'].apply(lambda x: x.split(':')[1] if 'Genre' in x else x) `
 

The resulting DF should look like below:

| VideoId | Movie | Genre |
| --- | --- | --- |
| 1234 | None | None |
| 3456 | Rocky | Drama |
| 5678 | Love Me | Romance |
| 7890 | Scream | Horror |
| 9012 | Shrek | None |

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[alvas](https://stackoverflow.com/users/610569)** (2023-04-02): `df.apply(lambda x: x.split(':')[1] if 'Genre:' in x or 'Movie:' in x else x)`
- **[SomeDude](https://stackoverflow.com/users/1410303)** (2023-04-02): What happens if both Tags1, Tags2 column has Movie: or Genre: in the same row?
