---
title: "I can't download the product image"
site: stackoverflow
question_id: 73875675
url: https://stackoverflow.com/q/73875675
asked: 2022-09-28T02:49:38Z
asked_by: "Felipe"
asked_by_url: https://stackoverflow.com/users/20021812
last_edited: never
tags: [python, selenium, web-scraping]
score: -1
views_at_snapshot: 165
answer_count: 2
accepted_answer_id: 73876351
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 794069c1605b2fb48d5f867f31d9c7b2b584f3dc3bc4921998fc9d49ada7a1f0
---

# I can't download the product image

Asked by [Felipe](https://stackoverflow.com/users/20021812) on Stack Overflow, <https://stackoverflow.com/q/73875675>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need to know how I can download the second product image, as it is inside a TAG in quotes.

An alternative would also be to just copy the image link to save in a DF.

[Link Element][1]

    import pandas as pd
    import xlsxwriter
    import pyautogui
    import urllib.request
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://shopee.com.br/Tapete-Sala-1-00-X-1-50-Peludo-Shaggy-Macio-Quarto-Felpudo-        
    i.346235717.7779211526")
    driver.maximize_window()
    
    df = pd.read_excel (r"C:\__Imagens e Planilhas Python\Shopee\Videos\Videos.xlsx")


    for index, row in df.iterrows():
    links = driver.get(str(row["links"]))
    sleep(5)
    video = driver.find_element(By. CLASS_NAME, "_1OPdfl")
    sleep(5)
    atributoSrc = video.get_attribute("src")
    print(atributoSrc)
    try:
        urllib.request.urlretrieve(atributoSrc,r"C:\__Imagens e Planilhas Python\Shopee\Videos     
    Baixados\nome" +  str(row["salvar"]) + ".mp4")

        
    except:
        print("error")


  [1]: https://i.sstatic.net/G4qcT.jpg
