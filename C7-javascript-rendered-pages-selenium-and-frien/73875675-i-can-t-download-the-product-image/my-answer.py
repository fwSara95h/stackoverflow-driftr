# Code from my Stack Overflow answer https://stackoverflow.com/a/73876351 (posted 2022-09-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
imgDivs = driver.find_elements(By.CSS_SELECTOR, '._1OPdfl > ._2PWsS4')
for i in range(len(imgDivs)):
    d = imgDivs[i].get_attribute('style')
    imgUrl = d.split('url("')[1].split('")')[0]
    with open(f"img_{i}.jpeg", "wb") as f:
        f.write(requests.get(imgUrl).content)
        f.close()
    print(imgUrl)

# --- block 2 ---
def getImgUrl(imgDiv):
    d = imgDiv.get_attribute('style')
    iUrl = d.split('url("')[1].split('")')[0]
    if iUrl.endswith('_tn'): 
        iUrl = iUrl[:-3]
    return iUrl

# --- block 3 ---
imgDivs = driver.find_elements(By.CSS_SELECTOR, '._1OPdfl > ._2PWsS4')
imgUrls = [getImgUrl(iDiv) for iDiv in imgDivs]
imgUrls = list(set(imgUrls))  # keep only unique urls
imgTot = len(imgUrls)

for i in range(imgTot):
    imgUrl = imgUrls[i]
    with open(f"img_{i}.jpeg", "wb") as f:
        f.write(requests.get(imgUrl).content)
        f.close()
    print(f'{i+1} of {imgTot} links: ', imgUrl)
