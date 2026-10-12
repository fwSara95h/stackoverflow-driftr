# Code from my Stack Overflow answer https://stackoverflow.com/a/74791332 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
sites = []
# for url in urls:   
        # driver.get...
        # soup = ....
        # try:....except:....

        data={
                'website':website
        }

        sites.append(data)

# --- block 2 ---
for pi, dictPair in enumerate(zip(product, sites)):
        product[pi].update(dictPair[1])

df = pd.DataFrame(product)
df.to_csv('firm.csv')

# --- block 3 ---
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
