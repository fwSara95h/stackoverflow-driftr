# Code from my Stack Overflow answer https://stackoverflow.com/a/76789908 (posted 2023-07-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     email_input = driver.find_element("email")
>     password_input = driver.find_element("pass")
>

# --- block 2 ---
# from selenium.webdriver.common.by import By

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
