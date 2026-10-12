# Code from my Stack Overflow answer https://stackoverflow.com/a/74589557 (posted 2022-11-27), extracted verbatim; may need the question's context to run.
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

## [ BEFORE BeautifulSoup ] ##

maxWait = 10 # adjust as preferred
wait =  WebDriverWait(driver, maxWait)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'js-listing-item')))

## [ NOW YOU CAN PARSE WITH BeautifulSoup ] ##
