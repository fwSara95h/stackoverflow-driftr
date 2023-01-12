---
title: "Parsing a table from website (choosing correct HTML tag)"
site: stackoverflow
question_id: 75099596
url: https://stackoverflow.com/q/75099596
asked: 2023-01-12T16:40:40Z
asked_by: "Fareed"
asked_by_url: https://stackoverflow.com/users/18088207
last_edited: 2023-01-13T08:04:22Z
last_editor: "flappix"
last_editor_url: https://stackoverflow.com/users/2213309
tags: [python, beautifulsoup]
score: -1
views_at_snapshot: 40
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 73307d1a5b904d90259b23bb452f8d2ad6e146147360ecaa0215ddcf4006064b
---

# Parsing a table from website (choosing correct HTML tag)

Asked by [Fareed](https://stackoverflow.com/users/18088207) on Stack Overflow, <https://stackoverflow.com/q/75099596>, 2023-01-12, last edited 2023-01-13 by [flappix](https://stackoverflow.com/users/2213309). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need to make dataframe from the following page: http://pitzavod.ru/products/upakovka/
````
from bs4 import BeautifulSoup
import pandas as pd
import requests
kre = requests.get(f'http://pitzavod.ru/products/upakovka/')
soup = BeautifulSoup(kre.text, 'lxml')
table1 = soup.find('table', id="tab3")
````
I chose "tab3", as I find in the HTML text <div class="tab-pane fade" id="tab3". But the variable table1  gives no output. How can I get the table? Thank You.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[flappix](https://stackoverflow.com/users/2213309)** (2023-01-12): There is no ```table``` with id ```tab3``` on the linked page just a ```div``` with this id.
