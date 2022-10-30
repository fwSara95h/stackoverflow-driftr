---
title: "Web scraping struggles of a category ending in == 0$"
site: stackoverflow
question_id: 74255099
url: https://stackoverflow.com/q/74255099
asked: 2022-10-30T17:07:18Z
asked_by: "Troy McLure"
asked_by_url: https://stackoverflow.com/users/19690963
last_edited: never
tags: [python-3.x, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 134
answer_count: 1
accepted_answer_id: 74274619
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2fdcf86c1c05d89c41276cc8744788426a20e2526237026b25e3c2339e4e90f7
---

# Web scraping struggles of a category ending in == 0$

Asked by [Troy McLure](https://stackoverflow.com/users/19690963) on Stack Overflow, <https://stackoverflow.com/q/74255099>, 2022-10-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I an writting a Paython script to scrap a website, and I get null output when I try to get an specific class.

The block is:



```
<div class="prdt Product"> == $0
	::before
	<!-- /cache: pl_class_46761{nULE0} -->
	<div>
		<h3 class= Title">...</div>
		... etc, the rest of items
```

And the .py is:



```
from bs4 import BeautifulSoup
import requests

baseurl = 'htps://www.list_of_brands.php'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

r = requests.get('https://www.the_first_page_of_a_brand.html')
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='prdt Product')

print(productlist)
```

And what I get printed is just []

I can't find where is my error... maybe something related with == $0 ?? Because it seems that it doesn't pick the container properly.

Thank you!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-31): We cannot [replicate your exact issue](https://stackoverflow.com/help/minimal-reproducible-example) without having the actual url/s you're using... or maybe the *actual* html your code is working with - but where did you get the html block in you q? If you just copied it from the site itself on your browser, that's not necessarily what's in `r.content`. Make sure that `r.status_code == 200`, and then run `with open('x.html', 'wb') as f: f.write(r.content)` and then open and see if 'x.html' looks like the page you're trying to scrape. If not, then the issue is with requests, not BeautifulSoup
- **[Troy McLure](https://stackoverflow.com/users/19690963)** (2022-11-01): Hi @Driftr95 , thank you for your reply. The URL is https://www.maquillalia.com/apieu-m-406.html. While it gets correctly the class 'prdt Product Agotado', it doesn't get the other one 'prdt Product'. BTW, I have printed the r.status_code and it is 200.
