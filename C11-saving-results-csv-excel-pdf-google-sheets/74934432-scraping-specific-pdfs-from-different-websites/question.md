---
title: "Scraping specific pdfs from different websites"
site: stackoverflow
question_id: 74934432
url: https://stackoverflow.com/q/74934432
asked: 2022-12-27T21:56:55Z
asked_by: "Cesare"
asked_by_url: https://stackoverflow.com/users/18899582
last_edited: 2022-12-28T13:54:06Z
tags: [python, html, web-scraping, spyder, pdf-scraping]
score: 1
views_at_snapshot: 98
answer_count: 2
accepted_answer_id: 74940312
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 69e52e31e4d868ca897b67fef77c6d5ed9c0ff790b799f2b6c048d8c0ff3f4e3
---

# Scraping specific pdfs from different websites

Asked by [Cesare](https://stackoverflow.com/users/18899582) on Stack Overflow, <https://stackoverflow.com/q/74934432>, 2022-12-27, last edited 2022-12-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

First question here. I need to download a specific pdf from every url. I need just the pdf of the european commission proposal from each url that I have, which is always in a specific part of the page

[Here the part from the website that I would always need in pdf form].
[The European Commission proposal](https://i.sstatic.net/vU9Pl.png)

And here is the html code of it (The part that is interesting for me is : 

"http://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2020/0791/COM_COM(2020)0791_EN.pdf" is the pdf that I need, as you can see from the image
) 

     [<a class="externalDocument" href="http://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2020/0791/COM_COM(2020)0791_EN.pdf" target="externalDocument">COM(2020)0791</a>, <a href="http://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2020/0791/COM_COM(2020)0791_EN.pdf" target="_blank">
     <span class="ep_name">
     COM(2020)0791
     				</span>
     <span class="ep_icon"> </span>
     </a>, <a href="http://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2020/0791/COM_COM(2020)0791_EN.pdf" target="_blank">
     <span class="ep_name">
     COM(2020)0791
     				</span>
    <span class="ep_icon"> </span>
    </a>]

   

I used the subsequent code for the task, so that it takes every url from my csv file and it goes in each page to download every pdf. The problem is that with this approach it takes also other pdf which I do not need. It is fine for me if it downloads it but I need to distinguish them from the part where they are downloaded, this is why i am asking here to download all the pdf from just one specific subsection. So if it is possible to distinguish them in the name by section it would be also fine, for now this code gives me back 3000 pdfs, i need around 1400, one for each link, and if it keeps the name of the link it could be also easier for me, but is not my main worry since they are ordered in order of recall from the csv file and it will be easy to tidy them after.

In synthesis this code here needs to become a code which downloads only from one part of the site, instead of all of it:

```
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
#import pandas

#data = pandas.read_csv('urls.csv')
#urls = data['urls'].tolist()

urls = ["http://www.europarl.europa.eu/oeil/FindByProcnum.do?lang=en&procnum=OLP/2020/0350", "http://www.europarl.europa.eu/oeil/FindByProcnum.do?lang=en&procnum=OLP/2012/0299", "http://www.europarl.europa.eu/oeil/FindByProcnum.do?lang=en&procnum=OLP/2013/0092"]
#url="http://www.europarl.europa.eu/oeil/FindByProcnum.do?lang=en&procnum=OLP/2013/0092"


folder_location = r'C:\Users\myname\Documents\R\webscraping'
if not os.path.exists(folder_location):os.mkdir(folder_location)

for url in urls:
 response = requests.get(url)
 soup= BeautifulSoup(response.text, "html.parser")     
 for link in soup.select("a[href$='EN.pdf']"):
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
```

for example I did not want do download this file here
[follow up document][1]
which is a follow up document which starts with com, ends with EN.pdf, but has a different date because it is a follow up (in this case 2018)
as you can see from the link:
https://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2018/0564/COM_COM(2018)0564_EN.pdf


  [1]: https://i.sstatic.net/1Ap7K.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-28): could you include some examples of links you *don't* want to download?
