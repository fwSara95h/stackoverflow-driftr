# Code from my Stack Overflow answer https://stackoverflow.com/a/74217161 (posted 2022-10-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
soup = linkToSoup_selenium('https://opensea.io/rankings?sortBy=total_volume')
values = soup.find_all(
            lambda l: l.name == 'a' and
            l.get('href') is not None and
            '/collection/' in l.get('href')
        )
# OR
# values = [a for a in soup.select('a') if a.get('href') and '/collection/' in a.get('href')]

# --- block 2 ---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import json

driver = webdriver.Chrome('chromedriver.exe')
url = f'https://opensea.io/rankings?sortBy=total_volume'
driver.get(url)
driver.maximize_window()
scrollCt = 0
rows = []

maxScrols = 1000  # adjust as preferred
while scrollCt < maxScrols:
    time.sleep(0.3)  # adjust as necessary - I seem to need  >0.25s
    aro = driver.find_elements_by_css_selector(
        'a[role="row"][overflow="hidden"][href*="/collection/"]')
    aro = [(
        a.get_attribute('href'),
        a.find_element_by_xpath('../..')  # parent's parent
    ) for a in aro]

    aroFil = [a for a in aro if a[0] not in [h['link'] for h in rows]]
    aroFil = [{   
        'outerHTML': [a[1].get_attribute('outerHTML')], # for BeatifulSoup
        'innerText': a[1].get_attribute('innerText').strip(),
        'link': a[0]
    } for a in aroFil]
    rows += aroFil

    print(f'[{scrollCt}] found {len(aro)}, filtered down to {len(aroFil)} rows [at {len(rows)} total]')
    if aroFil == []:
        # break # if you don't want to go to next page
        try:
            driver.find_element_by_xpath('//i[@value="arrow_forward_ios"]/..').click()
        except Exception as e:
            print('failed to go to next page', str(e))
            break

    scrollCt += 1
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)


# if you want to extract more with BeautifulSoup
for i, r in enumerate(rows):
    rSoup = BeautifulSoup(r['outerHTML'][0].encode('utf-8'), 'html5lib')

    rows[i]['bs4Text'] = rSoup.get_text(strip=True)
    ###### EXTRACT INFO AS NEEDED ######

    del rows[i]['html']  # if you don't need it anymore

# with open('x.json', 'w') as f: json.dump(rows, f, indent=4) # save json file 

driver.quit()
