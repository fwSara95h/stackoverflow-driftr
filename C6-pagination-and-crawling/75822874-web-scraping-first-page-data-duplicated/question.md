---
title: "Web scraping. First page data duplicated"
site: stackoverflow
question_id: 75822874
url: https://stackoverflow.com/q/75822874
asked: 2023-03-23T12:14:09Z
asked_by: "Bek"
asked_by_url: https://stackoverflow.com/users/20756357
last_edited: 2023-03-23T12:24:00Z
last_editor: "theherk"
last_editor_url: https://stackoverflow.com/users/2081835
tags: [python, dataframe, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 65
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7732086d96cd84b991f639262938a6a7f794ec935f1a9e788bbb42368ac26012
---

# Web scraping. First page data duplicated

Asked by [Bek](https://stackoverflow.com/users/20756357) on Stack Overflow, <https://stackoverflow.com/q/75822874>, 2023-03-23, last edited 2023-03-23 by [theherk](https://stackoverflow.com/users/2081835). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Here is code using Bs4 and pandas dataframe to scrape two websites' data . second page successfully scraped but instead of showing second page data first page's data duplicated .

-------

```python
@app.route('/')
def index():
    try:
        webpage1 = requests.get('https://bekorganics.myshopify.com/collections/nuts')
        sp1 = BeautifulSoup(webpage1.content, 'html.parser')
        webpage2 = requests.get('https://perfectorganics.myshopify.com/collections/nuts-1')
        sp2 = BeautifulSoup(webpage2.content, 'html.parser')
    except Exception as e:
        # Handle the exception here, e.g. log the error, display an error message to the user, etc.
            print(f"An error occurred: {e}")
            return "Sorry, we could not process your request at this time. Please try again later."    


    data1 = []
    for i in range(1, 3):
        #Extracting data from first website
    
        url = f'https://bekorganics.myshopify.com/collections/nuts?page={i}'
        webpage = requests.get(url)
        sp = BeautifulSoup(webpage.content, 'html.parser')
        title1 = sp.find_all('div', 'card__information')
        sellprice1 = sp.find_all('span', 'price-item price-item--regular')
        for title0, sellprice0 in zip(title1, sellprice1):
            title_text = title0.find('a').text
            price_text= sellprice0.text
            if title_text and price_text:
                product = {'Name of Product': title_text.strip(), 'Selling Price': re.sub(r'\s+', ' ', price_text.strip())}
                data1.append(product)
        next_page = sp.find('a', {'class': 'page-link', 'rel': 'next'})
```

[two websites scraped data ](https://i.sstatic.net/j5A3P.png)
First page data keep repeating and i am trying to avoid data repeating and trying to scrape next page data

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[childnick](https://stackoverflow.com/users/11338900)** (2023-03-23): I haven't solved your problem but just an FYI you can add "/products.json" to the end of the url to get pretty json back instead of having to parse html   https://perfectorganics.myshopify.com/collections/nuts-1/products.json & https://bekorganics.myshopify.com/collections/nuts/products.json
