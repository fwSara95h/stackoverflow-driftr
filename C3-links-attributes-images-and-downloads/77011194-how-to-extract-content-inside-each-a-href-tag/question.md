---
title: "How to Extract Content Inside Each <a href> Tag?"
site: stackoverflow
question_id: 77011194
url: https://stackoverflow.com/q/77011194
asked: 2023-08-30T19:58:38Z
asked_by: "Alex VIJU"
asked_by_url: https://stackoverflow.com/users/11829916
last_edited: 2023-08-31T07:39:14Z
tags: [python, web-scraping, beautifulsoup, html-parsing]
score: -2
views_at_snapshot: 97
answer_count: 1
accepted_answer_id: 77034640
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bec701bcd895b21bfc396126b8051a45f873a627f0fc3d050b2e58ff8c444582
---

# How to Extract Content Inside Each <a href> Tag?

Asked by [Alex VIJU](https://stackoverflow.com/users/11829916) on Stack Overflow, <https://stackoverflow.com/q/77011194>, 2023-08-30, last edited 2023-08-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working on a project that involves extracting some data from the website. Specifically, I am interested in pulling out the name of each category along with its description.

I have considered using web scraping libraries like BeautifulSoup in Python, but I am not sure how to navigate through each category link to get the required information.
  
The website has multiple category names listed, and each category has its own page with parameters and descriptions.
I am not sure how to programmatically "click" on each link to scrape the data.

    import requests
    from bs4 import BeautifulSoup
    URL = "https://docs.derivative.ca/Category:CHOPs"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="mw-pages")
    print(results.prettify())
    chop_elements = results.find_all("div", class_="mw-content-ltr")
    for chop_element in chop_elements:
        print(chop_element, end="\n"*2)
  
    <li><a href="/Analyze_CHOP" title="Analyze CHOP">Analyze CHOP</a></li>
    <li><a href="/Angle_CHOP" title="Angle CHOP">Angle CHOP</a></li>
    <li><a href="/Attribute_CHOP" title="Attribute CHOP">Attribute CHOP</a></li>
    <li><a href="/Audio_Band_EQ_CHOP" title="Audio Band EQ CHOP">Audio Band EQ CHOP</a></li>


Website is [https://docs.derivative.ca/Category:CHOPs][1]

What is the best way to navigate through each category link and extract the required data?
However, I'm not entirely sure what I'm doing, and I'm uncertain if I've inspected the HTML structure correctly. I'm looking for guidance on how to approach this problem.


  [1]: https://docs.derivative.ca/Category:CHOPs
