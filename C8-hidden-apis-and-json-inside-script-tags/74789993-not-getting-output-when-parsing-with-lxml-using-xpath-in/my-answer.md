---
title: "Not getting output when parsing with lxml using xpath in Beautifulsoup"
site: stackoverflow
question_id: 74789993
answer_id: 74794006
url: https://stackoverflow.com/a/74794006
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-14T05:39:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74794006/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3717c191ce7735ffd57dbf44c8546785559a134e4bafae69609f92700fc720f3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74794006>, 2022-12-14; **accepted**; score 0. Text as retrieved 2026-10-12.

#### 1. About the XPath

> ```python
> driver.find_element('xpath','//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span').text
> ```

I'm a bit surprised that the selenium code works for your Sephora links - the [link](https://www.sephora.com/product/coco-mademoiselle-P12495?skuId=513168&icid2=products) you provided redirects to a [*productnotcarried*](https://i.sstatic.net/bNBvj.png) page, but at [this link](https://www.sephora.com/ca/en/product/fenty-eau-de-parfum-P503757) (for example), that XPath [has no matches](https://i.sstatic.net/sz6dC.png). You can use `//p[@data-comp="Price "]//span/b` instead.
[![seph][1]][1]

Actually, even for Ulta, I prefer `//*[@class="ProductHero__content"]//*[@class="ProductPricing"]/span` just for human-readability although it looks better if you use this path with [css selectors](https://www.w3schools.com/cssref/css_selectors.php)

```python
prize=driver.find_element("css selector", '*.ProductHero__content *.ProductPricing>span').text 
```

---

##### [Coding for both sites - Selenium]

To account for both sites, you could set up something like this reference dictionary:

```python
xRef = {
    'www.ulta.com': '//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span',
    'www.sephora.com': '//p[@data-comp="Price "]//span/b'
}

# for url in urls[:599]:... ################ REST OF CODE #############
```

and then use it accordingly

```python
# from urllib.parse import urlsplit

# lst, urls, xRef = ....


# for url in urls[:599]:
    # sleep...driver.get...sleep...
    try:
         uxrKey = urlsplit(url).netloc
         prize = driver.find_element('xpath', xRef[uxrKey]).text
    except:
        # pass # you'll just be repeating whatever you got in the previous loop for prize
        # [also, if this happens in the first loop, an error will be raised at lst.append([prize])]

        prize = None # 'MISSING' # '' #
################ REST OF CODE #############
```

---

#### 2. Limitations of Scraping with bs4+requests

I don't know what `et` and `ureq` are, but response from `requests.get` can be parsed without them; although [afaik] bs4 doesn't have any XPath support, css selectors can be used with [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) .

```python
      price = soup.select('.ProductHero__content .ProductPricing>span') # for Ulta
```
```python
      price = soup.select('p[data-comp~="Price"] span>b') # for Sephora
```

Although that's [enough for Sephora](https://i.sstatic.net/HAdGC.png), there's another issue - **the price in Ulta pages are [loaded with js](http://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/)** so the parent of the price `span` [**is empty**](https://i.sstatic.net/0FDwL.png).

---

#### 3. [Suggested Solution] Extracting from JSON inside `script` Tags

For both sites, product data [can be found inside](https://i.sstatic.net/anOkH.png) `script` tags, so this function can be used to extract price from either site:

```python
# import json

############ LONGER  VERSION ##########
def getPrice_fromScript(scriptTag):
    try:
        s, sj = scriptTag.get_text(), json.loads(scriptTag.get_text())
        while s:
            sPair = s.split('"@type"', 1)[1].split(':', 1)[1].split(',', 1)
            t, s = sPair[0].strip(), sPair[1]
            try: 
                if t == '"Product"': return sj['offers']['price'] # Ulta
                elif t == '"Organization"': return sj['offers'][0]['price'] # Sephora
                # elif.... # can add more options
                # else.... # can add a default
            except: continue
    except: return None
#######################################

############ SHORTER VERSION ##########
def getPrice_fromScript(scriptTag):
    try:
        sj = json.loads(scriptTag.get_text())
        try: return sj['offers']['price'] # Ulta
        except: pass
        try: return sj['offers'][0]['price'] # Sephora
        except: pass 
        # try...except: pass # can try more options
    except: return None
#######################################
```

and you can use it with your BeautifulSoup code:

```python
# from requests_html import HTMLSession # IF you use instead of requests

# def getPrice_fromScript....

for i in range(len(df)):
    response = requests.get(df['product_url'].iloc[i]) # takes too long [for me]
    # response = HTMLSession().get(df['product_url'].iloc[i]) # is faster [for me]

    ## error handing, just in case ##
    if response.status_code != 200:
        errorMsg = f'Failed to scrape [{response.status_code} {response.reason}] - '
        print(errorMsg, df['product_url'].iloc[i])
        continue # skip to next loop/url

    soup = BeautifulSoup(response.content, 'html.parser')
    
    pList = [p.strip() for p in [
        getPrice_fromScript(s) for s in soup.select('script[type="application/ld+json"]')[:5] # [1:2]
    ] if p and p.strip()]

    if pList: df['price'].iloc[i] = pList[0]
```

(The price should be in the second `script` tag with `type="application/ld+json"`, but this is searching the first 5 just in case....)

---

<sub>**Note:** `requests.get` was being very slow when I was testing these codes, especially for Sephora, so I ended up using [`HTMLSession().get`](https://requests.readthedocs.io/projects/requests-html/en/latest/#tutorial-usage) instead.</sub>


  [1]: https://i.sstatic.net/NrRt4.png
