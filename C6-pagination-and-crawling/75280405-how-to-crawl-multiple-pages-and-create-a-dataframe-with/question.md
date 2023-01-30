---
title: "How to crawl multiple pages and create a dataframe with parsing?"
site: stackoverflow
question_id: 75280405
url: https://stackoverflow.com/q/75280405
asked: 2023-01-30T04:57:06Z
asked_by: "user21084142"
asked_by_url: (account no longer exists)
last_edited: 2023-01-30T08:59:34Z
tags: [web-scraping, beautifulsoup, web-crawler]
score: 0
views_at_snapshot: 168
answer_count: 2
accepted_answer_id: 75283337
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 20ce17e10ee33734bdff5f03334ab6799715cced16c6f03d343b845da48e8d49
---

# How to crawl multiple pages and create a dataframe with parsing?

Asked by user21084142 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/75280405>, 2023-01-30, last edited 2023-01-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I would like to load multple pages from a single website and extract specific attributes from different classes as below. Then I woule like to create a dataframe with parsed information from multiple pages.

# Extract from multiple pages
    for page in range(1,10):
        url = f"https://www.consilium.europa.eu/en/press/press-releases/?page={page}"
        res = requests.get(url)
        soup = bs(res.text, 'lxml')
# Parsing
    soup_content = soup.find_all('li', {'class':['list-item ceu clearfix','list-item gsc clearfix','list-item euco clearfix','list-item eg clearfix' ]})

    datePublished = []
    headline = []
    description =[]
    urls = []

    for i in range(len(soup_content)):
        datePublished.append(soup_content[i].find('span', {'itemprop': 'datePublished'}).attrs['content'])
        headline.append(soup_content[i].find('h3', {'itemprop': 'headline'}).get_text().strip())
        description.append(soup_content[i].find('p', {'itemprop': 'description'}).get_text().strip())
        urls.append('https://www.consilium.europa.eu{}'.format(soup.find('a', {'itemprop': 'url'}).attrs['href']))

# To DataFrame
    df = pd.DataFrame(data = zip(datePublished, headline, description, urls), columns=['date','title', 'description', 'link'])
    df

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-01-30): Are you having any issues with the current code? Aside from the messed up indentations and typos [like *`soup  bsoup(link)`*], it looks like it should work; It's risky to chain `.find....get...` like that in one statement though, bc if `.find` returns `None`, then `.get...` will raise an error. Would be safer to do something like in this [`extract_from_bs4tag`](https://pastebin.com/ZnZ7xM6u) function...
- **me** (2023-01-30): btw, you don't really need to *`i in range(len(soup_content))....soup_content[i].find...`* - since `i` doesn't seen essential, you can just iterate over `for sc in soup_content:...sc.find....`, if you need both `i` and `sc`, look into [enumerate](https://www.programiz.com/python-programming/methods/built-in/enumerate). `soup_content[i]` is only necessary if you want to **update** `soup_content`
- **user21084142 (account no longer exists)** (2023-01-30): I have modified using enumberate and it works well. However, the dataframe only shows the result of page 1 and `for page in pages` under `def bsoup(url):` doesn't apply to `soup = bsoup(link)` under `def max_page(link):`
- **me** (2023-01-30): [please fix your indentation, I can't tell which scope each variable is in.] Idk what's in `pages`, but you're not doing anything with `page`, so the loop is executing the exact same thing over and over. You're actually not doing anything to navigate through the pages at all...see some examples like https://stackoverflow.com/a/74334463/6146136 , https://stackoverflow.com/a/74343296/6146136
- **me** (2023-01-30): [empty lists should be initiated before *`for page....`*, but aside from that,] the "parsing" block should be indented to move inside the  *`for page....`* - otherwise I'd only expect results from the last `past`
