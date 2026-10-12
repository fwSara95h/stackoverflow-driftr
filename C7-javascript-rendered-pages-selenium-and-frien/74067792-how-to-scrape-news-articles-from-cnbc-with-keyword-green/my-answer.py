# Code from my Stack Overflow answer https://stackoverflow.com/a/74075841 (posted 2022-10-15), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# dataReqUrl contains the copied Request URL
dataReq = requests.get(dataReqUrl)
for r in dataReq.json()['results']: print(r['cn:title'])

# --- block 2 ---
# import urllib.parse

# find link to js file with api key
jsLinks = bsobj.select('link[href][rel="preload"]')
jUrl = [m.get('href') for m in jsLinks if 'main' in m.get('href')][0]

jRes = requests.get(jUrl) # request js file api key

# get api key from javascript
qKey = jRes.text.replace(' ', '').split(
    'QUERYLY_KEY:'
)[-1].split(',')[0].replace('"', '').strip()

# form url
qParams = {
    'queryly_key': qKey,
    'query': search_for, # = 'green hydrogen'
    'batchsize': 10 # can go up to 100 apparently
}
qUrlParams = urllib.parse.urlencode(qParams, quote_via=urllib.parse.quote)
dataReqUrl = f'https://api.queryly.com/cnbc/json.aspx?{qUrlParams}'

# --- block 3 ---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# define chromeDriver_path <-- where you saved 'chromedriver.exe'
cnbc_url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"
driver = webdriver.Chrome(chromeDriver_path)
driver.get(cnbc_url)

ctSelector = 'span.Card-title'
WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ctSelector)))
cardTitles = driver.find_elements(By.CSS_SELECTOR, ctSelector)

cardTitles_text = [ct.get_attribute('innerText') for ct in cardTitles] 
for c in cardTitles_text: print(c)
