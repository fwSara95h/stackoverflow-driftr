---
title: "is there a better way to get the data form beautiful soup query?"
site: stackoverflow
question_id: 74590759
answer_id: 74590848
url: https://stackoverflow.com/a/74590848
author: "baduker"
author_url: https://stackoverflow.com/users/6106791
posted: 2022-11-27T14:29:30Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1d9ae7c25567f1040c1181d45bbee58918094ae3e1c71ae85e6eb6be5c5c8596
role: another answer on the same question, kept as context; not my work
---

# Answer by [baduker](https://stackoverflow.com/users/6106791) — 2022-11-27

Posted on Stack Overflow, <https://stackoverflow.com/a/74590848>, 2022-11-27; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Not sure what you mean by *more elegant* but if all you want is the first option with the given `ion` value you can get the output you want this way:

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.lipidmaps.org/databases/lmsd/LMFA08040013"
soup = (
    BeautifulSoup(requests.get(url).text, "lxml")
    .select_one(".change\:calculate-mz > option:nth-child(2)")
)

mz = soup["data-mass-z-ratio"]
formula = soup["data-formula"]
ion = soup.getText(strip=True)

print(f"{mz} {formula} {ion}")
```

Output:

```
300.2897 C18H38NO2 [M+H]+
```

To list them all, try this:

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.lipidmaps.org/databases/lmsd/LMFA08040013"
options = (
    BeautifulSoup(requests.get(url).text, "lxml")
    .select(".change\:calculate-mz > option")[1:]
)

for option in options:
    mz = option["data-mass-z-ratio"]
    formula = option["data-formula"]
    ion = option.getText(strip=True)
    print(f"m_z = {mz}\nion-formula = {formula}\nion = {ion}")
    print("-" * 30)
```

Output:

```
m_z = 300.2897
ion-formula = C18H38NO2
ion = [M+H]+
------------------------------
m_z = 282.2791
ion-formula = C18H36NO
ion = [M+H-H2O]+
------------------------------
m_z = 299.2819
ion-formula = C18H37NO2
ion = [M.]+
------------------------------
m_z = 150.6485
ion-formula = C18H39NO2
ion = [M+2H]2+
------------------------------
m_z = 100.7681
ion-formula = C18H40NO2
ion = [M+3H]3+
------------------------------
m_z = 75.8279
ion-formula = C18H41NO2
ion = [M+4H]4+
------------------------------
m_z = 338.2456
ion-formula = C18H37KNO2
ion = [M+K]+
------------------------------
m_z = 188.6044
ion-formula = C18H37K2NO2
ion = [M+2K]2+
------------------------------
m_z = 376.2015
ion-formula = C18H36K2NO2
ion = [M+2K-H]+
------------------------------
m_z = 322.2716
ion-formula = C18H37NNaO2
ion = [M+Na]+
------------------------------
m_z = 172.6304
ion-formula = C18H37NNa2O2
ion = [M+2Na]2+
------------------------------
m_z = 344.2536
ion-formula = C18H36NNa2O2
ion = [M+2Na-H]+
------------------------------
m_z = 306.2979
ion-formula = C18H37LiNO2
ion = [M+Li]+
------------------------------
m_z = 156.6567
ion-formula = C18H37Li2NO2
ion = [M+2Li]2+
------------------------------
m_z = 317.3162
ion-formula = C18H41N2O2
ion = [M+NH4]+
------------------------------
m_z = 298.2752
ion-formula = C18H36NO2
ion = [M-H]-
------------------------------
m_z = 148.6339
ion-formula = C18H35NO2
ion = [M-2H]2-
------------------------------
m_z = 98.7535
ion-formula = C18H34NO2
ion = [M-3H]3-
------------------------------
m_z = 73.8133
ion-formula = C18H33NO2
ion = [M-4H]4-
------------------------------
m_z = 334.2518
ion-formula = C18H37ClNO2
ion = [M+Cl]-
------------------------------
m_z = 358.2963
ion-formula = C20H40NO4
ion = [M+OAc]-
------------------------------
m_z = 344.2806
ion-formula = C19H38NO4
ion = [M+HCOO]-
------------------------------
m_z = 299.2824
ion-formula = C18H37NO2
ion = M(neutral)
------------------------------
```
