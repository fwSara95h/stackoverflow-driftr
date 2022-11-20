---
title: "Crawl multiple pages with python but other pages show same results as first page"
site: stackoverflow
question_id: 74505539
url: https://stackoverflow.com/q/74505539
asked: 2022-11-20T03:56:38Z
asked_by: "Duchero Nguyên"
asked_by_url: https://stackoverflow.com/users/13126111
last_edited: 2022-11-20T08:51:32Z
last_editor: "Barry the Platipus"
last_editor_url: https://stackoverflow.com/users/19475185
tags: [python-3.x, web-scraping, beautifulsoup, web-crawler]
score: 0
views_at_snapshot: 573
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2320632551457e3f1a3084dcd7e3c9d11f9b308b1fbdc77efa699657c44eedfd
---

# Crawl multiple pages with python but other pages show same results as first page

Asked by [Duchero Nguyên](https://stackoverflow.com/users/13126111) on Stack Overflow, <https://stackoverflow.com/q/74505539>, 2022-11-20, last edited 2022-11-20 by [Barry the Platipus](https://stackoverflow.com/users/19475185). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I try to crawl data by bs4. For each page, I want to take all product id's, it's ok when I take data from first page, but starting with page 2 it always show product id's from first page. Here is my code (although I changed page = 5):

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen('https://tiki.vn/lam-sach-da-mat/c11232?sort=top_seller%3Fpage%3D5&page=5')
    bs = BeautifulSoup(html, 'html.parser') 
    
    result =bs.find_all(lambda tag: tag.get('class') == ['product-item'])

Here is the [result of 5th page in my code](https://i.sstatic.net/eEclc.png)

I want to take product-id of 5th page as [this](https://i.sstatic.net/0nS1Q.png)


I want to get product-id of 5th page but don't understand why my code still show result of first page.
