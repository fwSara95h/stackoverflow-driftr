---
title: "nested loop returns the same results for multiple rows while webscraping - beautiful soup"
site: stackoverflow
question_id: 74647356
answer_id: 74648103
url: https://stackoverflow.com/a/74648103
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-12-01T21:00:04Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3691fb0b8941c9b7ae9e81790e54dfe1ffb1dbe175fc1ee6649a76b4ba345a3a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-12-01

Posted on Stack Overflow, <https://stackoverflow.com/a/74648103>, 2022-12-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try:

```py
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.apartments.com/atlanta-ga/?bb=lnwszyjy-H4lu8uqH"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, "html.parser")

all_data = []
for art in soup.select("article:has(a)"):
    name, addr = art.a.get_text(strip=True, separator="|").split("|")

    info = art.select_one(".property-info")
    pricing = info.select_one(".property-pricing").text
    beds = info.select_one(".property-beds").text
    amenities = {s.text: "X" for s in info.select(".property-amenities span")}
    phone = info.select_one(".phone-link").text.strip()

    all_data.append([name, addr, pricing, beds, phone, amenities])

df = pd.DataFrame(
    all_data, columns=["Name", "Addr", "Pricing", "Beds", "Phone", "Amenities"]
)
df = pd.concat([df, df.pop("Amenities").apply(pd.Series)], axis=1)
df = df.fillna("")

print(df.head().to_markdown(index=False))
df.to_csv("data.csv", index=False)
```

Prints:

| Name                   | Addr                                    | Pricing        | Beds            | Phone          | Dog & Cat Friendly   | Fitness Center   | Pool   | In Unit Washer & Dryer   | Walk-In Closets   | Clubhouse   | Balcony   | CableReady   | Tub / Shower   | Dishwasher   | Kitchen   | Granite Countertops   | Gated   | Refrigerator   | Range   | Microwave   | Stainless Steel Appliances   | Grill   | Business Center   | Lounge   | Heat   | Oven   | Package Service   | Courtyard   | Ceiling Fans   | Office   | Maintenance on site   | Disposal   |
|:-----------------------|:----------------------------------------|:---------------|:----------------|:---------------|:---------------------|:-----------------|:-------|:-------------------------|:------------------|:------------|:----------|:-------------|:---------------|:-------------|:----------|:----------------------|:--------|:---------------|:--------|:------------|:-----------------------------|:--------|:------------------|:---------|:-------|:-------|:------------------|:------------|:---------------|:---------|:----------------------|:-----------|
| Broadstone Pullman     | 105 Rogers St NE, Atlanta, GA 30317     | $1,630 - 2,825 | Studio - 2 Beds | (470) 944-6584 | X                    | X                | X      | X                        | X                 | X           | X         | X            | X              |              |           |                       |         |                |         |             |                              |         |                   |          |        |        |                   |             |                |          |                       |            |
| 1660 Peachtree Midtown | 1660 Peachtree St NW, Atlanta, GA 30309 | $1,699 - 2,499 | 1-2 Beds        | (470) 944-9920 | X                    | X                | X      | X                        |                   |             |           |              |                | X            | X         | X                     | X       |                |         |             |                              |         |                   |          |        |        |                   |             |                |          |                       |            |
| Mira at Midtown Union  | 1301 Spring St NW, Atlanta, GA 30309    | $1,705 - 6,025 | Studio - 3 Beds | (470) 944-3921 | X                    | X                | X      | X                        |                   | X           |           |              |                | X            |           |                       |         | X              | X       |             |                              |         |                   |          |        |        |                   |             |                |          |                       |            |
| Alexan Summerhill      | 720 Hank Aaron Dr SE, Atlanta, GA 30315 | $1,530 - 3,128 | Studio - 2 Beds | (470) 944-9567 | X                    | X                | X      | X                        | X                 | X           |           |              |                | X            |           |                       |         | X              |         |             |                              |         |                   |          |        |        |                   |             |                |          |                       |            |
| 1824 Defoor            | 1824 Defoor Ave NW, Atlanta, GA 30318   | $1,676 - 3,194 | Studio - 3 Beds | (470) 944-3075 | X                    | X                | X      | X                        | X                 | X           |           |              |                |              |           |                       |         |                | X       | X           |                              |         |                   |          |        |        |                   |             |                |          |                       |            |

and saves `data.csv` (screenshot from LibreOffice):

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/maVcB.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user15564501 (account no longer exists)** (2022-12-02): This is great! I don't understand all of it but I will good those things
