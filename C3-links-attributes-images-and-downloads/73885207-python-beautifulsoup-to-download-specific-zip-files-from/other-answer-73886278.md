---
title: "python beautifulsoup to download specific .zip files from a website"
site: stackoverflow
question_id: 73885207
answer_id: 73886278
url: https://stackoverflow.com/a/73886278
author: "André C. Andersen"
author_url: https://stackoverflow.com/users/604048
posted: 2022-09-28T18:30:07Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 68868fa4a69c4ed7197f13134ff54cdac7fe8d0d7e4911f1da64740d68f673b9
role: another answer on the same question, kept as context; not my work
---

# Answer by [André C. Andersen](https://stackoverflow.com/users/604048) — 2022-09-28

Posted on Stack Overflow, <https://stackoverflow.com/a/73886278>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The following code will find the links, download the files, and unzip them.

```python
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import zipfile

target_folder = os.path.dirname(os.path.realpath(__file__))
base_url = "https://download.cms.gov/nppes"

url = f"{base_url}/NPI_Files.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elms = soup.select('div.bulletlistleft > ul > li > a')
for elm in elms:
    zip_filename = elm.attrs['href'].lstrip('./')
    zip_full_url = "/".join((base_url, zip_filename))
    target_zip_path = os.path.join(target_folder, zip_filename)
    target_zip_dir = ".".join(target_zip_path.split('.')[:-1])
    urlretrieve(zip_full_url, target_zip_path)

    with zipfile.ZipFile(target_zip_path, 'r') as zip_file:
        zip_file.extractall(target_zip_dir)
```
