---
title: "getting the span text from bs4"
site: stackoverflow
question_id: 74281093
answer_id: 74281266
url: https://stackoverflow.com/a/74281266
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-11-01T20:08:11Z
last_edited: never
accepted: true
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2549d832511631a237410258bb984bcc1a56c076bdd453562536dc82ee88deaa
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-11-01

Posted on Stack Overflow, <https://stackoverflow.com/a/74281266>, 2022-11-01; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try:

```py
import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.betexplorer.com/soccer/england/premier-league/results/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")


def get_odd_or_text(td):
    if "data-odd" in td.attrs:
        return td["data-odd"]

    odd = td.select_one("[data-odd]")
    if odd:
        return odd["data-odd"]

    return td.get_text(strip=True)


all_data = []
for row in soup.select(".table-main tr:has(td)"):
    tds = [get_odd_or_text(td) for td in row.select("td")]
    round_ = row.find_previous("th").find_previous("tr").th.text
    all_data.append([round_, *tds])

df = pd.DataFrame(
    all_data, columns=["Round", "Match", "Score", "1", "X", "2", "Date"]
)
print(df.head().to_markdown(index=False))
df.to_csv('data.csv', index=False)
```

Prints:

| Round     | Match                   | Score   |    1 |    X |     2 | Date   |
|:----------|:------------------------|:--------|-----:|-----:|------:|:-------|
| 14. Round | Arsenal-Nottingham      | 5:0     | 1.22 | 6.75 | 13.19 | 30.10. |
| 14. Round | Manchester Utd-West Ham | 1:0     | 1.71 | 3.87 |  4.97 | 30.10. |
| 14. Round | Bournemouth-Tottenham   | 2:3     | 4.97 | 3.72 |  1.74 | 29.10. |
| 14. Round | Brentford-Wolves        | 1:1     | 2.17 | 3.43 |  3.41 | 29.10. |
| 14. Round | Brighton-Chelsea        | 4:1     | 3.07 | 3.35 |  2.38 | 29.10. |

and saves `data.csv` (screenshot from LibreOffice):

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/Rjilj.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Paul Corcoran](https://stackoverflow.com/users/18776287)** (2022-11-01): thank you. spectacular
