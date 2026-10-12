# Code from my Stack Overflow answer https://stackoverflow.com/a/74565584 (posted 2022-11-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
chbVal = '613' # in case you need be able to change this

(By.CSS_SELECTOR, f'label > input[type="checkbox"][value="{chbVal}"][checked=""]') # for checked

(By.CSS_SELECTOR, f'label > input[type="checkbox"][value="{chbVal}"]:not([checked])') # for unchecked

# --- block 2 ---
chbVal = '613' # in case you need be able to change this

(By.XPATH, f'//label/input[@type="checkbox"][@value="{chbVal}"][@checked=""]') # for checked

(By.XPATH, f'//label/input[@type="checkbox"][@value="{chbVal}"][not(@checked="")]') # for unchecked
