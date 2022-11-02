---
title: "Extract data from Dell Community Forum for a specific date"
site: stackoverflow
question_id: 74292169
url: https://stackoverflow.com/q/74292169
asked: 2022-11-02T15:58:39Z
asked_by: "NApStor"
asked_by_url: https://stackoverflow.com/users/20399258
last_edited: never
tags: [python, web-scraping, beautifulsoup, csvwriter]
score: 0
views_at_snapshot: 92
answer_count: 2
accepted_answer_id: 74293454
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 03fabefc74ec5af900759b1e1e1d1ad01913120b4cc95bb0cc0a855045bd58f9
---

# Extract data from Dell Community Forum for a specific date

Asked by [NApStor](https://stackoverflow.com/users/20399258) on Stack Overflow, <https://stackoverflow.com/q/74292169>, 2022-11-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to extract the username, post title, post time and the message content from a Dell Community Forum thread of a particular date and store it into an excel file.

For example,
URL: https://www.dell.com/community/Inspiron-Desktops/I-am-getting-time-sync-errror-and-the-last-synced-time-shown-as/m-p/8290678#M36017

I want to extract the post title: "I am getting time sync errror and the last synced time shown as a day in 2015"

And details(username, post time, message) of comments for the date 10-25-2022 only

1. jraju, 04:20 AM, "This pc is desktop inspiron 3910 model . The dell supplied only this week."
2. Mary G, 09:10 AM, "Try rebooting the computer and connecting to the internet again to see if that clears       it up.
   Don't forget to run Windows Update to get all the necessary updates on a new computer."
3. RoHe, 01:00 PM, "You might want to read Fix: Time synchronization failed on Windows 11. Totally ignore the part about downloading the software tool, and scroll down that same page to the part: How to manually sync time on a Windows 11 PC. NOTE: In step #6, if time.windows.com doesn't work, pick a different server from the drop-down menu on that screen."

Not any other comments.

I'm very new to this.

Till now I've just managed to extract information(no username) without the date filter.

I'm very new to this.

Till now I've just managed to extract information(no username) without the date filter.

```

import requests
from bs4 import BeautifulSoup

url = "https://www.dell.com/community/Inspiron-Desktops/I-am-getting-time-sync-errror-and-the-last-synced-time-shown-as/m-p/8290678#M36017"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

###### time ######
time = doc.find_all('span', attrs={'class':'local-time'})
print(time)
##################

##### date #######
date = doc.find_all('span', attrs={'class':'local-date'})
print(date)
#################

#### message ######
article_text = ''
article = doc.find_all("div", {"class":"lia-message-body-content"})
for element in article:
    article_text += '\n' + ''.join(element.find_all(text = True))
    
print(article_text)
##################
all_data = []
for t, d, m in zip(time, date, article):
    all_data.append([t.text, d.get_text(strip=True),m.get_text(strip=True, separator='\n')])

with open('data.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in all_data:
        writer.writerow(row)
```
