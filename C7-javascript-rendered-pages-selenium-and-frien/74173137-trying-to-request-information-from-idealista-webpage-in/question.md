---
title: "Trying to request information from \"IDEALISTA webpage\" in PYTHON with \"requests\" and I get <Response [403]>"
site: stackoverflow
question_id: 74173137
url: https://stackoverflow.com/q/74173137
asked: 2022-10-23T17:06:52Z
asked_by: "Javier Cabrera"
asked_by_url: https://stackoverflow.com/users/20315236
last_edited: never
tags: [web-scraping, beautifulsoup, python-requests, http-headers, http-status-code-403]
score: -1
views_at_snapshot: 1512
answer_count: 2
accepted_answer_id: none
closed: 2022-10-24T19:39:07Z (Needs details or clarity)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dc65e2ee957605ac59f379c2875f495c0019c3c328ef77005241793df28f8302
---

# Trying to request information from "IDEALISTA webpage" in PYTHON with "requests" and I get <Response [403]>

Asked by [Javier Cabrera](https://stackoverflow.com/users/20315236) on Stack Overflow, <https://stackoverflow.com/q/74173137>, 2022-10-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Its a easy starting project that I'm doing, but the main body would be accesing to the information on the Webpage , so , I don't know if i'm doing something wrong

the starting code is: (to see if it works on Fotocasa Webpage)

    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://www.fotocasa.es/es/comprar/vivienda/valencia-capital/aire-acondicionado-trastero-ascensor-no-amueblado/161485852/d'
    # url = 'https://www.idealista.com/inmueble/97795476/'
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }
    
    r = requests.get(url, headers=headers)
    print(r)
    
    req = requests.get(url, headers=headers).text
    
    # Now that the content is ready, iterate
    # through the content using BeautifulSoup:
    soup = BeautifulSoup(req, "html.parser")
    
    # get the information of a given tag
    inm = soup.find(class_="re-DetailHeader-propertyTitle").text
    print(inm)

You can try and see that with the URL of Fotocasa , works perfectly (gets <Response [200]>) , but with the one from Idealista, doesn't work, (gets <Response [403]>)

the code is:

    import requests
    from bs4 import BeautifulSoup
    
    # url = 'https://www.fotocasa.es/es/comprar/vivienda/valencia-capital/aire-acondicionado-trastero-ascensor-no-amueblado/161485852/d'
    url = 'https://www.idealista.com/inmueble/97795476/'
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }
    
    r = requests.get(url, headers=headers)
    print(r)
    
    req = requests.get(url, headers=headers).text
    
    # Now that the content is ready, iterate
    # through the content using BeautifulSoup:
    soup = BeautifulSoup(req, "html.parser")
    
    # get the information of a given tag
    inm = soup.find(class_="main-info__title-main").text
    print(inm)
