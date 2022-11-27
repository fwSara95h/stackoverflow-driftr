---
title: "is there a better way to get the data form beautiful soup query?"
site: stackoverflow
question_id: 74590759
url: https://stackoverflow.com/q/74590759
asked: 2022-11-27T14:18:04Z
asked_by: "Nima Hojat"
asked_by_url: https://stackoverflow.com/users/20298996
last_edited: 2022-11-27T18:15:52Z
tags: [python, beautifulsoup]
score: 1
views_at_snapshot: 139
answer_count: 2
accepted_answer_id: 74590848
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 06cfcc7a02c3b4f73bc63071b4e04356c58437910f5ad3a4b7911c1e78885737
---

# is there a better way to get the data form beautiful soup query?

Asked by [Nima Hojat](https://stackoverflow.com/users/20298996) on Stack Overflow, <https://stackoverflow.com/q/74590759>, 2022-11-27, last edited 2022-11-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to extract the m/z data for different ions from "https://www.lipidmaps.org/databases/lmsd/LMFA08040013".
I can get access to the ions and thier data, however to extract the formula and m/z, I am thinking to convert it to a string and the use striping tool to extract it. Is thier another way using beautifulsoup?

```

from bs4 import BeautifulSoup #used to interact with the website
import requests
soup = BeautifulSoup(requests.get("https://www.lipidmaps.org/databases/lmsd/LMFA08040013").text, "html.parser")

for option in soup.find_all('option'):
    ion = option.text
    option = str(option)
    m_z = ion
    ion_formula = 
    return ([m_z,ion-formula,ion]
```

example of option data:

```
<option data-display-formula="C&lt;sub&gt;18&lt;/sub&gt;H&lt;sub&gt;38&lt;/sub&gt;NO&lt;sub&gt;2&lt;/sub&gt;" data-formula="C18H38NO2" data-mass-z-ratio="300.2897" value="MplusH">
                                    [M+H]+
                                </option>
```

Example of output data:

```

m_z = 300.2897
ion-formula = C18H38NO2
ion = \[M+H\]+
```
