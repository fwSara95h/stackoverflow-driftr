---
title: "Find pattern in HTML elements with Selenium/BeautifulSoup"
site: stackoverflow
question_id: 74709027
url: https://stackoverflow.com/q/74709027
asked: 2022-12-06T21:05:11Z
asked_by: "bs2012"
asked_by_url: https://stackoverflow.com/users/20233877
last_edited: 2022-12-07T01:05:42Z
tags: [python, html, selenium, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 112
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b49e51b507f6c903adccd75f01ad15c675c3159f05aceb96a4dec604494bdaab
---

# Find pattern in HTML elements with Selenium/BeautifulSoup

Asked by [bs2012](https://stackoverflow.com/users/20233877) on Stack Overflow, <https://stackoverflow.com/q/74709027>, 2022-12-06, last edited 2022-12-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this html that I am trying to scrape from surfing heats
```
     <div class="event-round">
           <div id="heat-85940" class="new-heat  new-heat--status-completed new-heat--athletes-4">
           <div id="heat-85941" class="new-heat  new-heat--status-completed new-heat--athletes-4">
           <div id="heat-85942" class="new-heat  new-heat--status-completed new-heat--athletes-4">
           <div id="heat-85943" class="new-heat  new-heat--status-completed new-heat--athletes-4">
     <div>
````

I have a loop created to scrape the heats on each page, but because the heat ID is changing on each page (ie not always starting at 85940), I can only get 1 page worth without manually changing the range i loop.

For one page, my code looks like this:

```
heat_count = len(driver.find_elements(By.CLASS_NAME, 'new-heat-hd-name').text)

for h in range(heat_count):
    for i in range(4):
        name = driver.find_element(By.XPATH, f'//*[@id="heat-8594{h}"]/div/div[2]/div[{i + 1}]/div[1]/div[1]/div/div[2]/div[1]/span').text
```

I'm looking for a way to search within the html to find `heat-85940` and then start from there instead of manually finding it for each page.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-06): Can you include a url or more examples of the elements you want to scrape from different pages?
- **[bs2012](https://stackoverflow.com/users/20233877)** (2022-12-07): @Driftr95 added html example
- **me** (2022-12-07): @bs2012- I meant enough to test some code on, with the nested divs and spans, and so that I could see how  `new-heat-hd-name`  class relates to the `heat-` ids.... anyway, I've posted something that *might* work - I couldn't test it, so please let me know if it works
- **me** (2022-12-07): Btw, can you really apply `.text` to multiple elements at once like you're doing in the `heat_count` line?
