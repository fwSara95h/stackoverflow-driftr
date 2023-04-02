---
title: "Split Pandas DF columns based on condition"
site: stackoverflow
question_id: 75909759
answer_id: 75909959
url: https://stackoverflow.com/a/75909959
author: "SomeDude"
author_url: https://stackoverflow.com/users/1410303
posted: 2023-04-02T03:20:31Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f81c6ee1da06fa1c5e4247c64a66c397864eaa8c930e97ea61d4881ce4518da5
role: another answer on the same question, kept as context; not my work
---

# Answer by [SomeDude](https://stackoverflow.com/users/1410303) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75909959>, 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Assuming you don't have Movie or Genre both in the same row for Tags1, Tags2 

(actually it should work even if you have, but there won't be space between two Movies or Genres in that case)

A fast solution would be to use `Series.str` methods like `str.extract`:

    df["Genre"] = df["Tags1"].str.extract(r"^\s*Genre\s*:\s*(.*?)$").fillna("") + df[
        "Tags2"
    ].str.extract(r"^\s*Genre\s*:\s*(.*?)$").fillna("")
    df["Movie"] = df["Tags1"].str.extract(r"^\s*Movie\s*:\s*(.*?)$").fillna("") + df[
        "Tags2"
    ].str.extract(r"^\s*Movie\s*:\s*(.*?)$").fillna("")
    print(df)

       VideoId          Tags1          Tags2    Genre    Movie
    0     1234           None           None                  
    1     3456    Movie:Rocky    Genre:Drama    Drama    Rocky
    2     5678  Genre:Romance  Movie:Love Me  Romance  Love Me
    3     7890   Movie:Scream   Genre:Horror   Horror   Scream
    4     9012    Movie:Shrek           None             Shrek
