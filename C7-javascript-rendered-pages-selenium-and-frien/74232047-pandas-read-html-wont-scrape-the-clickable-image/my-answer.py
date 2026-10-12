# Code from my Stack Overflow answer https://stackoverflow.com/a/74273504 (posted 2022-11-01), extracted verbatim; may need the question's context to run.
prefVals = [
    e.get_attribute('value') for e in 
    driver.find_elements_by_xpath(".//table[@id='gvSearchResults']//td/input")
]
val_scraped = []
max_scrapes = len(table_elements) # or whatever you prefer

valImgs = []

for i in range(max_scrapes):
    prefs = [
        e for e in 
        driver.find_elements_by_xpath(".//table[@id='gvSearchResults']//td/input")
        if e.get_attribute('value') not in val_scraped
    ]
    if not prefs: break # all scraped

    val_i = prefs[0].get_attribute('value')
    prefs[0].click()
    # add wait if necessary

    first_image = driver.find_element_by_xpath('.//img[@id="ImgCtrlLarge"]').get_attribute('src')

    # click for more images if you want

    val_scraped.append(val_i)
    valImgs.append([val_i, first_image, ...]) # add all image links for val_i

    # use "< Search Results" button to go back
    driver.find_element_by_xpath('.//input[@id="backButton"]').click()
    # add wait if necessary

imgCols = [[r for r in valImgs if r[0] == v] for v in prefVals]
imgCols = [r[0] if len(r) > 0 else [] for r in imgCols]
imgCol_headers = ['PRONI_REFERENCE_VALUE', 'FIRST_IMAGE', ....] # add in headers as appropriate

imgDfs = pd.DataFrame(imgCols, columns=imgCol_headers)

finalDf = pd.concat([dfs[0], imgDfs], axis=1)
