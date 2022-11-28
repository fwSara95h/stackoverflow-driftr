---
title: "Selenium Data scraping issue, unproper data scrapped"
site: stackoverflow
question_id: 74601118
url: https://stackoverflow.com/q/74601118
asked: 2022-11-28T13:13:09Z
asked_by: "Lalit Joshi"
asked_by_url: https://stackoverflow.com/users/19430670
last_edited: never
tags: [python, pandas, selenium, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 65
answer_count: 1
accepted_answer_id: 74604995
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 740c8ab832a50b71cfb7199b1fc2567cd17282c2805bf8953d432721fd19dda5
---

# Selenium Data scraping issue, unproper data scrapped

Asked by [Lalit Joshi](https://stackoverflow.com/users/19430670) on Stack Overflow, <https://stackoverflow.com/q/74601118>, 2022-11-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape data from:- https://www.canadapharmacy.com/

below are a few pages that I need to scrape:-

https://www.canadapharmacy.com/products/abilify-tablet,

https://www.canadapharmacy.com/products/accolate,

https://www.canadapharmacy.com/products/abilify-mt

I need all the information from the page. I wrote the below code:-


Using Soup:-

    base_url = 'https://www.canadapharmacy.com'
    data = []
    for i in tqdm(range(len(test))):
        r = requests.get(base_url+test[i])
        
        soup = BeautifulSoup(r.text,'lxml')
        # Scraping medicine Name
        try:
            main_name = (soup.find('h1',{"class":"mn"}).text.lstrip()).rstrip()
        except:
            main_name = None
        
        try:
            sec_name = ((soup.find('div',{"class":"product-name"}).find('h3').text.lstrip()).rstrip()).replace('\n','')
        except:
            sec_name = None
        
        try:
            generic_name = (soup.find('div',{"class":"card product generic strength equal"}).find('div').find('h3').text.lstrip()).rstrip()
        except:
            generic_name = None
            
        # Description
        
        card = ''.join([x.get_text(' ',strip=True) for x in soup.select('div.answer.expanded')])
    
        try:
            des = card.split('Directions')[0].replace('Description','')
        except:
            des = None
        
        try:
            drc = card.split('Directions')[1].split('Ingredients')[0]
        except:
            drc = None
            
        try:
            ingre= card.split('Directions')[1].split('Ingredients')[1].split('Cautions')[0]
        except:
            ingre = None
        
        try:
            cau=card.split('Directions')[1].split('Ingredients')[1].split('Cautions')[1].split('Side Effects')[0]
        except:
            cau = None
        try:
            se= card.split('Directions')[1].split('Ingredients')[1].split('Cautions')[1].split('Side Effects')[1]
        except: 
            se = None
    
        for j in soup.find('div',{"class":"answer expanded"}).find_all('h4'):
            if 'Product Code' in j.text:
                prod_code = j.text
            
        #prod_code = soup.find('div',{"class":"answer expanded"}).find_all('h4')[5].text #//div[@class='answer expanded']//h4
        
        pharma = {"primary_name":main_name,
                "secondary_name":sec_name,
                "Generic_Name":generic_name,
                'Description':des,
                'Directions':drc,
                'Ingredients':ingre,
                'Cautions':cau,
                'Side Effects':se,
                "Product_Code":prod_code}
        
        data.append(pharma)


Using Selenium:-

    main_name = []
    sec_name = []
    generic_name = []
    strength = []
    quantity = []
    desc = []
    direc = []
    ingre = []
    cau = []
    side_effect = []
    prod_code = []
    
    for i in tqdm(range(len(test_url))):
        card = []
        driver.get(base_url+test_url[i])
        time.sleep(1)
    
        try:
            main_name.append(driver.find_element(By.XPATH,"//div[@class='card product brand strength equal']//h3").text)
        except:
            main_name.append(None)
    
        try:
            sec_name.append(driver.find_element(By.XPATH,"//div[@class='card product generic strength equal']//h3").text)
        except:
            sec_name.append(None)
    
        try:
            generic_name.append(driver.find_element(By.XPATH,"//div[@class='card product generic strength equal']//h3").text)
        except:
            generic_name.append(None)
    
        try:
            for i in driver.find_elements(By.XPATH,"//div[@class='product-content']//div[@class='product-select']//form"):
                strength.append(i.text)
    
        except:
            strength.append(None)
    
    #     try:
    #         for i in driver.find_elements(By.XPATH,"//div[@class='product-select']//form//div[@class='product-select-options'][2]"):
    #             quantity.append(i.text)
    #     except:
    #         quantity.append(None)
    
        card.append(driver.find_element(By.XPATH,"//div[@class='answer expanded']").text)
    
        try:
            desc.append(card[0].split('Directions')[0].replace('Description',''))
        except:
            desc.append(None)
    
        try:
            direc.append(card[0].split('Directions')[1].split('Ingredients')[0])
        except:
            direc.append(None)
    
        try:
            ingre.append(card[0].split('Directions')[1].split('Ingredients')[1].split('Cautions')[0])
        except:
            ingre.append(None)
    
        try:
            cau.append(card[0].split('Directions')[1].split('Ingredients')[1].split('Cautions')[1].split('Side Effects')[0])
        except:
            cau.append(None)
        try:
            #side_effect.append(card.split('Directions')[1].split('Ingredients')[1].split('Cautions')[1].split('Side Effects')[1])
            side_effect.append(card[0].split('Cautions')[1].split('Side Effects')[1])
        except: 
            side_effect.append(None)
    
        for j in driver.find_elements(By.XPATH,"//div[@class='answer expanded']//h4"):
            if 'Product Code' in j.text:
                prod_code.append(j.text)

I am able to scrap the data from the pages but facing an issue while scraping the Strength and quantity box. I want to write the code in such a manner so that I could scrape the data from every medicine separately and convert it data frame with columns like 2mg, 5mg, 10mg , 30 tablets, 90 tablets and shows prices. 

I tried this code:-

    medicine_name1 = []
    medicine_name2 = []
    strength = []
    quantity = []
    
    for i in tqdm(range(len(test_url))):
        driver.get(base_url+test_url[i])
        time.sleep(1)
        
        try:
            name1 = driver.find_element(By.XPATH,"//div[@class='card product brand strength equal']//h3").text
        except:
            name1 = None
            
        try:
            name2 = driver.find_element(By.XPATH,"//div[@class='card product generic strength equal']//h3").text
        except:
            name2 = None
            
        try:
            for i in driver.find_elements(By.XPATH,"//div[@class='product-select']//form//div[@class='product-select-options'][1]"):
                strength.append(i.text)
                medicine_name1.append(name1)
                medicine_name2.append(name2)
        except:
            strength.append(None)
            
        try:
            for i in driver.find_elements(By.XPATH,"//div[@class='product-select']//form//div[@class='product-select-options'][2]"):
                quantity.append(i.text)
        except:
            quantity.append(None)

It works fine but still, here I am getting repeated values for the medicine. Could anyone please check?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Life is complex](https://stackoverflow.com/users/6083423)** (2022-11-28): Please provide some output for your Selenium code. This output will allow others to see your issue more clearly.  Also provide some details on this line in your code `requests.get(base_url+test[i])`.  What are the `test` values?
