# Code from my Stack Overflow answer https://stackoverflow.com/a/74711529 (posted 2022-12-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# heats = driver.find_elements(By.XPATH, '//*[starts-with(@id,"heat-")]')
heats = driver.find_elements(By.CSS_SELECTOR, '*[id^="heat-"]')
for heat in heats:
    names = heat.find_elements(By.XPATH, '/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span')
    for n in names[:4]:
        name = n.text

# --- block 2 ---
# heats = driver.find_elements(By.XPATH, '//*[starts-with(@id,"heat-")]')
heats = driver.find_elements(By.CSS_SELECTOR, '*[id^="heat-"]')
for heat in heats:
    for i in range(4):
        name = heat.find_element(By.XPATH, f'/div/div[2]/div[{i + 1}]/div[1]/div[1]/div/div[2]/div[1]/span').text
