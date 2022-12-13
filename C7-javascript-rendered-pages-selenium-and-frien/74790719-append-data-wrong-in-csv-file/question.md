---
title: "Append data wrong in csv file"
site: stackoverflow
question_id: 74790719
url: https://stackoverflow.com/q/74790719
asked: 2022-12-13T20:49:34Z
asked_by: "Amen Aziz"
asked_by_url: https://stackoverflow.com/users/17344809
last_edited: 2022-12-13T20:58:51Z
tags: [python, pandas, dataframe, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 85
answer_count: 1
accepted_answer_id: 74791332
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8e0441c9a4b1106cc541ab516a2b2e90d6aef7787b040d96598b09c231a42b55
---

# Append data wrong in csv file

Asked by [Amen Aziz](https://stackoverflow.com/users/17344809) on Stack Overflow, <https://stackoverflow.com/q/74790719>, 2022-12-13, last edited 2022-12-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

    from selenium import webdriver           
    import time
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import pandas as pd
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    import requests
    from csv import writer
    
    
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20) 
    
    URL = 'https://mergr.com/firms/search/employees?page=1&firm%5BactiveInvestor%5D=2&sortColumn=employee_weight&sortDirection=asc'
    driver.get(URL)
    
    
    
    email=driver.find_element(By.CSS_SELECTOR,"input#username")
    email.send_keys("timgr8@outlook.com")
    
    password=driver.find_element(By.CSS_SELECTOR,"input#password")
    password.send_keys("Cosmos1990$$$$$$$")
    
    login=driver.find_element(By.CSS_SELECTOR,"button.btn").click()
    
     
    
    
    urls=[]        
    product=[] 
    soup = BeautifulSoup(driver.page_source,"lxml")
    details=soup.select("tbody tr")
    for detail in details:
    
            try:        
                    t1 =detail.select_one("h5.profile-title a").text
            except:
                    pass
      
            wev={
                    'Name':t1,
                    }
            
            product.append(wev)
               
    page_links =driver.find_elements(By.CSS_SELECTOR, "h5.profile-title + p a")
    for link in page_links:
            href=link.get_attribute("href")
            urls.append(href)
            
    
    for url in urls: 
            
            driver.get(url) 
            soup = BeautifulSoup(driver.page_source,"lxml")
            try:
                    website=soup.select_one("p.adress-info a[target='_blank']").text
            except:
                    website=''
            
            data={
                    'website':website
            }
     
            product.append(data)
                    
    df=pd.DataFrame(product)
    df.to_csv('firm.csv')

The data of the `website` will be down in to CSV file  as shown in pic  is I am appending the data in wrong way why is data  moving down  where I am wrong ...Kindly recommend where I am wrong there .......

[![enter image description here][1]][1]


I want output in these format Kindly suggest solution for these...I want output in these format as you shown below...

[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/Z17Ii.png
  [2]: https://i.sstatic.net/84JpO.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Dan](https://stackoverflow.com/users/868044)** (2022-12-13): [How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example)
