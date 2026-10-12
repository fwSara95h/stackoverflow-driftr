# Code from my Stack Overflow answer https://stackoverflow.com/a/74343150 (posted 2022-11-07), extracted verbatim; may need the question's context to run.
# from selenium.webdriver.common.by import By

    serialnumber = result.find_elements(By.XPATH, "//p[@class='service-tag mb-0 d-none d-lg-block']")
    expirydate = result.find_elements(By.XPATH, "//p[@class='warrantyExpiringLabel mb-0 ml-1 mr-1']")
