---
title: "Writing csv file - Python-3.x web-scrapping"
site: stackoverflow
question_id: 73858513
answer_id: 73866458
url: https://stackoverflow.com/a/73866458
author: "Barry the Platipus"
author_url: https://stackoverflow.com/users/19475185
posted: 2022-09-27T10:56:53Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c5b915c7a5335ab00b925c74c1ac1b9dc8f753723245bae72392996766ba4f3f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Barry the Platipus](https://stackoverflow.com/users/19475185) — 2022-09-27

Posted on Stack Overflow, <https://stackoverflow.com/a/73866458>, 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

If you just want a csv document from those results (properly cleaned), why not do:

    import requests
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    
    big_list = []
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
    url = 'https://www.pararius.com/apartments/schiedam'
    r = requests.get(url, headers=headers)
    soup = bs(r.text, 'html.parser')
    titles = soup.select('h2.listing-search-item__title a')
    for t in titles:
        big_list.append((t.get_text(strip=True),))
    df = pd.DataFrame(big_list, columns=['Properties'])
    df.to_csv('schiedam_rentals.csv')
    print(df)

Result:


    Properties
    0	Apartment Korte Kerkstraat 1 B
    1	Apartment Tuinlaan
    2	Apartment Burgemeester Van Haarenlaan
    3	Apartment Broersvest
    4	Apartment 's-Gravelandseweg
    5	Apartment Heijermansplein
    6	Apartment Boerhaavelaan
    7	Apartment Rotterdamsedijk 330
    8	Apartment Newtonplein
    9	Apartment Broersvest
    10	Apartment Herenpad
    11	House Ampèrestraat
    12	Apartment Burgemeester Knappertlaan
    13	Apartment Broersveld 91 A
    14	Apartment 's-Gravelandseweg 1065
    15	Apartment Jan Steenstraat
    16	Apartment Burgemeester Knappertlaan
    17	Apartment Nicolaas Beetsstraat 52 A
    18	Apartment Schie 17 C
    19	Apartment Frans Halsplein
    20	Apartment Schiedamseweg 188
    21	Apartment Tuinlaan 50 A
    22	House Pascalstraat
    23	Apartment Albert Cuijpstraat
    24	Apartment Jan Steenstraat
    25	Apartment Frans Halsplein
    26	Apartment Baan 28 E
    27	House Hargplein 51
    28	Apartment Sint Liduinastraat
