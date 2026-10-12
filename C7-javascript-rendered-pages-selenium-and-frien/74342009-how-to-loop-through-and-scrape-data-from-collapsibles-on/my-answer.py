# Code from my Stack Overflow answer https://stackoverflow.com/a/74342847 (posted 2022-11-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
try:
    ### CODE THAT MIGHT RAISE EXCEPTION ###
except Exception as err:
    print(str(err))
    #########  HANDLE  EXCEPTION  #########

# --- block 2 ---
try:
    dtarget = n.get_attribute('data-target')
    dSel = f'a[data-target="{dtarget}"]'
    eSel = f'{dtarget} .store-email'

    s.execute_script("arguments[0].scrollIntoView(false);", n)
    WebDriverWait(s, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dSel)))
    n.click()
    time.sleep(3)

    emails = s.find_element(By.CSS_SELECTOR, eSel)
    email.append(emails.text)
    time.sleep(3)
except Exception as err:
    print(str(err))
    s.quit()
    break # no point looping again after s.quit()

# --- block 3 ---
['monica.bridalboutique@gmail.com', 'angelicasdesign@gmail.com', 'rbeamer@thetuxshopdm.com', 'staceysbridal@gmail.com', 'katie@somethingbluebride.com', 'info@affinitybridals.com', 'backwardsboutique16830@gmail.com']
