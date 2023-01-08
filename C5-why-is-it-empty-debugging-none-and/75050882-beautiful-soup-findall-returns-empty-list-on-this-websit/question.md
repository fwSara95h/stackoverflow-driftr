---
title: "Beautiful soup findAll returns empty list on this website?"
site: stackoverflow
question_id: 75050882
url: https://stackoverflow.com/q/75050882
asked: 2023-01-08T20:01:57Z
asked_by: "Vincent Cormier"
asked_by_url: https://stackoverflow.com/users/20960009
last_edited: 2023-01-08T20:11:07Z
last_editor: "jsotola"
last_editor_url: https://stackoverflow.com/users/6901081
tags: [parsing, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 33
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1e5eb42fab96a09680f2e6714cdcfbe956e47082404f513fb3dda8c72b83a03e
---

# Beautiful soup findAll returns empty list on this website?

Asked by [Vincent Cormier](https://stackoverflow.com/users/20960009) on Stack Overflow, <https://stackoverflow.com/q/75050882>, 2023-01-08, last edited 2023-01-08 by [jsotola](https://stackoverflow.com/users/6901081). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to extract property value history from this website:https://www.properly.ca/buy/home/view/ma-tEpHcSzeES-OlhE-V6A/bc/vancouver/1268-w-broadway-%23720/

But my code returns an empty list instead of the property cost history.



I used the following code:
```python
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url= "https://www.properly.ca/buy/home/view/ma-tEpHcSzeES-OlhE-V6A/bc/vancouver/1268-w-broadway-%23720/"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
officials = soup.findAll("table",{"id":"property-history"})

for entry in officials:
    print(str(entry))
```

Which returns an empty list, although this URL does have a property history table. Any help would be appreciated.

Thanks!
