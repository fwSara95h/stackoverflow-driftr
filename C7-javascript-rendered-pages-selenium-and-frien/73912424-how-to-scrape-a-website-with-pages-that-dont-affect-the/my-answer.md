---
title: "how to scrape a website with pages that dont affect the url"
site: stackoverflow
question_id: 73912424
answer_id: 73914652
url: https://stackoverflow.com/a/73914652
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-30T22:56:22Z
last_edited: 2022-10-01T20:22:38Z
revisions: 5
revision_history: https://stackoverflow.com/posts/73914652/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0); the revisions listed under edited_by_others are those users' work under CC BY-SA 4.0
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bed89f4975426c11e6ed2708defc5970542bff56909442f9f65bcf199c4bcd64
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
edited_by_others:
  - "Nuspli (https://stackoverflow.com/users/19232040), revision 5, 2022-10-01, CC BY-SA 4.0 — fixed logic and functionality, also added some thoughts"
---

# My answer — 2022-09-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73914652>, 2022-09-30, last edited 2022-10-01; **accepted**; score 1. Text as retrieved 2026-10-12. Later revisions by other users are listed in the front matter.

Since the 'next' and page button are not hyperlinked and the site doesn't seem to be loading the data via any easy-to-find APIs, I expect it would take a horribly convoluted process of requesting and parsing scripts to retrieve this one date from the last page.

Instead, you could use selenium to click the last page button [(`2`) in this case] and then get the last date. (If you haven't ever used selenium before, I found [this][1] to a be a very helpful starting point.) 

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    chromeDriver_path = 'chromedriver.exe'
    # I just copied the exe file to the same folder as this py file
    driver = webdriver.Chrome(chromeDriver_path)

    tag = "L9YJUPY22"  # your player tag without '#'

    driver.get('https://www.clashofstats.com/players/' + tag + '/history/log')

    start_dates = driver.find_elements(By.CSS_SELECTOR, 'span.start.date')
    end_dates = driver.find_elements(By.CSS_SELECTOR, 'span.end.date')
    page_btns = driver.find_elements(By.CSS_SELECTOR, 'button.v-pagination__item')

    try:
        clan = driver.find_element(By.CSS_SELECTOR, 'div.v-list-item__title.text--secondary.font-italic').get_attribute(
        'innerText')
    except:
        clan = "something else"

    if start_dates[0].get_attribute('innerText') == end_dates[0].get_attribute('innerText') or clan == "Not in any Clans":
        # basically the inactivity time can't really be seen from just the clan, so it only works on
        # players that don't have a clan. this is sometimes displayed weird by the website, thus this logic
        last_played = start_dates[1].get_attribute('innerText')
        # only start date is available when turning inactive
    else:
        last_played = end_dates[0].get_attribute('innerText')  # in a normal case this is "today"

    # see if there are more pages
    if len(page_btns) > 0 and len(end_dates) > 0:
        page_btns[-1].click()  # click the last page_btn
        start_dates = driver.find_elements(By.CSS_SELECTOR, 'span.start.date')  # update start dates

    first_played = start_dates[-1].get_attribute('innerText')  # get last start date

    print(f"First time played| {first_played}")
    print(f"Last  time played| {last_played}")

    driver.close()  # else the window stays open and your program keeps running

Output:

    First time played| Sep 8, 2020
    Last  time played| Oct 1, 2022
    


This should work standalone for any number of pages.


  [1]: https://www.scrapingbee.com/blog/selenium-python/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): I am getting an error:  AttributeError: 'WebDriver' object has no attribute 'find_elements_by_css_selector'            As I was trying to find some solutions yesterday I faced the same problem... is something wrong with my selenium version?
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): pycharm only gives the methods "find_element(self, by, value)" and "find_element(self, by, value)"
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): I tried using : end_dates = driverC.find_elements("css_selector", 'span.end.date') but only got another error : selenium.common.exceptions.InvalidArgumentException: Message: invalid argument: invalid locator
- **me** (2022-10-01): Sorry, I should probably stop doing it like that - some versions don't recognize it [I think mine is not updated yet maybe so it still works]
- **me** (2022-10-01): Try adding `from selenium.webdriver.common.by import By` to your imports, and then change to `driverC.find_elements(By.CSS_SELECTOR, 'span.end.date')`
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): Thanks for your quick response, all fine now with selenium. However, first time played as output doesnt match whats on the website and the date still comes from the first page
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): So I found the problem, first off all the print for First time played should also be at the bottom in case it gets updated and secondly replace span.end.date in line 24 with span.start.date and also change the variable name
- **me** (2022-10-01): @Nuspli sorry again, I mixed them up - and didn't notice that there were 2 different date classes. I'm glad you figured it out. ( you don't need it anymore, but I've edited my answer. again 😅).
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): Sorry but you still got the dates wrong, it's a little complicated for me too. Last time played is definetely today, I also got to work out something there as the latest log will always show the current date...
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-10-01): Ok finally found a working solution, is there a way for me to edit your answer or should I make my own ?
- **me** (2022-10-01): There should be `Share` , `Edit` ,  `Follow` and `Flag` buttons [that look like this](https://i.sstatic.net/uWY7I.jpg) just above these comments, but if you don't see the edit button (or even if you do, but just want to post separately) I'd very much appreciate if you edited in/ added the final solution!
