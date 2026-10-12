# Code from my Stack Overflow answer https://stackoverflow.com/a/74948927 (posted 2022-12-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
### full version at https://pastebin.com/tgC4EpGZ
## YOU MUST DOWNLOAD CHROMEDRIVER.EXE FOR THIS ##
## https://chromedriver.chromium.org/downloads ##

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapeGmailDotTrix(username: str, wait_start=10, wait_op=200):
    driver = webdriver.Chrome()
    driver.get('https://gmail.inputekno.com/')

    WebDriverWait(driver, wait_start).until(
        EC.visibility_of_element_located((
            By.XPATH, '//input[@id="username"][@type="text"]')))

    driver.find_element(
        By.XPATH, '//input[@id="username"][@type="text"]'
    ).send_keys(str(username))

    WebDriverWait(driver, wait_op).until(
        EC.text_to_be_present_in_element_value(
            (By.XPATH, '//textarea[@id="emails"]'),
            '.'.join(str(username))))

    return [em.strip() for em in driver.find_element(
        By.XPATH, '//textarea[@id="emails"]'
    ).get_attribute('value').splitlines()]

# --- block 2 ---
def gmailTrix_gen(uname:str):
    if len(uname) > 1: 
        head, tail = uname[0], uname[1:]
        for item in gmailTrix_gen(tail):
            yield head + item
            yield head + '.' + item
    else: yield uname

def gmailTrix_list(username:str):
    return [f'{gu}@gmail.com' for gu in gmailTrix_gen(username)]

# --- block 3 ---
> ['rand@gmail.com', 'r.and@gmail.com', 'ra.nd@gmail.com', 'r.a.nd@gmail.com', 
>  'ran.d@gmail.com', 'r.an.d@gmail.com', 'ra.n.d@gmail.com', 'r.a.n.d@gmail.com']
>
