# Code from my Stack Overflow answer https://stackoverflow.com/a/75011988 (posted 2023-01-04), extracted verbatim; may need the question's context to run.
while True:
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Load More Listings')]")))

        # ActionChains(driver).move_to_element(element).click().perform()
        driver.execute_script('arguments[0].scrollIntoView(false);', element)
        try: element.click() # for some reason, the 1st click always fails
        except: element.click() # but after the 1st attempt, the 2nd click works...

    except Exception as e:
        print (e)
        break
