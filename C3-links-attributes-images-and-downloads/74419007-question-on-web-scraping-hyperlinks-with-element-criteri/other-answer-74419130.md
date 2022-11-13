---
title: "Question on web-scraping hyperlinks with element criteria using python on tennisexplorer.com"
site: stackoverflow
question_id: 74419007
answer_id: 74419130
url: https://stackoverflow.com/a/74419130
author: "Barry the Platipus"
author_url: https://stackoverflow.com/users/19475185
posted: 2022-11-13T07:14:42Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2bd89c9e53afa338a9fc78142f733d2da7f6b4150ed4d0a4cb82ca02ee833019
role: another answer on the same question, kept as context; not my work
---

# Answer by [Barry the Platipus](https://stackoverflow.com/users/19475185) — 2022-11-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74419130>, 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is a way to get a dataframe (with one column) with urls pointing to every match detail:

    import requests
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    
    url = 'https://www.tennisexplorer.com/results/?type=atp-single&year=2022&month=09&day=08'
    
    big_list = []
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    links = soup.select('table tbody tr td:last-child a')
    for l in links:
        big_list.append(l.get('href'))
    df = pd.DataFrame(big_list, columns = ['Url'])
    print(df)

Result in terminal:



    Url
    0	/match-detail/?id=2188301
    1	/match-detail/?id=2188937
    2	/match-detail/?id=2188807
    3	/match-detail/?id=2188867
    4	/match-detail/?id=2188869
    ...	...
    131	/results/?year=2022&month=09&day=11
    132	/results/?year=2022&month=09&day=18
    133	/results/?year=2022&month=09&day=25
    134	/results/?year=2022&month=10&day=02
    135	/results/?year=2022&month=10&day=09
    136 rows × 1 columns

You can further filter those urls based on text, for example (if you only want the `info` links, you did not clarify it)

See BeautifulSoup documentation here: https://beautiful-soup-4.readthedocs.io/en/latest/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Md. Fazlul Hoque](https://stackoverflow.com/users/12848411)** (2022-11-13): Good solution just make them absolute urls that's always a better way. +1
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-13): Cheers @Fazlul and and you're right. I guess I'm a bit burnout, and missing some of the finer details.
