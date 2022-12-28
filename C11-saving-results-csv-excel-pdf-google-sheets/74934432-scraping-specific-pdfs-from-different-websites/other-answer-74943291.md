---
title: "Scraping specific pdfs from different websites"
site: stackoverflow
question_id: 74934432
answer_id: 74943291
url: https://stackoverflow.com/a/74943291
author: "Cesare"
author_url: https://stackoverflow.com/users/18899582
posted: 2022-12-28T17:33:05Z
last_edited: 2022-12-29T08:22:09Z
last_editor: "Heliton Martins"
last_editor_url: https://stackoverflow.com/users/5160230
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3de0136236fe459223492693f30e5bda95ff5dbb2fa322b7228521fc9b48d928
role: another answer on the same question, kept as context; not my work
---

# Answer by [Cesare](https://stackoverflow.com/users/18899582) — 2022-12-28

Posted on Stack Overflow, <https://stackoverflow.com/a/74943291>, 2022-12-28, last edited 2022-12-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I have tried to solve this by adding different steps so that it can check at the same time what year the pdf comes from and add it to the name. The code is below, and it is an improvement, however, the answer above by Driftr95 is way better than mine, if someone wants to replicate this they should use his code.

    import requests
    import pandas
    import os
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup
    
    data = pandas.read_csv('urls.csv') 
    urls = data['url'].tolist()
    years = data["yearstr"].tolist()
    numbers = data["number"].tolist()
    
    folder_location = r'C:\Users\dario.marino5\Documents\R\webscraping'
    if not os.path.exists(folder_location):
        os.mkdir(folder_location)
    
    for url, year, number in zip(urls, years, numbers):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")     
    
        for link in soup.select("a[href$='.pdf']"):
            if year in link['href']:
                # Construct the filename with the number from the CSV file
                filename = f'document_{year}_{number}.pdf'
                filename = os.path.join(folder_location, filename)
    
                # Download the PDF file and save it to the filename
                with open(filename, 'wb') as f:
                    f.write(requests.get(urljoin(url, link['href'])).content)
