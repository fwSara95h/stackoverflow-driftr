---
title: "I can't download the product image"
site: stackoverflow
question_id: 73875675
answer_id: 73876351
url: https://stackoverflow.com/a/73876351
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T04:54:46Z
last_edited: 2022-09-30T02:13:54Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73876351/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 20af2c99b61bd7e6ac0913e657581555baed07942926bc7593ec88ff1e501356
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73876351>, 2022-09-28, last edited 2022-09-30; **accepted**; score 0. Text as retrieved 2026-10-12.

This should download all the product images:

    #import requests  

    imgDivs = driver.find_elements(By.CSS_SELECTOR, '._1OPdfl > ._2PWsS4')
    for i in range(len(imgDivs)):
        d = imgDivs[i].get_attribute('style')
        imgUrl = d.split('url("')[1].split('")')[0]
        with open(f"img_{i}.jpeg", "wb") as f:
            f.write(requests.get(imgUrl).content)
            f.close()
        print(imgUrl)

The enlarged image gets downloaded twice. You can change the `find_elements` arguments to be pickier about the images.

EDIT: to reduce duplicates you *might* try this:

    def getImgUrl(imgDiv):
        d = imgDiv.get_attribute('style')
        iUrl = d.split('url("')[1].split('")')[0]
        if iUrl.endswith('_tn'): 
            iUrl = iUrl[:-3]
        return iUrl

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
since the link to the thumbnail seems to be the same as for the enlarged version - but with '_tn' added to the end. BUT, if they change their naming conventions this might cause errors

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Felipe](https://stackoverflow.com/users/20021812)** (2022-09-30): I answered below the code repeats many times, infinite loop
