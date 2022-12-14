---
title: "Web scraping all the newsletter info from the blog using BeautifulSoup"
site: stackoverflow
question_id: 74798064
url: https://stackoverflow.com/q/74798064
asked: 2022-12-14T12:07:08Z
asked_by: "Anand"
asked_by_url: https://stackoverflow.com/users/20549925
last_edited: 2022-12-14T12:14:03Z
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 262
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1014a04a3daaab28cd6167959dae42646523e7e79d12c01eec4c1d4195bcd9a8
---

# Web scraping all the newsletter info from the blog using BeautifulSoup

Asked by [Anand](https://stackoverflow.com/users/20549925) on Stack Overflow, <https://stackoverflow.com/q/74798064>, 2022-12-14, last edited 2022-12-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

There are 48 pages in this blog and i have scrapped the 1st page using web scraping. Using for loop i am trying to scrape remaining 47 pages and append the 47 pages dataframes to a 1st page dataframe but i am getting errors and in some cases i can only concat upto 2 pages dataframes. 


```
import requests
from bs4 import BeautifulSoup
import pandas as pd

No_of_pages_in_radletters = 48
page_urls = []
for i in range(2,No_of_pages_in_radletters):
        main_url = f'https://www.radletters.com/?page={i}&tag='
        page_urls.append(main_url)

for page in page_urls:
    response = requests.get(page)
    soup = bs(response.text,'html.parser')

    # Retriving newsletter names from each page
    newsletter_class = 'md:mt-2 mt-1 align-text-bottom inline-block font-semibold cursor-text'
    newsletter_title = soup.find_all('div',newsletter_class)
    newsletter_title_list = []
    for title in newsletter_title:
        newsletter_title_list.append(title.text.strip())

    # Retrieving newsletter description of each newsletter
    newsletter_desc_class = 'flex justify-center text-sm text-gray-600'
    newsletter_description = soup.find_all('div',{'class' : newsletter_desc_class})
    newsletter_description_list = []
    for desc in newsletter_description:
        newsletter_description_list.append(desc.text.strip())

    # Retrieving url of each newsletter
    newsletter_url_class = 'flex justify-center mx-8 mt-3'
    newsletter_url = soup.find_all('div',{'class' : newsletter_url_class})
    newsletter_url_list = []
    for url in newsletter_url:
        newsletter_url_list.append(url.a['href'])

    # Retrieving topic tags of each news letter    
    newsletter_topic_tags_class = 'md:mt-2 mt-1 flex flex-wrap justify-center'
    newsletter_topic_tags_class_2 = 'inline-flex text-sm hover:bg-gray-100 text-gray-700 rounded-full px-3 my-1 mx-1 h-6 border border-gray-200 shadow cursor-pointer'
    newsletter_topic_tags = soup.find_all('div',{'class' : newsletter_topic_tags_class})
    newsletter_topic_tags_list = []
    for topic_tags in newsletter_topic_tags:
        newsletter_topic_tags_list.append(topic_tags.text.replace('\n','').rstrip().lstrip().replace('            ',','))

    dict_2 = {
    'Newsletter Title' : newsletter_title_list,
    'Description' : newsletter_description_list,
    'url' : newsletter_url_list,
    'Topic Tags' : newsletter_topic_tags_list
    }
    pages_df = pd.DataFrame(dict_2)

    # concatenating 1st page dataframe with the remaining pages dataframes
    page1_df = pd.concat(page1_df,pages_df)

print(page1_df)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Cleared](https://stackoverflow.com/users/3222782)** (2022-12-14): What errors are you getting?
- **[Anand](https://stackoverflow.com/users/20549925)** (2022-12-14): The dataframes are not concatenating to the page1_df
- **[Cleared](https://stackoverflow.com/users/3222782)** (2022-12-14): Can you write the error message here?
- **[Anand](https://stackoverflow.com/users/20549925)** (2022-12-14): TypeError: first argument must be an iterable of pandas objects, you passed an object of type "DataFrame"
- **[Cleared](https://stackoverflow.com/users/3222782)** (2022-12-14): Take a look at the documentation for pd.concat. What it expects as argument is not two data frames, but rather a list of dataframes. So I suggest you append your dataframes to a list in the loop, and then after/outside your loop you run pd.concat(list_of_dfs)
- **[Anand](https://stackoverflow.com/users/20549925)** (2022-12-14): As there are many dataframes, how can i list the each dataframe.
- **[Cleared](https://stackoverflow.com/users/3222782)** (2022-12-14): df_list = [page1_df, page2_df, page3_df, ...], and then pd.concat(df_list). Or inside each loop do df_list.append(page_df) or similar.
