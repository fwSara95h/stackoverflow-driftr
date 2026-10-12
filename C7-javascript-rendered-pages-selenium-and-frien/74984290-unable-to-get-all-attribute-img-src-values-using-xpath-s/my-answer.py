# Code from my Stack Overflow answer https://stackoverflow.com/a/74988832 (posted 2023-01-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
xpBanners = '//div[contains(@id,"dismissible")]/ytd-thumbnail/a'
## WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpBanners)))
## scroll to load all Banners (will explain below)

Banners_imgs = driver.find_elements_by_xpath(f'{xpBanners}//img')
Banners_src = [b.get_attribute('src') for b in Banners_imgs]

# --- block 2 ---
> Banners_src = [] 
> for element in Banners:
>     Banners_src.append(element.find_element_by_xpath('.//img').get_attribute('src'))
>

# --- block 3 ---
# import time
scrollCt = 10 # 5 should be enough, but just in case...
scrollWait = 2 # in seconds - adjust according to loading speed
xpBanner = '//div[contains(@id,"dismissible")]/ytd-thumbnail/a'

## wait to load... as necessary
for x in range(scrollCt):
    lastBanner = driver.find_elements_by_xpath(xpBanner)[-1]
    driver.execute_script('arguments[0].scrollIntoView(false);', lastBanner)
    time.sleep(scrollWait)

# --- block 4 ---
for x in range(scrollCt):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(scrollWait)

# --- block 5 ---
# import time
# from selenium.webdriver.common.keys import Keys

pgCt = 10 # adjust according to your browser (mine needs 7 - used 10 just in case)
scrollCt = 10 # 5 should be enough, but just in case...
scrollWait = 2 # in seconds - adjust according to loading speed

for x in range(scrollCt):
    driverD.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
    if x%pgCt == 0: time.sleep(scrollWait)
