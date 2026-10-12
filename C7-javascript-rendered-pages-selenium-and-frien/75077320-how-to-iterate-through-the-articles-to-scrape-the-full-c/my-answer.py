# Code from my Stack Overflow answer https://stackoverflow.com/a/75079960 (posted 2023-01-11), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# while....[ load more ]
article_links = driver.find_elements(By.CSS_SELECTOR, "div.row div.row h5>a[href]")
article_links = list(set([l.get_attribute('href') for l in article_links])) ## set <-> unique

for url in article_links:
    driver.get(url)
    ### SCRAPE ARTICLE ###

# --- block 2 ---
>         driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-content > div.wrapper.clearfix > div.col-a.pull-left > section.widget-area-2.pull-right > div > div > div.row > div > button'))))
>
