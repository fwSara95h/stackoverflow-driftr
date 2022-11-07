---
title: "my excel sheet did not display result after webscrapping using selenium and export to excel"
site: stackoverflow
question_id: 74342077
url: https://stackoverflow.com/q/74342077
asked: 2022-11-07T04:49:25Z
asked_by: "Chloe Chew"
asked_by_url: https://stackoverflow.com/users/20238176
last_edited: 2022-11-07T04:59:17Z
tags: [python, excel, selenium, web-scraping, xpath]
score: 0
views_at_snapshot: 38
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aab3335fa49cf573a128bfacffa6ea60702f4c61f846d83876ef07418ae0b95f
---

# my excel sheet did not display result after webscrapping using selenium and export to excel

Asked by [Chloe Chew](https://stackoverflow.com/users/20238176) on Stack Overflow, <https://stackoverflow.com/q/74342077>, 2022-11-07, last edited 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I would like to extract the serial number and and the expirydate from this link into excel sheet 

[https://www.dell.com/support/home/en-sg/product-support/servicetag/0-ZUQwbW14d28xZHZBYTZWNDdHVy80Zz090/overview][1]

 After watching tutorial on how to extract using selenium and run the code on python (using pycharm) my excel sheet was created but there is no output of the result other than the header and a chromewebsite popped out.

Here's my code:

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

url = "https://www.dell.com/support/home/en-sg/product-support/servicetag/0-ZUQwbW14d28xZHZBYTZWNDdHVy80Zz090/overview"
path = "C:\\Users\\ChloeChew\\Downloads\\chromedriver_win32\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(url)

frame = driver.find_elements(by="xpath", value="//div[@class='product-info d-flex flex-column align-items-center d-lg-block product-info-width']")

serialnumbers = []
expirydates = []

for result in frame:
    serialnumber = driver.find_elements(by="xpath", value="//div[@class='service-tag mb-0 d-none d-lg-block']")
    expirydate = driver.find_elements(by="xpath", value="//div[@class='warrantyExpiringLabel mb-0 ml-1 mr-1']")

    serialnumbers.append(serialnumber)
    expirydates.append(expirydate)

my_dict = {'serialnumber' : serialnumbers, 'expirydate' : expirydates}
df_headlines=pd.DataFrame(my_dict)
df_headlines.to_excel("practice123.xlsx")
```

I also did another code using Beautifulsoup instead but the excel sheet was completely empty (without header or anything) which is why i decided to try selenium. yet the outcome is fairly the same.

[![enter image description here](https://i.sstatic.net/ZWAc4.png)](https://i.sstatic.net/ZWAc4.png)


  [1]: https://www.dell.com/support/home/en-sg/product-support/servicetag/0-ZUQwbW14d28xZHZBYTZWNDdHVy80Zz090/overview
