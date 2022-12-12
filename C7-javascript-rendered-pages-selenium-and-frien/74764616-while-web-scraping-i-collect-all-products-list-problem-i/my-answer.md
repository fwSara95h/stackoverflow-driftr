---
title: "while Web Scraping I collect All products list, problem is 'For loop doesn't execute properly to Extract individual product Elements like title, Etc.'"
site: stackoverflow
question_id: 74764616
answer_id: 74777214
url: https://stackoverflow.com/a/74777214
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-12T20:56:02Z
last_edited: 2022-12-13T14:46:05Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74777214/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 002fb7d9674a632f64a83d6e67b591098fb0805d6c42c09d9cd18c8b40d6595e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74777214>, 2022-12-12, last edited 2022-12-13; **accepted**; score 0. Text as retrieved 2026-10-12.

For avoiding duplicates in general, you can use the `data-asin` attribute which should be unique to each `result`. First initiate a list of added IDs **before** the `for i in range...` loop [like **`scrapedIds = []`**] and then, inside the `for result...` loop, skip results if the ID has already been added

```python
    for result in results:
        dasin = result.get_attribute('data-asin')
        if dasin in scrapedIds:
                continue
        scrapedIds.append(dasin)
        ## REST OF CODE ##
``` 

---

As for not getting anything but the first result in each page, I don't know the reason for this, and what I'm suggesting is probably more of a work-around than anything, but I came across a [similar duplicates issue](https://stackoverflow.com/a/74631249/6146136) with selenium before, and it you might get around it with [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start):

```python
# from bs4 import BeautifulSoup


# scrapedIds = []
# for i in range...

    for result in results:
        print('', end=f'\rpage {i} of 7 - {len(results)} results left')
        dasin = result.get_attribute('data-asin')
        if dasin in scrapedIds: continue
        scrapedIds.append(dasin)
        rSoup = BeautifulSoup(result.get_attribute('outerHTML').encode('utf-8'), 'html.parser')
        title = rSoup.select_one("h2 > a > span[class='a-size-base-plus a-color-base a-text-normal']")
        price = rSoup.select_one("span[class='a-price'] > span[class='a-offscreen']")
        rating = rSoup.select_one("span[class='a-declarative'] > a[role='button'] > i > span")
        auth = rSoup.select_one("h2 ~ div[class='a-row a-size-base a-color-secondary']")

        booksList.append({k: v if k in ['pg', 'asin'] else (
            '' if v is None else v.get_text(' ').strip()
        ) for k, v in {
            'pg': i, 'asin': dasin, ## remove if you don't want
            'book title': title, 'authors': auth, 'rating': rating, 'price': price
        }.items()})
    ## REST OF YOUR CODE ##
```

---

Btw, why don't you use 

```python
        nextBtn.click()
    except NoSuchElementException:
        break 
```
instead of `except NoSuchElementException: pass`? That way, the code won't be unnecessarily scraping the last page multiple times...

---

With the above changes, I got 115 unique entries and the data collected in `booksList` looked like:

```lang-none
|   pg | asin       | book title                                                                                                           | authors                                                     | rating             | price   |
|-----:|:-----------|:---------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:-------------------|:--------|
|    1 | 9388369882 | My First Complete Learning Library: Boxset of 20 Board Books for Kids                                                | by  Wonder House Books                                      | 4.7 out of 5 stars | $26.88  |
|    1 | 031077702X | I'm So Glad You Were Born: Celebrating Who You Are                                                                   | by  Ainsley Earhardt    and  Kim Barnes                     | 4.9 out of 5 stars | $14.16  |
|    1 | 9389432006 | Best of Children s Classics (Set of 5 Books)                                                                         | by  Various                                                 | 4.6 out of 5 stars | $22.49  |
|    1 | 0545261244 | The Wonky Donkey                                                                                                     | Part of: Wonky Donkey (4 books)                             | 4.8 out of 5 stars | $5.28   |
|    1 | 0375832416 | Dancing Dinos Go to School (Step into Reading)                                                                       | Part of: Step into Reading (233 books)                      | 4.8 out of 5 stars | $3.99   |
|    1 | 0062075535 | The Berenstain Bears' Night Before Christmas: A Christmas Holiday Book for Kids                                      | Part of: Berenstain Bears (90 books)                        | 4.9 out of 5 stars | $4.99   |
|    1 | 054521579X | Clifford's Good Deeds (Classic Storybook)                                                                            | Part of: Clifford (37 books)                                | 4.8 out of 5 stars | $4.99   |
|    1 | 0060254920 | Where the Wild Things Are                                                                                            | Part of: Caldecott Collection (8 books)                     | 4.9 out of 5 stars | $13.20  |
|    1 | 0736431411 | The Never Girls Collection #1 (Disney: The Never Girls): Books 1-4                                                   | Book 1 of 3: The Never Girls Collection                     | 4.8 out of 5 stars | $14.39  |
|    1 | 1797213873 | Construction Site: Farming Strong, All Year Long (Goodnight, Goodnight, Construc)                                    | by  Sherri Duskey Rinker    and  AG Ford                    | 4.7 out of 5 stars | $14.99  |
|    1 | 1665920580 | Angelina Ballerina 5-Minute Stories                                                                                  | Part of: Angelina Ballerina (42 books)                      | 4.5 out of 5 stars | $11.00  |
|    1 | 1452170339 | Tiny T. Rex and the Impossible Hug                                                                                   | Book 1 of 4: Tiny T. Rex                                    | 4.8 out of 5 stars | $9.26   |
|    2 | 006267529X | Pete the Cat Goes Camping (I Can Read Level 1)                                                                       | Part of: I Can Read Level 1 (375 books)                     | 4.8 out of 5 stars | $4.74   |
|    3 | 1510756299 | World Cup Women: Megan, Alex, and the Team USA Soccer Champs                                                         | by  Meg Walters    and  Nikkolas Smith                      | 4.9 out of 5 stars | $16.99  |
|    3 | 1496454839 | How Much Is a Little Boy Worth?                                                                                      | by  Rachael Denhollander   ,  Jacob Denhollander , et al.   | 4.8 out of 5 stars | $13.49  |
|    3 | 0312527594 | See, Touch, Feel: A First Sensory Book                                                                               | by  Roger Priddy                                            | 4.8 out of 5 stars | $7.58   |
|    4 | 1680105469 | Grandma Loves You!                                                                                                   | by  Danielle McLean    and  Alison Edgson                   | 4.9 out of 5 stars | $6.49   |
|    4 | 1452111731 | Goodnight, Goodnight Construction Site (Board Book for Toddlers, Children's Board Book)                              | Part of: Goodnight, Goodnight, Construction Site (6 books)  | 4.9 out of 5 stars | $4.28   |
|    5 | 1644725088 | Best Hidden Pictures Puzzles EVER: The Ultimate Collection of America's Favorite Puzzle (Highlights Hidden Pictures) | Part of: Highlights Hidden Pictures (17 books)              | 4.7 out of 5 stars | $7.29   |
|    6 | 1664350292 | Early Learning Library: 10 Books! (My First Home Learning)                                                           | by  Tiger Tales                                             | nan                | $19.35  |
|    6 | 0823425479 | The Story of Hanukkah                                                                                                | by  David A. Adler    and  Jill Weber                       | 4.7 out of 5 stars | $7.99   |
|    7 | 1728280117 | TummyTime Fold-Out Book Set: 4 high-contrast books to help develop strength and eye coordination for your baby       | by  duopress labs                                           | nan                | $34.84  |
|    7 | 0593406265 | Little Black Boy: Oh, the Things You Will Do!                                                                        | by  Kirby Howell-Baptiste   ,  Larry C. Fields III , et al. | 4.3 out of 5 stars | $17.94  |
```

[ The above was processed with [pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and is the output printed from **`print(pandas.DataFrame(booksList).loc[::5].to_markdown(index=False))`** (only every 5th row) ]

---
---

**EDIT:** For a selenium-only approach, try

```python
scrapedIds = []
for i in range(1, 8):
    WebDriverWait(driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH, resultsXpath)))
    resLen = len(driver.find_elements(By.XPATH, resultsXpath))

    for ri in range(1, resLen + 1):
        print('', end=f'\rpage {i} of 7 - result {ri} of {resLen}')
        dasin = driver.find_element(By.XPATH, f"{resultsXpath}[{ri}]").get_attribute('data-asin')
        if dasin in scrapedIds: continue
        scrapedIds.append(dasin)

        title = driver.find_elements(By.XPATH, f"{resultsXpath}[{ri}]//h2/a/span[@class='a-size-base-plus a-color-base a-text-normal']")
        price = driver.find_elements(By.XPATH, f"{resultsXpath}[{ri}]//span[@class='a-price']/span[@class='a-offscreen']")
        rating = driver.find_elements(By.XPATH, f"{resultsXpath}[{ri}]//span[@class='a-declarative']/a[@role='button']/i/span")
        auth = driver.find_elements(By.XPATH, f"{resultsXpath}[{ri}]//h2/following-sibling::div[@class='a-row a-size-base a-color-secondary']")

        booksList.append({k: v if k in ['pg', 'asin'] else (
            v[0].get_attribute('innerText').strip() if v else ''
        ) for k, v in {
            'pg': i, 'asin': dasin, ## remove if you don't want
            'book title': title, 'authors': auth, 'rating': rating, 'price': price
        }.items()})
print()
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[SadiqHussain](https://stackoverflow.com/users/18836746)** (2022-12-13): if u can give it a try with Selenium also, that would be very helpful.  i used Bs4 for the same problem. i got the required output. but i was trying to do this task with Selenium only. btw  thank you for your recommendation of using break keyword. i never noticed this thing.
- **[SadiqHussain](https://stackoverflow.com/users/18836746)** (2022-12-13): also plz have a look at the Xpaths, i have used. the Xpaths of price and rating are not extracting their respective elements data. returns empty strings ' '. although seems right to me... thank you for Your precious time and help....
- **me** (2022-12-13): @SadiqHussain I *might* have stumbled on a solution with selenium - to use `.find_element` on `driver` with full XPath [starting with an indexed `resultsXpath`] instead of on `result` with partial XPath [**see my added edit** - btw, I used `.find_elements` bc `.find_element` will raise error if the element is missing and not new listings might not have ratings]
- **me** (2022-12-13): @SadiqHussainI also think that your XPaths seem right, just try `.get_attribute('innerText')` instead of `.text` [but remember that you have to check if the element was actually found before trying to get an attribute/property - that's what the `if v else ''` part is for]
- **[SadiqHussain](https://stackoverflow.com/users/18836746)** (2022-12-13): Thank You Sir, i tried it, its working perfectly. but i am little confused in the Logic Inside that **booksList.append()** method. `{ everything here }.items()} ` ..... can You Please explain it little More. so that I Can **Understand the Concept** . and may be able to Use similar logics in future. Thank You .
- **me** (2022-12-13): @SadiqHussain glad it worked! [`.items()`](https://www.programiz.com/python-programming/methods/dictionary/items) returns a list of key-value pairs (`k, v`) from the  `{'pg': i, 'asin': ...}` dict, so it's just building a new dictionary (using [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension), which is like [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) ) based on those - if `v` is empty, it just set an empty str `''` as the value but if there are any elements if v, it gets the `innerText` of the 1st element
- **[SadiqHussain](https://stackoverflow.com/users/18836746)** (2022-12-13): Yes it worked, this was very helpful discussion... I really appreciate ur  help.
- **me** (2022-12-13): @SadiqHussain that's great! If my answer resolved your issue satisfactorily, please mark it [as accepted](https://meta.stackexchange.com/questions/5234/how-does-accepting-an-answer-work) by clicking the "checkmark" button to the the top-left of it.
