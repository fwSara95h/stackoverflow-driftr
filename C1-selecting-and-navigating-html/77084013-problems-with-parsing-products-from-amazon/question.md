---
title: "Problems with parsing products from amazon"
site: stackoverflow
question_id: 77084013
url: https://stackoverflow.com/q/77084013
asked: 2023-09-11T18:27:17Z
asked_by: "Timur"
asked_by_url: https://stackoverflow.com/users/22539580
last_edited: 2023-09-12T17:21:10Z
tags: [python, parsing, beautifulsoup]
score: -1
views_at_snapshot: 121
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3ad70e748e080c8efe6d71f18ad4a77590e6c45004ab3313c4e9419a31ef51b4
---

# Problems with parsing products from amazon

Asked by [Timur](https://stackoverflow.com/users/22539580) on Stack Overflow, <https://stackoverflow.com/q/77084013>, 2023-09-11, last edited 2023-09-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I wanted to parse amazon products, but I got this traceback. I cant't figure out why it is happening. I think it may happened because the site doesn't want me to do this.


Traceback (most recent call last):

  File "c:\Users\grafity\Desktop\main.py", line 42, in <module>

    main()

  File "c:\Users\grafity\Desktop\main.py", line 31, in main

    products = get_products(search_url)

               ^^^^^^^^^^^^^^^^^^^^^^^^

  File "c:\Users\grafity\Desktop\main.py", line 14, in get_products

    response.raise_for_status()

  File "C:\Users\grafity\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 1021, in raise_for_status

    raise HTTPError(http_error_msg, response=self)

requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url:
https://www.amazon.ca/s?k=RTX+3070ti

Edited: I spent some time and somehow made it work but it is very inconsistent. Sometimes it parses the cards well, sometimes values are half Null and, generally, all of the values are Null. How can i make ,y program more consistent and relieble. Here is some sample output:

{"img": null, "name": null, "price": null, "url": null}, {"img": "https://m.media-amazon.com/images/I/71vWKkde2yL._AC_UY218_.jpg", "name": null, "price": null, "url": "/sspa/click?ie=UTF8&spc=MToyNjUzMzM1MzIwODAzNjE5OjE2OTQ1MzczOTE6c3BfYXRmOjMwMDAwMTUzMzIyNDgwMjo6MDo6&url=%2FPNY-GeForce-Uprising-Triple-Graphics%2Fdp%2FB0C1HVL3BD%2Fref%3Dsr_1_1_sspa%3Fkeywords%3DRTX%2B3070ti%26qid%3D1694537391%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1"}, {"img": "https://m.media-amazon.com/images/I/81d0pk3xOiS._AC_UY218_.jpg", "name": null, "price": 843.0, "url": "/MSI-Gaming-RTX-3070-Trio/dp/B096HJC18P/ref=sr_1_2?keywords=RTX+3070ti&qid=1694537391&sr=8-2"}

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-09-11): It means the server isn't available. Maybe you can repeat the request after a while.
- **[Mous](https://stackoverflow.com/users/16435355)** (2023-09-12): For more information, I'd recommend checking out [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).
- **[Mous](https://stackoverflow.com/users/16435355)** (2023-09-12): For more information, check out [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) on MDN.
- **me** (2023-09-12): they don't like bots. even if you don't get error, you'll just get captcha....you could give selenium a try though
