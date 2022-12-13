---
title: "Not getting output when parsing with lxml using xpath in Beautifulsoup"
site: stackoverflow
question_id: 74789993
url: https://stackoverflow.com/q/74789993
asked: 2022-12-13T19:27:24Z
asked_by: "THASNI HAKEEM"
asked_by_url: https://stackoverflow.com/users/20769294
last_edited: 2022-12-13T19:54:35Z
tags: [python, xpath, beautifulsoup, lxml]
score: 0
views_at_snapshot: 285
answer_count: 1
accepted_answer_id: 74794006
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a195fccb2e2e96655b103b4d3d862601dfb73b492d9eafbf85fb85d15c4339b0
---

# Not getting output when parsing with lxml using xpath in Beautifulsoup

Asked by [THASNI HAKEEM](https://stackoverflow.com/users/20769294) on Stack Overflow, <https://stackoverflow.com/q/74789993>, 2022-12-13, last edited 2022-12-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When I was trying to scrape the data from Sephora and Ulta using beautifulsoup, I could get the html content of the page. Then when I tried to use lxml to parse it using xpath, i didn't get any output. But working with this same xpath in selenium, i could get the output. 


**Using Beautifulsoup**
```
for i in range(len(df)):
    response = requests.get(df['product_url'].iloc[i])
    my_url=df['product_url'].iloc[i]
    My_url= ureq(my_url)
    my_html=My_url.read()
    My_url.close()
    soup = BeautifulSoup(my_html, 'html.parser')
    dom = et.HTML(str(soup))
#price
    try:
      price=(dom.xpath('//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span/text()'))
      df['price'].iloc[i]=price
    except:
      pass
```
**Using Selenium**
```
lst=[]
urls=df['product_url']
for url in urls[:599]:
    time.sleep(1)
    driver.get(url)
    time.sleep(2)
    try:
         prize=driver.find_element('xpath','//*[@id="1b7a3ab3-2765-4ee2-8367-c8a0e7230fa4"]/span').text
    except:
        pass
 
    lst.append([prize])
    pz=None
    dt=None
```

Does anyone know why i cant get the content using lxml to parse it using same xpath in beautifulsoup? Thanks so much in advance.

Sample Link of Ulta:
  [1]: https://www.ulta.com/p/coco-mademoiselle-eau-de-parfum-spray-pimprod2015831

Sample Link of Sephora:
  [2]: https://www.sephora.com/product/coco-mademoiselle-P12495?skuId=513168&icid2=products

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[larsks](https://stackoverflow.com/users/147356)** (2022-12-13): You didn't include the url from which you're fetching the data, but it's highly likely that the web page you're scraping is populated dynamically using Javascript. Selenium works because selenium is a full browser with a javascript engine. Python `requests` is just an http client and will not be able to access dynamic content.
- **me** (2022-12-13): what are `et` and `ureq`? are you parsing multiple times? I feel like `str(soup)` and `my_html` might be effectively the same thing....
