---
title: "What is going on? (Attemp at scraping multiple pages)"
site: stackoverflow
question_id: 74411153
answer_id: 74411346
url: https://stackoverflow.com/a/74411346
author: "Barry the Platipus"
author_url: https://stackoverflow.com/users/19475185
posted: 2022-11-12T08:13:09Z
last_edited: never
accepted: true
score: 3
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d86e975b12a307251794dafd4a11ae0e6bd43c1e69d42b3316a629f1d9248173
role: another answer on the same question, kept as context; not my work
---

# Answer by [Barry the Platipus](https://stackoverflow.com/users/19475185) — 2022-11-12

Posted on Stack Overflow, <https://stackoverflow.com/a/74411346>, 2022-11-12; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is a way to get those listings (didn't go for an infinite loop, you're welcome to increase page count and look up for the existence of an element in page (like `next page` url, etc) if you want). There are 10 pages:

    import requests
    from bs4 import BeautifulSoup as bs
    from tqdm import tqdm
    import pandas as pd
    import time as t
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    
    s = requests.Session()
    s.headers.update(headers)
    
    big_list = []
    for x in tqdm(range(1, 11)):
        r = s.get(f'https://www.gumtree.com/search?search_category=cars&search_location=uk&q=ferrari&page={x}')
        soup = bs(r.text, 'html.parser')
        cards = soup.select('div[class="listing-content"]')
        for c in cards:
            title = c.select_one('h2[class="listing-title"]').text.strip()
            location = c.select_one('div[class="listing-location"]').text.strip()
            price = c.select_one('span[class="listing-price"]').text.strip()
            big_list.append((title, location, price))
        t.sleep(3)
    df = pd.DataFrame(big_list, columns = ['title', 'location', 'price'])
    print(df)
    df.to_csv('absurd_cars_uk.csv')

This will print out the dataframe, and also save it to disk, as csv:

    	title	location	price
    0	2011 11 FERRARI CALIFORNIA 4.3 2 PLUS 2 Auto 4...	Liskeard, Cornwall	£77,500
    1	2011 61 FERRARI FF 6.3 V12 4WD 660bhp with ver...	Liskeard, Cornwall	£88,500
    2	2020 Ferrari 812 Superfast 6.5 V12 F1 DCT Euro...	Huthwaite, Nottinghamshire	£294,980
    3	FERRARI F430 SPIDER Black AUTO Petrol, 2007	Spalding, Lincolnshire	£110,000
    4	1982 Ferrari 308 GTSi Coupe Petrol Manual	Newark, Nottinghamshire	£73,000
    ...	...	...	...
    130	2001 (X) FERRARI 360 3.6 MODENA F1 2DR	Dinnington, South Yorkshire	£64,880
    131	2012 Ferrari 458 4.5 Italia Auto Seq 2dr COUPE...	St Albans, Hertfordshire	£139,995
    132	1997 Ferrari 456 GTA - 6700 miles	Ripon, North Yorkshire	£59,995
    133	2021 Ferrari Roma 3.8T V8 F1 DCT Euro 6 (s/s) ...	York, North Yorkshire	£194,995
    134	2015 Ferrari California 3.8 V8 T F1 DCT Euro 6...	Loughborough, Leicestershire	£99,950
    135 rows × 3 columns

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jack9992](https://stackoverflow.com/users/20483330)** (2022-11-12): Is pandas needed to scrape multiple pages?
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-12): No, @Jack9992. It's needed for meaningful display of information, as well as saving it.
- **[Jack9992](https://stackoverflow.com/users/20483330)** (2022-11-12): Thank you so much for your answers Barry. I really appreciate it. Does this script look okay to you? I've made some editing to it .@Driftr95 recommended changing these things. Here is the script https://pastebin.com/V057zv3a
