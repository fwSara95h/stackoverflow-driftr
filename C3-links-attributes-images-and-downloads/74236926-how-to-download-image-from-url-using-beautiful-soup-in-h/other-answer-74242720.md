---
title: "How to download image from URL using beautiful soup in high quality?"
site: stackoverflow
question_id: 74236926
answer_id: 74242720
url: https://stackoverflow.com/a/74242720
author: "Utsav Upadhyay"
author_url: https://stackoverflow.com/users/10825522
posted: 2022-10-29T03:58:27Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f9b86be1da20f8766a150669e75e4039faa1f00610add0973bf35d622ecfe280
role: another answer on the same question, kept as context; not my work
---

# Answer by [Utsav Upadhyay](https://stackoverflow.com/users/10825522) — 2022-10-29

Posted on Stack Overflow, <https://stackoverflow.com/a/74242720>, 2022-10-29; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I made some changes to download image from URL which is in CSV file

    import csv
    import requests
    import os
    import urllib
    from bs4 import BeautifulSoup as bs
    
    with open('cat.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            imagesname = ' '.join(row)
            r = requests.get(imagesname)
    
            soup = bs(r.content, 'html.parser')
            tables = soup.find_all('img', class_='pick')
    
            for image in tables:
                img_url = image.get('src').replace('\\', '/')
                real_url = "domain-name" + img_url
                
                img_name = str(img_url.split('/')[-1])
     
                urllib.request.urlretrieve(real_url, os.path.join(
                    path, img_name))
