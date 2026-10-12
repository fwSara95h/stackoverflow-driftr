# Code from my Stack Overflow answer https://stackoverflow.com/a/74777214 (posted 2022-12-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for result in results:
    dasin = result.get_attribute('data-asin')
    if dasin in scrapedIds:
            continue
    scrapedIds.append(dasin)
    ## REST OF CODE ##

# --- block 2 ---
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

# --- block 3 ---
    nextBtn.click()
except NoSuchElementException:
    break

# --- block 4 ---
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
