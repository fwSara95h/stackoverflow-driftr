---
title: "itterating over a set of data - so that i fetch data from a site with beautiful-soup, panda and store it subsequently"
site: stackoverflow
question_id: 75828524
answer_id: 75831805
url: https://stackoverflow.com/a/75831805
author: "baduker"
author_url: https://stackoverflow.com/users/6106791
posted: 2023-03-24T09:13:30Z
last_edited: 2023-03-25T17:15:54Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ea144a49ecaab54660503241e2f1844b02e95846f66cc294d78e89a586691974
role: another answer on the same question, kept as context; not my work
---

# Answer by [baduker](https://stackoverflow.com/users/6106791) — 2023-03-24

Posted on Stack Overflow, <https://stackoverflow.com/a/75831805>, 2023-03-24, last edited 2023-03-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I'd resort to using `pandas` mostly, as the data on the site is pretty well structured, so it shouldn't be hard to get it with minimal effort and then massage it a bit to the format you like.

**NOTE**: The servers are pretty slow, so you can access the `.csv` file thru my [onedrive link](https://1drv.ms/u/s!ArAg_nhR8Mj8gRQIR6IkYdOmaUsZ?e=sRUhSW), where you can find the output file with all the data.

**ANOTHER NOTE**: Please proofread the data, to see if that's *exactly* what you need.

Try this:

```python
import requests
from bs4 import BeautifulSoup

import pandas as pd

main_url = "https://schulen.bildung-rp.de"
columns_to_drop = [
    "letzte Änderung:",
]

with requests.Session() as s:
    anchors = (
        BeautifulSoup(s.get(main_url).content, "lxml")
        .select("#schulen > tbody > tr > td > a")
    )
    urls = [
        f'{main_url}{anchor["href"]}' for anchor in anchors
        if anchor["href"].startswith("/einzelanzeige")
    ]
    tables = [
        pd.read_html(s.get(url).text, flavor="lxml", index_col=0)[0].T
        for url in urls
    ]
    df = (
        pd
        .concat(tables, ignore_index=True)
        .drop(columns=columns_to_drop)
    )
    df["Anschrift:"].replace({"\xa0": " "}, regex=True, inplace=True)
    df.to_csv("daten_für_alle_schulen.csv", index=False)
```

This should get you a `.csv` file that looks something like this:

[![!\[Final Data Table Output][1]][1]


  [1]: https://i.sstatic.net/02hbn.jpg

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): many thanks dear Baduker for sharing your ideas and thoughts - this is really cool. And i am learning alot. Your great!!
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): hello dear baduker - again this is so awesome.  your ideas are brilliant - and i learn alot from you - and your competence to solve problems.  Could you perhaps have a look at this tiny script that i struggle with  - here: https://stackoverflow.com/questions/75828625/nonetype-object-is-not-subscriptable-bs4-task-fails-permanently - i would be more than happy. - have a great day.  Yours Malaga
- **[baduker](https://stackoverflow.com/users/6106791)** (2023-03-25): You already have two answers there. Also, you can just download the data in an Excel file straight from the site. No need to scrape the tables.
