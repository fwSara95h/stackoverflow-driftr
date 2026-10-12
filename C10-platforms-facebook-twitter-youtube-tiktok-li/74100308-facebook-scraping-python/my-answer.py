# Code from my Stack Overflow answer https://stackoverflow.com/a/74105681 (posted 2022-10-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def linkToSoup_selenium(l, ecx=None):
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        # I copy chromedriver.exe to every folder with py file that will need to scrape with selenium

        driver.get(l)
        if ecx:
            WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, ecx)))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        return lSoup
    except Exception as e:
        print(e)
        return None

# --- block 2 ---
soup = linkToSoup_selenium(
    'https://www.facebook.com/KNOW-MORE-training-center-111698018315706/?ref=page_internal', 
    '//h2//span//*[contains(text(),"Intro")]'
)

# --- block 3 ---
# import re
a = soup.find('div', attrs={"data-pagelet": "ProfileTilesFeed_0"}).find(
   lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)).text)
).text
print(a)

# --- block 4 ---
# import re
if soup:
   introSection = soup.find('div', attrs={"data-pagelet": "ProfileTilesFeed_0"}) 
   if introSection:
      emailEl = introSection.find(
         lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)).text)
      )
      if emailEl:
         print(emailEl.text)
      else: print('!could not find any span tag with email within section!')
   else: print('!could not find intro section!')
else: print('!could not extract!')

# --- block 5 ---
# import re

#if soup:
h2span = [s for s in soup.select('h2 span') if 'Intro' in s.text]
if len(h2span) > 0:
    introSection = [
        p for p in h2span[0].parents if p.name == 'div' and
        p.get('class') and len(p.get('class')) == 1
    ]
    if len(introSection) > 0:
        # as before, but introSection[0] because list
        emailEl = introSection[0].find(
            lambda l: l.name == 'span' and re.search('\S+@\S+', l.text)
        )
        if emailEl:
            print(emailEl.text)
        else: print('could not find any span tag with email within section')
    else: print('could not find intro section in h2span ancestors')
else:  print('found no span with h2 ancestor')
