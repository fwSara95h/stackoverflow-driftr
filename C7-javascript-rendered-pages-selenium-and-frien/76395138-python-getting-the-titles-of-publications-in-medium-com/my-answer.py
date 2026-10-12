# Code from my Stack Overflow answer https://stackoverflow.com/a/76416860 (posted 2023-06-06), extracted verbatim; may need the question's context to run.
h2Sel = 'a[href][aria-label="Post Preview Title"] h2'
elements = driver.find_elements(By.CSS_SELECTOR, h2Sel)
for x in elements:
    print(x.text)
