---
title: "Web Scrape table data from this webpage"
site: stackoverflow
question_id: 74216240
answer_id: 74216953
url: https://stackoverflow.com/a/74216953
author: "QHarr"
author_url: https://stackoverflow.com/users/6241235
posted: 2022-10-27T04:50:37Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 86acaee25d37631dc1f8e1573128dca3b60fd95e3fc5ba3f5115e77d62098346
role: another answer on the same question, kept as context; not my work
---

# Answer by [QHarr](https://stackoverflow.com/users/6241235) — 2022-10-27

Posted on Stack Overflow, <https://stackoverflow.com/a/74216953>, 2022-10-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The contents for constructing the table are within a script tag. You can extract the relevant string and re-create the table through string manipulation.

    import requests, re
    import pandas as pd
    
    r = requests.get('https://www.lochinvar.com/products/commercial-water-heaters/armor-condensing-water-heater/').text
    s = re.sub(r'\\"', '"', re.search(r'table":"([\s\S]+?)(?:","tableFootNote)', r).groups(1)[0])
    lines = [i.split('\\t') for i in s.split('\\n')]
    df = pd.DataFrame(lines[1:], columns = lines[:1])
    df.head(5)
