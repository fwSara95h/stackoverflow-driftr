---
title: "I can't download the product image"
site: stackoverflow
question_id: 73875675
answer_id: 73920017
url: https://stackoverflow.com/a/73920017
author: "Felipe"
author_url: https://stackoverflow.com/users/20021812
posted: 2022-10-01T16:32:30Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe1860bf0bbb20db4b131aafbb479cadd90e3d8458a1b4b40f7bb0d4dab9fd71
role: another answer on the same question, kept as context; not my work
---

# Answer by [Felipe](https://stackoverflow.com/users/20021812) — 2022-10-01

Posted on Stack Overflow, <https://stackoverflow.com/a/73920017>, 2022-10-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

thanks, following your logic, I'll build my own line of codes that worked


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
    driver.get("https://www.google.com.br")
    driver.maximize_window()

    df = pd.read_excel (r"C:\__Imagens e Planilhas                     
    Python\Shopee\Videos\LinksAfiliado.xlsx")

    Link = []

    for index, row in df.iterrows():
    
    links = driver.get(str(row["links"]))
    sleep(5)    
    classe = driver.find_element(By. CLASS_NAME, "_3DKwBj")
    sleep(5)
    atributo = classe.get_attribute("style")
    link_imagem = atributo.split('url("')[1].split('")')[0]

    print(link_imagem)

    Link.append(link_imagem)
          
    data = {'Link Imagem': Link} 
    df = pd.DataFrame(data)
 
    df.to_excel(r"C:\__Imagens e Planilhas Python\Shopee\Videos\linkimagens.xlsx", 
    engine='xlsxwriter')   
    print(df)
