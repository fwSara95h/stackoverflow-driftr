---
title: "Trying to request information from \"IDEALISTA webpage\" in PYTHON with \"requests\" and I get <Response [403]>"
site: stackoverflow
question_id: 74173137
answer_id: 74187673
url: https://stackoverflow.com/a/74187673
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-24T23:11:14Z
last_edited: 2022-10-24T23:16:29Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74187673/revisions
accepted: false
score: 2
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c53532ffd342b8a89a0b50b542293e371b660f1d38e34c2bff884c90016fcc2f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74187673>, 2022-10-24, last edited 2022-10-24; score 2. Text as retrieved 2026-10-12.

Your headers are probably fine, but I think you need to include cookies as well.

One way to replicate your browser's request almost exactly is to [go to the network tab][1] on the [browser's dev tools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools), and then copy the request for the page 
[![enter image description here][2]][2]
(you *might* need to refresh for it to show up - it's the one with the same **Request URL** as whatever you entered in the address bar)

Then, you can paste the copied cURL somewhere like [curlconverter](https://curlconverter.com/) to convert to python code, and then copy paste *that* into to your code so that you can continue with
```python
soup = BeautifulSoup(response.content, "html.parser")
```
<hr>

**However**, you will have to update the cookies frequently, so it migth be less hassle to use a library or api that can bypass these blocks. For example if you sign up for [ScrapingAnt](https://app.scrapingant.com/signup), and then paste your API token to the code below:
```python
scrapingant_api = 'https://api.scrapingant.com/v2/general'
scrapingant_key = 'YOUR_API_TOKEN' # paste here
url_to_Scrape = 'https://www.idealista.com/inmueble/97795476/'
url = f'{scrapingant_api}?url={url_to_Scrape}&x-api-key={scrapingant_key}'
r = requests.get(url)

soup = BeautifulSoup(r.text)
inm = soup.find(class_="main-info__title-main").text
print(inm) # prints "Ático en venta en plaza del Ayuntamiento, 6"
```

<hr>

There is a limit to how many requests you can run on the free tier of ScrapingAnt, though; so I suggest also considering selenium if you'll be needing to scrape an unlimited number of times. If you copy the function from [this gist](https://gist.github.com/Driftr95/cbae6710c134df708f44ade8503f6638), you can simply call it like:

```python
# def linkToSoup_selenium .... # paste function into your code

soup = linkToSoup_selenium('https://www.idealista.com/inmueble/97795476/')
inm = soup.find(class_="main-info__title-main").text
print(inm) # prints "Ático en venta en plaza del Ayuntamiento, 6"
```


  [1]: https://i.sstatic.net/43R56.png
  [2]: https://i.sstatic.net/jLohC.png
