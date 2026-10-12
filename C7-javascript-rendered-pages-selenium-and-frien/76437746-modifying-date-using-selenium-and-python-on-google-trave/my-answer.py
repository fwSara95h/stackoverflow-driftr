# Code from my Stack Overflow answer https://stackoverflow.com/a/76440789 (posted 2023-06-09), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>         checkinElement.send_keys(search_query[j])
>

# --- block 2 ---
# from selenium.webdriver.common.keys import Keys

        checkinElement.send_keys(Keys.CONTROL, "a")
        checkinElement.send_keys(Keys.BACKSPACE)
        checkinElement.send_keys(checkin_query[j])
