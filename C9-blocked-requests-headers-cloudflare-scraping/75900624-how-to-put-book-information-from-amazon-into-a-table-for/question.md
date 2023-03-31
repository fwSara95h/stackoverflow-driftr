---
title: "How to put book information from amazon into a table form?"
site: stackoverflow
question_id: 75900624
url: https://stackoverflow.com/q/75900624
asked: 2023-03-31T16:07:29Z
asked_by: "Akira"
asked_by_url: https://stackoverflow.com/users/7357673
last_edited: 2023-03-31T16:15:32Z
tags: [html, css, python-3.x, beautifulsoup, css-selectors]
score: 0
views_at_snapshot: 64
answer_count: 1
accepted_answer_id: 75903974
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0459a1792332b25179eaaffb6599f70c39fc3468e94b2916e76a61349f2977f0
---

# How to put book information from amazon into a table form?

Asked by [Akira](https://stackoverflow.com/users/7357673) on Stack Overflow, <https://stackoverflow.com/q/75900624>, 2023-03-31, last edited 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have an amazon [link](https://www.amazon.com/Functional-Analysis-Dzung-Ha/dp/0971576610), i.e.,
[![enter image description here][1]][1]

I'm able to extract `Product details` from the HTML with `soup.select("#detailBullets_feature_div .a-unordered-list:first-child")`, i.e.,

    <ul class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list">
    <li><span class="a-list-item"> <span class="a-text-bold">Publisher : </span> <span>Matrix Editions (January 1, 2007)</span> </span></li>
    <li><span class="a-list-item"> <span class="a-text-bold">Language : </span> <span>English</span> </span></li>
    <li><span class="a-list-item"> <span class="a-text-bold">Hardcover : </span> <span>640 pages</span> </span></li>
    <li><span class="a-list-item"> <span class="a-text-bold">ISBN-10 : </span> <span>0971576610</span> </span></li>
    <li><span class="a-list-item"> <span class="a-text-bold">ISBN-13 : </span> <span>978-0971576612</span> </span></li>
    <li><span class="a-list-item"> <span class="a-text-bold">Item Weight : </span> <span>2.3 pounds</span> </span></li>
    </ul>



Could you explain how to put above data in a tabular form? My expected result is
[![enter image description here][2]][2]

    from bs4 import BeautifulSoup
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    
    link = 'https://www.amazon.com/Functional-Analysis-Dzung-Ha/dp/0971576610'
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup.select("#detailBullets_feature_div .a-unordered-list:first-child")



  [1]: https://i.sstatic.net/aZOFR.png
  [2]: https://i.sstatic.net/sowJm.png
