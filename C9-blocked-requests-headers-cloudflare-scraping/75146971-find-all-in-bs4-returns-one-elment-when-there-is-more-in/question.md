---
title: "FInd_all in bs4 returns one elment when there is more in the web page in"
site: stackoverflow
question_id: 75146971
url: https://stackoverflow.com/q/75146971
asked: 2023-01-17T13:13:41Z
asked_by: "majduddin alboon"
asked_by_url: https://stackoverflow.com/users/14315689
last_edited: never
tags: [python, html, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 53
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 40cf46f5894421d8f87c8b08f86b8030b4291f9998f739a540439f2f0e734fe9
---

# FInd_all in bs4 returns one elment when there is more in the web page in

Asked by [majduddin alboon](https://stackoverflow.com/users/14315689) on Stack Overflow, <https://stackoverflow.com/q/75146971>, 2023-01-17. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am doing web scrapping to a new egg page and i want to scrape the rating of the product by the consumers and i am using this code

    page = requests.get('https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632?Description=gpu&cm_re=gpu-_-14-137-632-_-Product').text
    soup = bs(page , 'lxml')
    the_rating = soup.find_all( class_ = 'rating rating-4')
    print(the_rating)
And it returns only this one element even though I am using the find all element

    [<i class="rating rating-4"></i>]

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jon Clements](https://stackoverflow.com/users/1252759)** (2023-01-17): There's only that one element that has a class attribute containing *both* rating and rating-4 though...
- **[majduddin alboon](https://stackoverflow.com/users/14315689)** (2023-01-17): this is just an example all of the ratings return one elment even the rating rating-5 elment that is the thing that i seem not understand?/
- **[Marco Aurelio Fernandez Reyes](https://stackoverflow.com/users/12511801)** (2023-01-17): @majduddinalboon I got the recaptha with your code, but, if you manage to get the data, check [this answer](https://stackoverflow.com/a/35465898/12511801)
