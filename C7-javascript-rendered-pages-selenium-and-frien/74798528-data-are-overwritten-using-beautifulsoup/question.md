---
title: "Data are overwritten using beautifulsoup"
site: stackoverflow
question_id: 74798528
url: https://stackoverflow.com/q/74798528
asked: 2022-12-14T12:45:52Z
asked_by: "Amen Aziz"
asked_by_url: https://stackoverflow.com/users/17344809
last_edited: never
tags: [python, dataframe, selenium, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 94
answer_count: 1
accepted_answer_id: 74819089
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 00931630a61e57f43e0d99a04a5371ddfb87cc0bc61919c663c653d0bfcc76e3
---

# Data are overwritten using beautifulsoup

Asked by [Amen Aziz](https://stackoverflow.com/users/17344809) on Stack Overflow, <https://stackoverflow.com/q/74798528>, 2022-12-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Try to scrape the data but data are overwrite and they will give the data of only 2 page in the csv file kindly recommend any solution for that I an waiting for your response How can I fix this? is there any way then suggest me I think due to for loop they overwrite data Thank you.these is the have already searched for an answer here and spent a long time on google, but nothing... I've already tried opening the file with 'w' instead of 'r' or 'a' but I still can't get my code to

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
    
    url='https://mergr.com/login'
    
    driver.get(url)
    
    email=driver.find_element(By.CSS_SELECTOR,"input#username")
    email.send_keys("timgr8@outlook.com")
    
    password=driver.find_element(By.CSS_SELECTOR,"input#password")
    password.send_keys("Cosmos1990$$$$$$$")
    
    login=driver.find_element(By.CSS_SELECTOR,"button.btn").click()
    
    for page in range(1,3):
            URL = 'https://mergr.com/firms/search/employees?page={page}&firm%5BactiveInvestor%5D=2&sortColumn=employee_weight&sortDirection=asc'.format(page=page)
            driver.get(URL)
    
    
            added_urls = []        
            product=[]
            soup = BeautifulSoup(driver.page_source,"lxml")
            details = soup.select("tbody tr")
            for detail in details:
    
                    try:        
                            t1 = detail.select_one("h5.profile-title a").text
                    except:
                            # pass # then you'll just be using the previous row's t1
                            # [also, if this happens in the first loop, it will raise an error]
    
                            t1 = 'MISSING' # '' #
                    
                  
            
                    wev = {
                            'Name':t1,
                            
                            }
    
                    href = detail.select_one("h5.profile-title + p a[href]") 
                    if href and href.get("href", '').startswith('http'): 
                            wev['page_link'] = href.get("href")
                            added_urls.append(href.get("href"))
                    
                    product.append(wev)
            
            ### IF YOU WANT ROWS THAT CAN'T BE CONNECTED TO NAMES ###       
            page_links = driver.find_elements(By.CSS_SELECTOR, "h5.profile-title + p a")
            for link in page_links:
                    if href in added_urls: continue  # skip links that are already added
                    href = link.get_attribute("href")
    
                    # urls.append(href)
                    added_urls.append(href)
                    product.append({"page_link": href})
            ##########################################################
                    
           
            for pi, prod in enumerate(product): 
                    if "page_link" not in prod or not prod["page_link"]: continue ## missing link
                    url = prod["page_link"]
                    
                    driver.get(url) 
                    soup = BeautifulSoup(driver.page_source,"lxml")
                    try:
                            website=soup.select_one("p.adress-info a[target='_blank']").text
                    except:
                            website=''
                    
                    del product[pi]["page_link"] ## REMOVE this line IF you want a page_link column in csv
    
                    # data={'website':website}
                    # product.append(data)
                    
                    product[pi]['website'] = website
            
                            
    df=pd.DataFrame(product)
    df.to_csv('firm.csv')

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-14): `for page in range(1,3)` - so that will only loop for `i=1` and `i=2`. If you want more pages, try using a larger number than `3`...
- **[Amen Aziz](https://stackoverflow.com/users/17344809)** (2022-12-14): try  but they give me last page data only
- **me** (2022-12-14): Currently, you're clearing the `product` list and the beginning of each page loop - either move the `product=[]` line to *before*  `for page in range(1,3)` **OR** indent the last two lines [with append mode - `df.to_csv('firm.csv', mode='a' )`] to get then inside the page loop; i.e., **the `product=[]` line and the `df...` lines should have the SAME indent level**
- **me** (2022-12-14): (I don't recommend append mode btw, it's a bit annoying - if you use `header=False`, you won't have any headers [unless you write extra code to initialize the csv with them], but if you don't then the header row keeps getting repeated every few rows....)
