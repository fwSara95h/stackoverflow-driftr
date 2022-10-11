---
title: "How to extract data from unknown data type returned by BS html parser"
site: stackoverflow
question_id: 74030376
url: https://stackoverflow.com/q/74030376
asked: 2022-10-11T15:13:51Z
asked_by: "user3384929"
asked_by_url: https://stackoverflow.com/users/3384929
last_edited: 2022-10-12T15:46:54Z
tags: [python, beautifulsoup]
score: -2
views_at_snapshot: 147
answer_count: 1
accepted_answer_id: 74071424
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 032d0e612cba749f845b096cae6a49f77424c2820cf95d0f77b56140ebcb1db7
---

# How to extract data from unknown data type returned by BS html parser

Asked by [user3384929](https://stackoverflow.com/users/3384929) on Stack Overflow, <https://stackoverflow.com/q/74030376>, 2022-10-11, last edited 2022-10-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

https://docs.google.com/document/d/1qqhVYhuwQsR2GOkpcTwhLvX5QUBCj5tv7LYqXAzB2UE/edit?usp=sharing

The above document shows the output of BeautifulSoup after html parsing. This is a response from an API with POST request. In the website, it  renders as a table. 

Can anyone tell what is the data format and why find() and find_all() not working with it.


    # Import libs
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    import json
    
    # Reading codes from local CSV file on my computer
    dp_code = ("code.csv")
    
    # Form Data for passing to the request body
    formdata = {'objid': '14'}
    
    # URL
    url = "https://www.somewebsite.com"
    
    # Query
    for i in dp_code:
        formdata["objid"] = str(i)
        response = requests.request("POST", url, data=formdata, timeout=1500)
        out = response.content
        soup = BeautifulSoup(out,"html.parser")
        json = json.loads(soup.text)
        df = pd.DataFrame(bat["form"])
        df.to_csv(str(i) + ".csv")

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-12): It would help if you added more info - the parts of your code where you make the POST request, and what produced the contents of that doc (was it just a `print`?), the url...
- **me** (2022-10-12): Anyway, from what I could see in the doc, you're getting a json response with a `form` value that has all the unicode escaped; if you just used something like `response = requests.post...` you could try `formHtml = response.json()['form']` before passing to BeautifulSoup `formHtml` or `formHtml.replace('\/','/')` (because it looks like slashes were escaped as well, and they don't need to be)
- **[user3384929](https://stackoverflow.com/users/3384929)** (2022-10-12): I have added the code. But omitted the URL for security reasons
- **me** (2022-10-13): Did you try `BeautifulSoup(response.json()['form'].replace('\/','/'), "html.parser")` or  `BeautifulSoup(json.loads(response.content)['form'].replace('\/','/'), "html.parser")`  ?
- **me** (2022-10-13): was `response.content` what you saved in the doc?
- **[user3384929](https://stackoverflow.com/users/3384929)** (2022-10-13): response.content parsed the html parser then with json parser and the first element saved as dataframe, then the dataframe to csv.
- **me** (2022-10-14): what do `response.content` and `response.json()` return?
- **[user3384929](https://stackoverflow.com/users/3384929)** (2022-10-15): Thank you. I would have sent the original wesite address if there was a personal message option available here. I am a bit affraid of legal consequences of posting it publicly.
- **me** (2022-10-15): That's alright - as I said, I just wanted to know what the original response looked like. Hope my answer solved your issue and helped you understand the reasons behind it
