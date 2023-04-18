---
title: "how to extract text from table with same class name using BeautifulSoup?"
site: stackoverflow
question_id: 76046043
url: https://stackoverflow.com/q/76046043
asked: 2023-04-18T14:49:21Z
asked_by: "Temp4 Watch"
asked_by_url: https://stackoverflow.com/users/21397514
last_edited: never
tags: [python, pandas, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 34
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6e29e1c90318e8a53380c931f2f2f9845d4c730ff162dd3b70a83341664fcd4d
---

# how to extract text from table with same class name using BeautifulSoup?

Asked by [Temp4 Watch](https://stackoverflow.com/users/21397514) on Stack Overflow, <https://stackoverflow.com/q/76046043>, 2023-04-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have tried to extract from the table with same class name but its getting messed the table.

    import pandas as pd
    from bs4 import BeautifulSoup as extractor
    import requests
    from dateutil import parser
    import numpy as np

    for page in range(1, 354):
        ba="https://www.airlinequality.com/airline-reviews/british-airways/page/"+str(page)
        Headers={'User-agent': 'Mozilla/5.0'}
        response=requests.get(ba, headers=Headers)
        soup=extractor(response.content, "html.parser")
        for Reviewer in soup.findAll("article", itemprop="review"):
            type_of_traveller=Reviewer.find("tr", class_="review-rating-header type_of_traveller")
print(type_of_traveller)

When i try to print the above code i am getting a all the cell as None.

    array([None, None, None, ..., None, None, None], dtype=object)

Expected Output

    Type of Traveller
    Couple leisure
    Family leisure
    Solo leisure
    .
    .
    .
Does anyone know how to solve it.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Temp4 Watch](https://stackoverflow.com/users/21397514)** (2023-04-18): There are 353 pages where i have to extract the text.and there are not only 4 types of travellers its just an example.
