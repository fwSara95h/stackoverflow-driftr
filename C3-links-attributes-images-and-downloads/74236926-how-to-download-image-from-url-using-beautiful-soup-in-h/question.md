---
title: "How to download image from URL using beautiful soup in high quality?"
site: stackoverflow
question_id: 74236926
url: https://stackoverflow.com/q/74236926
asked: 2022-10-28T14:35:18Z
asked_by: "Utsav Upadhyay"
asked_by_url: https://stackoverflow.com/users/10825522
last_edited: never
tags: [python-3.x, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 1020
answer_count: 2
accepted_answer_id: 74242720
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7cac7040ff3d4e6e3291f8e0944383be162502c4c8bb1c52f2e48c2c9a6c312f
---

# How to download image from URL using beautiful soup in high quality?

Asked by [Utsav Upadhyay](https://stackoverflow.com/users/10825522) on Stack Overflow, <https://stackoverflow.com/q/74236926>, 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to **download images using beautiful soup While Importing a list of URLs from .CSV file**. Now I am getting results like below,

    <img class="pick" src="backup/remote_2109image/008f3ef7-1da9-11ec-abad-88ae1db4aa6901.jpg" width="350height=616\"/>

In the below code, I am **trying to get an image from URL that has the class 'pick'**

Now, How Will I download this in a folder?

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
                print(image)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Bijay Regmi](https://stackoverflow.com/users/8591711)** (2022-10-28): you can fetch image content with `img_content = requests.get(url + image["src"]).content` which has byte content of image. Now you write this into a file using `("my_img.jpg", "wb").write(img_content)`
- **[Utsav Upadhyay](https://stackoverflow.com/users/10825522)** (2022-10-28): this is not working, also I have to save the image name the same as shown in the code, no hard coded image name
