---
title: "Pandas Read HTML wont scrape the clickable image"
site: stackoverflow
question_id: 74232047
url: https://stackoverflow.com/q/74232047
asked: 2022-10-28T07:38:18Z
asked_by: "Gerard"
asked_by_url: https://stackoverflow.com/users/5760497
last_edited: 2022-10-30T13:43:28Z
tags: [python, pandas, selenium, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 227
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d3e0918716d9fa27ac92195245060913e2e3d5cb0dbed93825681aeee11b5395
---

# Pandas Read HTML wont scrape the clickable image

Asked by [Gerard](https://stackoverflow.com/users/5760497) on Stack Overflow, <https://stackoverflow.com/q/74232047>, 2022-10-28, last edited 2022-10-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

For reference I am scraping this website: https://apps.proni.gov.uk/Val12B/SearchResults.aspx

The table looked like this:
[![enter image description here][1]][1]


I am trying to scrape this table along with the clickable links on the PRONI REFERENCE header.

my code is:

```table_elements = driver.find_elements_by_xpath(".//table[@id='gvSearchResults']")```
```dfs = []
for i in table_elements:
    a = pd.read_html(i.get_attribute('outerHTML'))
    dfs.append(a[0])
``` 
but the dataframe looks like:
[![enter image description here][2]][2]

my next plan to to individually scrape the href, collect it as a list and join it to the previous dataframe, unfortunately upon inspecting the elements, the table elements containing the link does not have an href.

[![enter image description here][3]][3]

The ideal dataframe should contain the clickable link which will be saved as an excel file.

  [1]: https://i.sstatic.net/rAIxe.png
  [2]: https://i.sstatic.net/o19jC.png
  [3]: https://i.sstatic.net/bzIk1.jpg
