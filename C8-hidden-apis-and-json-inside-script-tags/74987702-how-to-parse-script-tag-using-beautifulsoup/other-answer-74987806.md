---
title: "How to parse <script> tag using beautifulsoup"
site: stackoverflow
question_id: 74987702
answer_id: 74987806
url: https://stackoverflow.com/a/74987806
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-01-02T23:13:11Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b11087083c5d45b5ee89d57c2952016694800b527155cf62751ad4febd516c67
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-01-02

Posted on Stack Overflow, <https://stackoverflow.com/a/74987806>, 2023-01-02; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

One solution is to parse the required data with `re`/`json` module:

```py
import json
import pprint
import re

import requests

url = "https://www.glassdoor.com/Reviews/Alteryx-Reviews-E351220.htm"

html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

reviews = re.search(r'"reviews":(\[.*?}\])}', html, flags=re.S).group(1)
reviews = json.loads(reviews)

pprint.pprint(reviews)
```

Prints:

```py
[{'__typename': 'EmployerReview',
  'advice': "Don't rush too finish a project",
  'adviceOriginal': None,
  'cons': 'Typical like other companies where newbies get higher salary and '
          'you have to work your way up for promotions nothing really bad',
  'consOriginal': None,
  'countHelpful': 0,
  'countNotHelpful': 0,
  'divisionLink': None,
  'divisionName': None,
  'employer': {'__ref': 'Employer:351220'},
  'employerResponses': [],
  'employmentStatus': None,
  'isCovid19': False,
  'isCurrentJob': True,
  'isLanguageMismatch': False,
  'isLegal': True,
  'jobEndingYear': None,
  'jobTitle': None,
  'languageId': 'eng',
  'lengthOfEmployment': 6,
  'location': None,

...and so on.
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Dunc](https://stackoverflow.com/users/20907457)** (2023-01-02): Thank you! This is exactly what I needed. For future reference, could you explain what the regex statement here is doing exactly?
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-02): @Dunc The `"reviews":(\[.*?}\])}` will try to find a text that follows `"reviews":` and ends with `}]}` (this should be the final three letters in `"reviews"` variable)
