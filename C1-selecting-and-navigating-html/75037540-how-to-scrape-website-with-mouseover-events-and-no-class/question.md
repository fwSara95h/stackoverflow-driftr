---
title: "How to scrape website with mouseover events and no class on most elements"
site: stackoverflow
question_id: 75037540
url: https://stackoverflow.com/q/75037540
asked: 2023-01-07T01:36:10Z
asked_by: "tracemuch"
asked_by_url: https://stackoverflow.com/users/20949243
last_edited: 2023-01-07T13:33:16Z
last_editor: "imxitiz"
last_editor_url: https://stackoverflow.com/users/12446721
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 98
answer_count: 1
accepted_answer_id: 75037729
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d4530b81b779fdebf1b38a3889d2bdab6b3172a911f84d8604a348f3966c4e5e
---

# How to scrape website with mouseover events and no class on most elements

Asked by [tracemuch](https://stackoverflow.com/users/20949243) on Stack Overflow, <https://stackoverflow.com/q/75037540>, 2023-01-07, last edited 2023-01-07 by [imxitiz](https://stackoverflow.com/users/12446721). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape a table with data off a website with mouse-over color changing events and on each row only the first two columns have a class:
![Elements](https://i.sstatic.net/jX8DM.png)

Additionally, when I do try to scrape those first two rows I get the output as such:
![Output](https://i.sstatic.net/pDpif.png)

This is the code I am running.

```python
lists = soup.find_all('table', class_= "report")

for list in lists:
    date = list.find_all('td', class_= "time")
    flag = list.find_all('td', class_= "flag")
    info = [date, flag]
    print(info)
```

I was expecting to receive only the numerical values so that I can export them and work with them.  
I tried to use the `.replace()` function but it didn't remove anything.
I was unable to use `.text` even after converting date and flag to strings.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrew Ryan](https://stackoverflow.com/users/7451892)** (2023-01-07): Well date and flag themselves will return list objects which `.replace()` will not work on unless you access the particular item that you want to look at. (secondly you shouldn't name something `list` as that is a function keyword to turn elements into a list, instead do something like list_item in you for loop or just simply item) It is unclear what the problem / what you are doing to advise what you should be doing.
