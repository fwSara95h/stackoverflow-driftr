# Code from my Stack Overflow answer https://stackoverflow.com/a/74119968 (posted 2022-10-19), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def linkToSoup_selenium(l, ecx=None, clickFirst=None):
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        # I copy chromedriver.exe to the same folder as this py file

        driver.get(l) # go to link

        # if something needs to be confirmed by click
        if clickFirst:
            WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, clickFirst))
            )
            driver.find_element(By.XPATH, clickFirst).click()

        # if some section needs to be loaded first
        if ecx:
            WebDriverWait(driver, 25).until(
                EC.visibility_of_all_elements_located((By.XPATH, ecx)))

        lSoup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()
        del driver
        return lSoup
    except Exception as e:
        print(str(e))
        return None

# --- block 2 ---
soup = linkToSoup_selenium(
    l = 'https://dre.pt/dre/detalhe/anuncio-concurso-urgente/491-2022-201313437',
    ecx = '//div[@id="transitionContainer"]//div[@data-container]//div[@data-container]/p'
    # clickFirst argument is not necessary for this site
)

# --- block 3 ---
if soup is not None: 
    numbered = soup.find_all(lambda t: t.name == 'p' and
        t.text.count(' - ') > 0 and t.text.split(' - ')[0].isdigit())

    for n in numbered:
        print(n.get_text(strip=True))
