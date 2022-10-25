---
title: "Scraping nested items with Selenium and Python"
site: stackoverflow
question_id: 74192587
url: https://stackoverflow.com/q/74192587
asked: 2022-10-25T10:24:57Z
asked_by: "DaOP"
asked_by_url: https://stackoverflow.com/users/18333558
last_edited: 2022-10-25T10:52:50Z
last_editor: "baduker"
last_editor_url: https://stackoverflow.com/users/6106791
tags: [python-3.x, selenium, web-scraping, beautifulsoup, tiktok]
score: 1
views_at_snapshot: 357
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1d5a2625d045fcab3ee8288f7b881da7b98c16cf4e1d45efff9c4980c8c6b607
---

# Scraping nested items with Selenium and Python

Asked by [DaOP](https://stackoverflow.com/users/18333558) on Stack Overflow, <https://stackoverflow.com/q/74192587>, 2022-10-25, last edited 2022-10-25 by [baduker](https://stackoverflow.com/users/6106791). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

How can I access the content inside the highlighted class (image bellow)? I am trying to print all comments from a TikTok video ([url here][1]), but I haven't manage to do it. I have tried several different approaches (listed bellow), but they always retrieved empty variables. I tested:

With bs4:  
    
    url_ = urllib.request.urlopen(url)  
    content = url_.read()  
    soup = BeautifulSoup(content, 'lxml')
    # 1.
    containers = soup.find_all('p',{'data-e2e':'comment-level-1'})
    # or 2. (to access the container and then somehow access the sub-container)
    containers = soup.findAll('div',attrs={"class":"content-tiktok-1mf23fd-DivContentContainer e1g2efjf1"})

With Selenium:

    browser = webdriver.Chrome(executable_path=path, options=options)  
    browser.get(url)  
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
    comm = browser.find_elements_by_class_name("tiktok-q9aj5z-PCommentText e1g2efjf6")

I managed to make it work with Selenium using Xpath, but this thing changes among container to container, so it does not work because a have a lot of this "boxes".

This works with Selenium for only one comment box:

    browser = webdriver.Chrome(executable_path=path, options=options)  
    browser.get(url)  
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = browser.find_element_by_xpath('//*[@id="7156976296152449797"]/div[1]/p[1]')
    print(element.text)

[![enter image description here][2]][2]

  [1]: https://www.tiktok.com/@adhdvision/video/7156974534078385413?is_from_webapp=v1&item_id=7156974534078385413
  [2]: https://i.sstatic.net/OCGRM.png
