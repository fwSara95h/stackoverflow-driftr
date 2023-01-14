---
title: "Data/Table Scraping from Website using Python"
site: stackoverflow
question_id: 75119631
url: https://stackoverflow.com/q/75119631
asked: 2023-01-14T16:48:42Z
asked_by: "python noobie"
asked_by_url: https://stackoverflow.com/users/16395506
last_edited: never
tags: [python, dataframe, web-scraping, beautifulsoup, screen-scraping]
score: 1
views_at_snapshot: 159
answer_count: 2
accepted_answer_id: 75120574
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2c6dd050de01f3818e16fa8c5694c63bce617cf5c2967a9d23f30162d986ea73
---

# Data/Table Scraping from Website using Python

Asked by [python noobie](https://stackoverflow.com/users/16395506) on Stack Overflow, <https://stackoverflow.com/q/75119631>, 2023-01-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape a data from a table on a website. 
However, I am continuously running into "ValueError: cannot set a row with mismatched columns". 

The set-up is:

    url = 'https://kr.youtubers.me/united-states/all/top-500-youtube-channels-in-united-states/en'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    table1 = soup.find('div', id = 'content')

    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

    my_data = pd.DataFrame(columns = headers)
    my_data = my_data.iloc[:,:-4]

Here, I was able to make an empty dataframe with headers same as the table (I did iloc because there were some repeating columns at the end).

Now, I wanted to fill in the empty dataframe through:

    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(my_data)
        my_data.loc[length] = row

However, as mentioned, I get "ValueError: cannot set a row with mismatched columns" in this line: length = len(my_data).
I would really appreciate any help to solve this problem and to fill in the empty dataframe.

Thanks in advance.
