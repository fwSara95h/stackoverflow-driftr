---
title: "Hi. I'm trying to scrape infinite scrolling website. It stuck in 200th data"
site: stackoverflow
question_id: 74598056
url: https://stackoverflow.com/q/74598056
asked: 2022-11-28T08:46:22Z
asked_by: "Rasim Dilbani"
asked_by_url: https://stackoverflow.com/users/20316348
last_edited: never
tags: [python, selenium, selenium-webdriver, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 157
answer_count: 1
accepted_answer_id: 74631249
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ec8ead5026b83491eb607c1c042f1ea54722ce58103460c699f17478987ddd62
---

# Hi. I'm trying to scrape infinite scrolling website. It stuck in 200th data

Asked by [Rasim Dilbani](https://stackoverflow.com/users/20316348) on Stack Overflow, <https://stackoverflow.com/q/74598056>, 2022-11-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I scrolled with selenium and grabbed all urls and used these urls in beautifulsoup.But there are so many duplicates in scraped data.I tried to left them with drop_duplicates but it stack in about 200th data .I cannot detect the problem. I add the code which i use. I want to grab all prices,areas,rooms et.c. 


```


import requests

from lxml import html

from bs4 import BeautifulSoup as bs
import bs4
import pandas as pd


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import pandas as pd
import time

driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
driver.get('https://tap.az/elanlar/dasinmaz-emlak/menziller')
time.sleep(1)

price = []
citi = []
elann = []
bina = []
arrea = []
adres = []
roome = []
baxhise = []
mulkayet = []
descript = []
urll = []
zefer = []
previous_height = driver.execute_script('return document.body.scrollHeight')


while True:
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    time.sleep(2)
    
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == previous_height:
        break 
    previous_height = new_height
    lnks=driver.find_elements(By.CSS_SELECTOR, '#content > div > div > div.categories-products.js-categories-products > div.js-endless-container.products.endless-products > div.products-i')
    for itema in lnks:
        urla=itema.find_element(By.TAG_NAME, 'a')  
        aae = (urla.get_attribute('href'))
        urel = aae.split('/bookmark')[0]
        result = requests.get(urel)
        soup = bs(result.text, 'html.parser')
        casee = soup.find_all("div",{"class":"lot-body l-center"})
        for ae in casee:        
            c =  ae.find_all('table', class_ = 'properties')
            pp = c[0].text
            city = pp.split('Şəhər')[-1].split('Elanın')[0].replace('ş' ,'sh').replace('ə' ,'e').replace('ü' ,'u').replace('ö' ,'o').replace('ı' ,'i').replace('ğ' ,'g').replace('ç' ,'ch').replace('Ç', 'ch').replace('Ş', 'sh').replace('Ə' ,'e').replace('Ü' ,'u').replace('Ö' ,'o').replace('İ', 'I')
            cxe = c[0].text
            elan_tipi = cxe.split('Elanın tipi')[-1].split('Binanın tipi')[0].replace(' verilir','')
            elane = elan_tipi.replace(' ', '_').replace('ş' ,'sh').replace('ə' ,'e').replace('ü' ,'u').replace('ö' ,'o').replace('ı' ,'i').replace('ğ' ,'g').replace('ç' ,'ch').replace('Ç', 'ch').replace('Ş', 'sh').replace('Ə' ,'e').replace('Ü' ,'u').replace('Ö' ,'o').replace('İ', 'I')
            cx = c[0].text
            bina_tipi = cx.split('Binanın tipi')[-1].split('Sahə')[0].replace(' ', '_').replace('ş' ,'sh').replace('ə' ,'e').replace('ü' ,'u').replace('ö' ,'o').replace('ı' ,'i').replace('ğ' ,'g').replace('ç' ,'ch').replace('Ç', 'ch').replace('Ş', 'sh').replace('Ə' ,'e').replace('Ü' ,'u').replace('Ö' ,'o').replace('İ', 'I')
            cx = c[0].text
            area = cx.split('tikiliSahə,')[-1].split('Otaq')[0].replace('m²', '')                         
            cx = c[0].text
            room = cx.split('Otaq sayı')[-1].split('Yerləşmə yeri')[0]
            cx = c[0].text
            addresss = cx.split('Yerləşmə yeri')[-1].replace('ş' ,'sh').replace('ə' ,'e').replace('ü' ,'u').replace('ö' ,'o').replace('ı' ,'i').replace('ğ' ,'g').replace('ç' ,'ch').replace('Ç', 'ch').replace('Ş', 'sh').replace('Ə' ,'e').replace('Ü' ,'u').replace('Ö' ,'o').replace('İ', 'I')
            d = ae.find_all('p')
            elan_kod = (d[0].text.replace('Elanın nömrəsi:', ''))
            d = ae.find_all('p')
            baxhis = d[1].text.replace('Baxışların sayı: ', '')
            d = ae.find_all('p')
            description = (d[3].text.replace('Baxışların sayı: ', '').replace('ş' ,'sh').replace('ə' ,'e').replace('ü' ,'u').replace('ö' ,'o').replace('ı' ,'i').replace('ğ' ,'g').replace('ç' ,'ch').replace('Ç', 'ch').replace('Ş', 'sh').replace('Ə' ,'e').replace('Ü' ,'u').replace('Ö' ,'o').replace('İ', 'I').replace("\n", ''))
            kim =  ae.find_all('div', class_ = 'author')
            kime = kim[0].text
            if 'bütün' in kime:
                mulkiyet = int(0)
            else:
                mulkiyet = int(1)
        caseee = soup.find_all("div",{"class":"middle"})
        for aecex in caseee:        
            pricxxe =  aecex.find_all('span', class_ = 'price-val') 
            pricef = pricxxe[0].text.replace(' ' , '')
            price.append(pricef)
            zefer.append(elane)
            elann.append(elan_kod)
            citi.append(city)
            bina.append(bina_tipi)
            arrea.append(area)
            adres.append(addresss)
            roome.append(room)
            baxhise.append(baxhis)
            mulkayet.append(mulkiyet)
            descript.append(description)
            ae = pd.DataFrame({'URL': urel,'Unique_id': elann,'Price': price,'Room': roome,'Area': arrea,'Seher': citi,'Elan_tipi': zefer,'Description': descript,'Address': adres,'Category': bina,'Mulkiyyet': mulkayet})
            aere = ae.drop_duplicates()
            aere.to_csv('dde.csv', index=False, encoding='utf-8' )
        


```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[darren](https://stackoverflow.com/users/7318120)** (2022-11-28): You should use `from webdriver_manager.chrome import ChromeDriverManager` in place of `webdriver.Chrome(path_name_to_webdriver.exe)`.
- **me** (2022-11-28): what do you mean by it's stuck? is there an error? or does the program just hang?
- **[Rasim Dilbani](https://stackoverflow.com/users/20316348)** (2022-11-30): @Driftr95 program just hang and i have to restart kernel.
- **[Rasim Dilbani](https://stackoverflow.com/users/20316348)** (2022-11-30): @D.L in place of webdriver.Chrome(path_name_to_webdriver.exe) is an error could you please give more explanation that. thanks
- **[darren](https://stackoverflow.com/users/7318120)** (2022-11-30): @ElxanCabbarli :   this might not solve, but it is a cleaner way to access the latest version of chromedriver which reduces error rate.    https://stackoverflow.com/questions/71603374/webdriverexception-unknown-error-cannot-find-chrome-binary-error-when-trying-t/71626868#71626868
