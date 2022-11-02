---
title: "Extract data from Dell Community Forum for a specific date"
site: stackoverflow
question_id: 74292169
answer_id: 74293454
url: https://stackoverflow.com/a/74293454
author: "Mihnea-Octavian Manolache"
author_url: https://stackoverflow.com/users/13904455
posted: 2022-11-02T17:34:45Z
last_edited: 2023-04-23T15:37:00Z
last_editor: "blackgreen"
last_editor_url: https://stackoverflow.com/users/4108803
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e53b6d6d7d6fe25e22e5c88cbe81f162f59f81b0266cfc9dc210976bced94a7
role: another answer on the same question, kept as context; not my work
---

# Answer by [Mihnea-Octavian Manolache](https://stackoverflow.com/users/13904455) — 2022-11-02

Posted on Stack Overflow, <https://stackoverflow.com/a/74293454>, 2022-11-02, last edited 2023-04-23; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

it seems to me you have an issue with your selectors and the fact that you're searching for them in the general scope (the entire HTML body). My approach would be to narrow down 'components' and search inside them:

1. Locate the `div` that holds all comments 
2. Search inside it for each comment comment container
3. Get the username, date and comment info from each comment container

Here is how you can achieve this:

```py
import requests
from bs4 import BeautifulSoup

url = "https://www.dell.com/community/Inspiron-Desktops/I-am-getting-time-sync-errror-and-the-last-synced-time-shown-as/m-p/8290678#M36017"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

date = '10-25-2022'
comments = []

comments_section = soup.find('div', {'class':'lia-component-message-list-detail-with-inline-editors'})
comments_body = comments_section.find_all('div', {'class':'lia-linear-display-message-view'})
for comment in comments_body:
    if date in comment.find('span',{'class':'local-date'}).text:
        comments.append({
            'name': comment.find('a',{'class':'lia-user-name-link'}).text,
            'date': comment.find('span',{'class':'local-date'}).text,
            'comment': comment.find('div',{'class':'lia-message-body-content'}).text,
        })

data = {
    "title": soup.find('div', {'class':'lia-message-subject'}).text,
    "comments": comments
}

print(data)
```

This script generates an JSON object (stringified) that looks like this:

```js
{
   "title":"\n\n\n\n\n\t\t\t\t\t\t\tI am getting time sync errror and the last synced time shown as a day in 2015\n\t\t\t\t\t\t\n\n\n\n",
   "comments":[
      {
         "name":"jraju",
         "date":"10-25-2022",
         "comment":"This pc is desktop inspiron 3910 model . The dell supplied only this week."
      },
      {
         "name":"Mary G",
         "date":"10-25-2022",
         "comment":"Try rebooting the computer and connecting to the internet again to see if that clears it up.\\xa0\nDon't forget to run Windows Update to get all the necessary updates on a new computer.\\xa0\n\\xa0"
      },
      {
         "name":"RoHe",
         "date":"10-25-2022",
         "comment":"You might want to read Fix: Time synchronization failed on Windows 11.\nTotally ignore the part about downloading the software tool, and scroll down that same page to the part: How to manually sync time on a Windows 11 PC.\nNOTE: In step #6, if time.windows.com doesn't work, pick a different server from the drop-down menu on that screen.\n\nRon\\xa0\\xa0 Forum Member since 2004\\xa0\\xa0 I'm not a Dell employee"
      }
   ]
}
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[NApStor](https://stackoverflow.com/users/20399258)** (2022-11-17): This does not take the main message, i.e, the comment of the original post into account (if it is made on the given date), but only the subsequent reply comments. How can i include that as well?
- **[Mihnea-Octavian Manolache](https://stackoverflow.com/users/13904455)** (2022-11-18): I don't understand what you're looking for exactly. Maybe adjust the date?
- **[NApStor](https://stackoverflow.com/users/20399258)** (2022-11-22): I have elaborated my query here: https://stackoverflow.com/questions/74532790/beautifulsoup-to-dataframe
