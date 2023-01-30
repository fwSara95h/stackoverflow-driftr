---
title: "Brings back only first data point out of 20 possible on page(BeautifulSoup Scraping)"
site: stackoverflow
question_id: 75279360
url: https://stackoverflow.com/q/75279360
asked: 2023-01-30T00:26:06Z
asked_by: "eInvincible"
asked_by_url: https://stackoverflow.com/users/21089758
last_edited: never
tags: [python, beautifulsoup, containers]
score: -1
views_at_snapshot: 20
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e5eee45819237175240867ac969ce7fc4abb10fead4f4fa6b82e560c41aba24
---

# Brings back only first data point out of 20 possible on page(BeautifulSoup Scraping)

Asked by [eInvincible](https://stackoverflow.com/users/21089758) on Stack Overflow, <https://stackoverflow.com/q/75279360>, 2023-01-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.


```
from bs4 import BeautifulSoup
import requests
import xlsxwriter

number = 1
counter = 0
row = 0
wb = xlsxwriter.Workbook('try002.xlsx')
sheet = wb.add_worksheet()
while number <= 150:
    url = "https://www.realtor.com/realestateagents/houston_tx/photo-1/sort-activelistings/pg-{}".format(number)
    base = 'https://www.realtor.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find_all('ul', class_='jsx-1526930885')
    # print(container)
    for con in container:
        try:
            name = con.find('div', class_='jsx-2987058905 agent-name text-bold').text
        except:
            name = 'no price found'
        try:
            pnumber = con.find('div', class_='jsx-2987058905 agent-phone hidden-xs hidden-xxs').text
        except:
            pnumber = 'no type found'
        sheet.write(row, 0, name)
        sheet.write(row, 1, pnumber)
        counter += 1
        row += 1
        print(counter)
    number += 1
    print(url)
wb.close()
```

Because the names and numbers are held under the same class and div and such IDs, I would expect it to bring back all 20 per page, but it only brings back the first, how can I bring all 20 back. As shown in photo, all 20 realtors per page are in the same class identity, and their name and numbers are also in the same class. How can I make it return all values in those classes not just the first set?[Each Subtree is one of the realtor pages](https://i.sstatic.net/k37HC.png)
