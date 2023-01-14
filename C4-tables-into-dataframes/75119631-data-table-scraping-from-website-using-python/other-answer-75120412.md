---
title: "Data/Table Scraping from Website using Python"
site: stackoverflow
question_id: 75119631
answer_id: 75120412
url: https://stackoverflow.com/a/75120412
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-01-14T18:39:41Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 27312537f170688a77d100b3f1cf4cad887087ef52abacee95cbb55391baec4b
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-01-14

Posted on Stack Overflow, <https://stackoverflow.com/a/75120412>, 2023-01-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can try to use `pd.read_html` to read the table into a dataframe:

```py
import pandas as pd

url = "https://kr.youtubers.me/united-states/all/top-500-youtube-channels-in-united-states/en"

df = pd.read_html(url)[0]
print(df)
```

Prints:

```none
     rank                                            Youtuber  subscribers  video views  video count              category  started
0       1                                   ✿ Kids Diana Show    106000000  86400421379         1052        People & Blogs     2015
1       2                                          Movieclips     58500000  59672883333        39903      Film & Animation     2006
2       3                                        Ryan's World     34100000  53568277882         2290         Entertainment     2015
3       4                                     Toys and Colors     38300000  44050683425          901         Entertainment     2016
4       5   LooLoo Kids - Nursery Rhymes and Children's Songs     52200000  30758617681          605                 Music     2014
5       6                                            LankyBox     22500000  30147589773         6913                Comedy     2016
6       7                                          D Billions     24200000  27485780190          582                   NaN     2019
7       8                   BabyBus - Kids Songs and Cartoons     31200000  25202247059         1946             Education     2016
8       9                                              FGTeeV     21500000  23255537029         1659                Gaming     2013

...and so on.
```
