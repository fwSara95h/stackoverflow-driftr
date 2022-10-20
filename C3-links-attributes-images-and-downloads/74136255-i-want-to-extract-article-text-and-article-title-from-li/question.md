---
title: "I want to extract article text and article title from list of URL's"
site: stackoverflow
question_id: 74136255
url: https://stackoverflow.com/q/74136255
asked: 2022-10-20T07:54:20Z
asked_by: "Ashish Sharma"
asked_by_url: https://stackoverflow.com/users/18722108
last_edited: 2022-10-20T08:25:20Z
last_editor: "zerocog"
last_editor_url: https://stackoverflow.com/users/1480918
tags: [python, pandas, beautifulsoup]
score: -3
views_at_snapshot: 596
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8f2594cdaa3ef037533a9f665457d1d78282b15a84156e311af2997e77c5d944
---

# I want to extract article text and article title from list of URL's

Asked by [Ashish Sharma](https://stackoverflow.com/users/18722108) on Stack Overflow, <https://stackoverflow.com/q/74136255>, 2022-10-20, last edited 2022-10-20 by [zerocog](https://stackoverflow.com/users/1480918). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need help with the use of `BeautifulSoup`. How do I extract `article text` and `article title` from a list of URLs?  Here is my current state of the code:: 

    for i in range(0,len(df)):
        j = df.iloc[i].values
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        page = requests.get(j[0],headers = headers)#loading text in url
        soup = BeautifulSoup(page.content,'html.parser')#parsing url text
        content = soup.findAll(attrs = {'class':'td-post-content'})#extracting only text part
        content = content[0].text
        title = soup.findAll(attrs = {'class':'entry-title'})#extracting title of website
        #title = title[16].text
        print(content)

   
But I get Index error , Can anyone help ?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Marcin Orlowski](https://stackoverflow.com/users/1235698)** (2022-10-20): you may want to properly format your question's code
- **[Azhar Khan](https://stackoverflow.com/users/2847330)** (2022-10-20): At which line do you get index error? Please check for array length before accessing a specific index.
- **[Ashish Sharma](https://stackoverflow.com/users/18722108)** (2022-10-20): content = content[0].text  at this line
- **[Azhar Khan](https://stackoverflow.com/users/2847330)** (2022-10-20): Access the array elements only it is not empty. Use checks like `if content:`
