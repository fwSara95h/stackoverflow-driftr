---
title: "How to read table from url as DataFrame and modify format of data in one column in Python Pandas?"
site: stackoverflow
question_id: 74913448
url: https://stackoverflow.com/q/74913448
asked: 2022-12-25T13:03:48Z
asked_by: "dingaro"
asked_by_url: https://stackoverflow.com/users/12242085
last_edited: never
tags: [python, pandas, date, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 408
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5d9a80fc0c43e98dccbbd33537bb887811eb7ff1f493c331f5aa448358a45511
---

# How to read table from url as DataFrame and modify format of data in one column in Python Pandas?

Asked by [dingaro](https://stackoverflow.com/users/12242085) on Stack Overflow, <https://stackoverflow.com/q/74913448>, 2022-12-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a link to the website with table like the follow: https://www.timeanddate.com/holidays/kenya/2022 

How can I:
1. read this table as DataFrame in Jupyter Notebook in Python ?
2. Convert column "Date" so as to have date format like "01.01.2022" not as exists on website "1 sty"
3. how to create column "Day" where will be value like: sobota, niedziela and so on which currently are between columns "Date" and "Name" ?

So, as a result I need something like below:

Date       | Day       | Name           | Type
-----------|-----------|----------------|-------
01.01.2022 | sobota    | New Year's Day | Public holiday
20.03.2022 | niedziela | March Equinox  | Season
...        | ...       | ...            | ...

How can I do that in Python Pandas ?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[simpleApp](https://stackoverflow.com/users/15568504)** (2022-12-25): show us the code attempts you did so far? where you are unable to move forward?
- **[dingaro](https://stackoverflow.com/users/12242085)** (2022-12-25): I tried many solutions from internet, which did not work :/
- **[simpleApp](https://stackoverflow.com/users/15568504)** (2022-12-25): pls add your most recent code and also specify what's not working, so we can suggest the tweak you would need.
- **[simpleApp](https://stackoverflow.com/users/15568504)** (2022-12-25): for example, this is the starter code and then fix each need 1 by 1. `import pandas as pd df=pd.read_html("https://www.timeanddate.com/holidays/kenya/2022",attrs = {'id': 'holidays-table'}) df[0]=df[0].dropna(axis = 0, how = 'all') df[0].head(20)`
- **[dingaro](https://stackoverflow.com/users/12242085)** (2022-12-25): simpleApp, when I use your code I have error like that: AttributeError: module 'html5lib.treebuilders' has no attribute '_base'
- **[simpleApp](https://stackoverflow.com/users/15568504)** (2022-12-25): you have something else going on vs pandas error. [solve error](https://stackoverflow.com/questions/38447738/beautifulsoup-html5lib-module-object-has-no-attribute-base) pls look at these reference to fix the error. most likely you would need this `pip install --upgrade beautifulsoup4 pip install --upgrade html5lib`
- **[dingaro](https://stackoverflow.com/users/12242085)** (2022-12-25): simpleApp it is ok, but I still do not have idea how to convert date column to usefull form :/
