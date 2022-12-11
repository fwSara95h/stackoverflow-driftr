---
title: "while Web Scraping I collect All products list, problem is 'For loop doesn't execute properly to Extract individual product Elements like title, Etc.'"
site: stackoverflow
question_id: 74764616
url: https://stackoverflow.com/q/74764616
asked: 2022-12-11T21:19:53Z
asked_by: "SadiqHussain"
asked_by_url: https://stackoverflow.com/users/18836746
last_edited: never
tags: [python, selenium, for-loop, selenium-webdriver, web-scraping]
score: 1
views_at_snapshot: 390
answer_count: 1
accepted_answer_id: 74777214
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c46416f60bd46e4f3e7756035080e44cb446b09fd4be8ed6d517478a53fb63f1
---

# while Web Scraping I collect All products list, problem is 'For loop doesn't execute properly to Extract individual product Elements like title, Etc.'

Asked by [SadiqHussain](https://stackoverflow.com/users/18836746) on Stack Overflow, <https://stackoverflow.com/q/74764616>, 2022-12-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

### #  I am trying to extract Books data from Amazon.com. using Selenium + Python only.
the last part of  output is something like this::

```
`
{'book title: ': 'Explore Atoms and Molecules!: With 25 Great Projects', 'authors: ': 'Part of: Explore Your World (59 books)', 'rating: ': '', 'price: ': ''} #each 10+ times
.
.
.
{'book title: ': 'Patience is my Superpower: A Kid’s Book about Learning How to Wait (My Superpower Books)', 'authors: ': 'Book 7 of 7: My Superpower Books', 'rating: ': '', 'price: ': ''}
#and so on... till end
#due to restriction, cant paste whole result.. hope u got my point

`
```



when I run my program, in result I get repetition of first book's Elements for 1 page iteration, then for 2nd, 3rd page till last, i some elements of that pages are repeated each for 10+ times in a row, then displays another book for 10 times in a row. I tried simple for loop/ for loop with Range. both same issue, different result. such a weird behavior.. hehe

**from search-results pages, without going into each book's detail pages,** I am trying to extract each book's specific elements like it's title, price, rating, authors etc. ignoring its remaining elements. the way I am trying is:

first of all, I collect **results** list from search result. through 'resultsXpath', into a variable called results. **i then execute 2 'for loops', one outer Loop for pagination. and the 2nd as a nested for loop, for extracting result one by one.**

**now within this nested loop I am trying to get each result's Elements(not all only specific)**, I think the issue is with the loops. but how to solve it... I don't know. any help form your side would be highly appreciated. I am new to selenium.


thank you all. 
this is how I tried:

```

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://amazon.com")
driver.maximize_window()

# searching for Children books in search bar
driver.implicitly_wait(2)
searchBox = driver.find_element("id", "twotabsearchtextbox")
searchBox.send_keys("children Books")

# to click the search button
searchBtn = driver.find_element("id", "nav-search-submit-button")
searchBtn.click()

# collecting data of all listed books

booksList = []
resultsXpath = "//div[@data-component-type='s-search-result']"

# total pages to search = 7 so,

for i in range(1, 8):

    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, resultsXpath)))
    results = driver.find_elements(By.XPATH, resultsXpath)

    for result in results:
        title = result.find_element(By.XPATH, "//h2/a/span[@class='a-size-base-plus a-color-base a-text-normal']").text.strip()
        price = result.find_element(By.XPATH, "//span[@class='a-price']/span[@class='a-offscreen']").text
        rating = result.find_element(By.XPATH, "//span[@class='a-declarative']/a[@role='button']/i/span").text
        auth = result.find_element(By.XPATH,"//h2/following-sibling::div[@class='a-row a-size-base a-color-secondary']").text.strip()
        # title = aatag.text.strip()
        booksList.append({'book title: ': title, 'authors: ': auth, 'rating: ': rating, 'price: ': price})

        print()

    try:
        nextBtn = driver.find_element("xpath",
                                      "//a[@class=\"s-pagination-item s-pagination-next s-pagination-button s-pagination-separator\"]")
        nextBtn.click()
    except NoSuchElementException:
        pass

for book in booksList:
    print(book)

print()
print(len(booksList))
driver.quit()`


```
