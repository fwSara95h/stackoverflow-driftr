---
title: "TypeError: slice indices must be integers or None or have an __index__ method error in scraping a help page"
site: stackoverflow
question_id: 74951298
url: https://stackoverflow.com/q/74951298
asked: 2022-12-29T12:46:01Z
asked_by: "hanan"
asked_by_url: https://stackoverflow.com/users/11885361
last_edited: 2022-12-30T16:38:09Z
last_editor: "Community"
last_editor_url: https://stackoverflow.com/users/-1
tags: [python, python-3.x, web-scraping, beautifulsoup, python-requests]
score: -2
views_at_snapshot: 214
answer_count: 1
accepted_answer_id: 74961326
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e961fedacd04804b05ab3b87d0c0c28fa8726205957f076d47e1b1ae2e749cd2
---

# TypeError: slice indices must be integers or None or have an __index__ method error in scraping a help page

Asked by [hanan](https://stackoverflow.com/users/11885361) on Stack Overflow, <https://stackoverflow.com/q/74951298>, 2022-12-29, last edited 2022-12-30 by [Community](https://stackoverflow.com/users/-1). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I created python script to scrape **facebook** *help page*. I wanted to scrape `cms_object_id`, `cmsID`, `name`. so these values are in a script tag then firstly tried to find all `<script>` tags then tried to iterate over this and then there is `__bbox` inside the tags which contains the values wanted to scrape. 

so this is my script:

```
import json
import requests
import bs4
from Essentials import Static


class CmsIDs:
    def GetIDs():
        # cont = requests.get(""https://www.facebook.com:443/help"", headers=Static.headers) # syntax error
        cont = requests.get("https://www.facebook.com:443/help", headers=Static.headers)
        soup = bs4.BeautifulSoup(cont.content, "html5lib")

        text = soup.find_all("script")

        start = ""
        txtstr = ""

  

        for i in range(len(text)):
    
            mystr = text[i]

            # mystr = text[i]
            print("this is: ", mystr.find('__bbox":'))
            if text[i].get_text().find('__bbox":') != -1:
                # print(i, text[i].get_text())
                txtstr += text[i].get_text()
                start = text[i].get_text().find('__bbox":') + len('__bbox":')

        print('start:', start)

        count = 0
        for end, char in enumerate(txtstr[start:], start):
            if char == '{':
                count += 1
            if char == '}':
                count -= 1
            if count == 0:
                break
        print('end:', end)

        # --- convert JSON string to Python structure (dict/list) ---

        data = json.loads(txtstr[start:end+1])
        # pp.pprint(data)
        print('--- search ---')
        CmsIDs.search(data)

        # --- use recursion to find all 'cms_object_id', 'cmsID', 'name' ---

    def search(data):
        if isinstance(data, dict):
            found = False
            if 'cms_object_id' in data:
                print('cms_object_id', data['cms_object_id'])
                found = True
            if 'cmsID' in data:
                print('cmsID', data['cmsID'])
                found = True
            if 'name' in data:
                print('name', data['name'])
                found = True
            if found:
                print('---')
            for val in data.values():
                CmsIDs.search(val)
        if isinstance(data, list):
            for val in data:
                CmsIDs.search(val)


if __name__ == '__main__':
    CmsIDs.GetIDs()

```

the page contains `cms_object_id`, `cmsID`, `name`. so wanted to scrape all these 3 values but I am getting an error:

```
for end, char in enumerate(txtstr[start:], start):
TypeError: slice indices must be integers or None or have an __index__ method
```

so how can I solve this error and reach ultimate goal?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[deceze](https://stackoverflow.com/users/476)** (2022-12-30): Well, what does `print('start:', start)` give you…?
- **[hanan](https://stackoverflow.com/users/11885361)** (2022-12-30): @deceze it is empty and I don't know firstly working but not now.
