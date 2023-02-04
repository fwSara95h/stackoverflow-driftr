---
title: "Creating dataframe from XML file with non-unique tags"
site: stackoverflow
question_id: 75346930
answer_id: 75348373
url: https://stackoverflow.com/a/75348373
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-02-04T21:05:14Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 859cf560d5eb7cf00512d46b8c859e36a84df3bdbbfe95698798082462ea3d3e
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75348373>, 2023-02-04; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

To parse one XML file using `beautifulsoup` you can use this example:

```py
from bs4 import BeautifulSoup

def get_info(xml_file):
    with open(xml_file, 'r') as f_in:
        soup = BeautifulSoup(f_in.read(), 'xml')

    file_name = soup.find(lambda tag: tag.name == 'PathName' and '.mp4' in tag.text).text.rsplit('.mp4', maxsplit=1)[0]
    url = soup.select_one('[sourceType="Proxy"] PathName').text
    brand_name = soup.select_one('BrandName').text
    id_ = soup.select_one('BHGXId').text

    return file_name, brand_name, id_, url

print(get_info('your_file.xml'))
```

Prints:

```
('zzTap_zzTop_AAAA1111999Z_30s_Pill_aa-bb', 'zzTop', 'AAAA1111999Z', 'https://app.url.com/DMM/DL/wew52f')
```
