---
title: "How to parse <script> tag using beautifulsoup"
site: stackoverflow
question_id: 74987702
url: https://stackoverflow.com/q/74987702
asked: 2023-01-02T22:52:05Z
asked_by: "Dunc"
asked_by_url: https://stackoverflow.com/users/20907457
last_edited: 2023-01-02T22:55:03Z
tags: [python, json, string, beautifulsoup]
score: 4
views_at_snapshot: 659
answer_count: 3
accepted_answer_id: 74987806
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 53f041223e354e90bbc298d21343ec2585f0ec03bf9325445a0bd11380d9ff27
---

# How to parse <script> tag using beautifulsoup

Asked by [Dunc](https://stackoverflow.com/users/20907457) on Stack Overflow, <https://stackoverflow.com/q/74987702>, 2023-01-02, last edited 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to read the `window.appCache` from a glassdoor reviews site.

```
url = "https://www.glassdoor.com/Reviews/Alteryx-Reviews-E351220.htm"
html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) 
soup = BeautifulSoup(html.content,'html.parser') 
text = soup.findAll("script")[0].text
```

This isolates the dict I need however when I tried to do `json.loads()` I get the following error:
 
```
raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) 
```

I checked the type of `text` and it is `str`.

When I print `text` to a file, it looks something like this (just a snippet as the output is about 5000 lines):

```
window.appCache={"appName":"reviews","appVersion":"7.14.12","initialState"
{"surveyEndpoint":"https:\u002F\u002Femployee-pulse-survey-b2c.us-east-1.prod.jagundi.com",
"i18nStrings":{"_":"JSON MESSAGE BUNDLE - do not remove",
"eiHeader.seeAllPhotos":"
See All Photos","eiHeader.viewJobs":"View Jobs",
"eiHeader.bptw.description":"This employer is a winner of the [year] Best Places to Work award. 
Winners were determined by the people who know these companies best...
```

I am only concerned with the `"reviews":[` field that is buried about halfway through the data, but I can't seem to parse the string into json and retrieve what I need.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[dskrypa](https://stackoverflow.com/users/19070573)** (2023-01-02): You most likely need to do something like `json.loads(text.split('=', 1)[1].strip())`, but it may require more string manipulation to isolate the portion that you need.
- **[dskrypa](https://stackoverflow.com/users/19070573)** (2023-01-02): Sometimes, the easiest way to extract something from a script tag, once you have the raw text, is to just use [regex](https://docs.python.org/3/library/re.html)
