---
title: "Append data wrong in csv file"
site: stackoverflow
question_id: 74790719
answer_id: 74791332
url: https://stackoverflow.com/a/74791332
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T21:58:22Z
last_edited: 2022-12-13T22:31:00Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74791332/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bb314cf2677bab22ae14384fc2ad232ae784a541c80600ac0b89e587bc9562ce
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74791332>, 2022-12-13, last edited 2022-12-13; **accepted**; score 1. Text as retrieved 2026-10-12.

You can't append `wev` and `data` separately - you need website and name in the same dictionary for pandas to know that they belong to same row.

---

You could add the websites in a separate list like

```python
sites = []
# for url in urls:   
        # driver.get...
        # soup = ....
        # try:....except:....

        data={
                'website':website
        }
 
        sites.append(data) 
```

and then [`zip`](https://www.w3schools.com/python/ref_func_zip.asp) and [combine](https://www.geeksforgeeks.org/python-dictionary-update-method/):

```python
for pi, dictPair in enumerate(zip(product, sites)):
        product[pi].update(dictPair[1])

df = pd.DataFrame(product)
df.to_csv('firm.csv')
```

**However, I don't think it's the best way to make sure the right Names and Websites are matched up.**

---

You should just add to the same dictionary for each row from the start instead of zipping and merging.

```python
added_urls = []        
product = [] 
soup = BeautifulSoup(driver.page_source,"lxml")
details = soup.select("tbody tr")
for detail in details:

        try:        
                t1 = detail.select_one("h5.profile-title a").text
        except:
                # pass # then you'll just be using the previous row's t1
                # [also, if this happens in the first loop, it will raise an error]

                t1 = 'MISSING' # '' #
  
        wev = {
                'Name':t1,
                }

        href = detail.select_one("h5.profile-title + p a[href]") 
        if href and href.get("href", '').startswith('http'): 
                wev['page_link'] = href.get("href")
                added_urls.append(href.get("href"))
        
        product.append(wev)

### IF YOU WANT ROWS THAT CAN'T BE CONNECTED TO NAMES ###       
page_links = driver.find_elements(By.CSS_SELECTOR, "h5.profile-title + p a")
for link in page_links:
        if href in added_urls: continue  # skip links that are already added
        href = link.get_attribute("href")

        # urls.append(href)
        added_urls.append(href)
        product.append({"page_link": href})
##########################################################
        

for pi, prod in enumerate(product): 
        if "page_link" not in prod or not prod["page_link"]: continue ## missing link
        url = prod["page_link"]
        
        driver.get(url) 
        soup = BeautifulSoup(driver.page_source,"lxml")
        try:
                website=soup.select_one("p.adress-info a[target='_blank']").text
        except:
                website=''
        
        del product[pi]["page_link"] ## REMOVE this line IF you want a page_link column in csv

        # data={'website':website}
        # product.append(data)
        product[pi]['website'] = website
                
df=pd.DataFrame(product)
df.to_csv('firm.csv')
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Amen Aziz](https://stackoverflow.com/users/17344809)** (2022-12-14): can yu answer that also......https://stackoverflow.com/questions/74798528/data-are-overwritten-using-beautifulsoup
