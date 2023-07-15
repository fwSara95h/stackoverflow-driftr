---
title: "What is the difference between the list and list item in Beautiful Soup?"
site: stackoverflow
question_id: 76693965
url: https://stackoverflow.com/q/76693965
asked: 2023-07-15T13:24:20Z
asked_by: "rcLibrary"
asked_by_url: https://stackoverflow.com/users/22231938
last_edited: 2023-07-15T13:28:41Z
tags: [string, beautifulsoup, types]
score: -1
views_at_snapshot: 35
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5de1f3f16afdeae8129444315c8c622105043cb54218e2f7086aec292626839c
---

# What is the difference between the list and list item in Beautiful Soup?

Asked by [rcLibrary](https://stackoverflow.com/users/22231938) on Stack Overflow, <https://stackoverflow.com/q/76693965>, 2023-07-15, last edited 2023-07-15. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am writing code to take scraped HTML and turn it into wordcounts and eventually a word cloud. I am using Beautiful Soup to read the HTML file. 

I would like to pull the strings from all the h2 tags. 

To test getting a string I used: 

```
title = wheatleySoup.h2.text
print(type(title))
print(title)
```

which returned

```
<class 'str'>

      TO  M AE C E N A S.
```

However, when I add that title to a list:

```
wheatleyPoems = []
wheatleyPoems.append(title)
print(type(wheatleyPoems[0]))
print(wheatleyPoems)
``` 

I get the following:

```
<class 'str'>

['\n      TO\xa0\xa0M AE C E N A S.\n    ']
``` 

Why are these different? Is there a way to get the nice raw str (as shown in the first return) in a list? I know I can get the bs4.element.NavigableStrings into a list, but I'd like to just have str types if possible. 


The above was just testing the code and figuring out the data types. I would eventually need all the titles and will be using .find_all()

I have already built this code: 

```
titles = wheatleySoup.find_all('h2')

for item in titles:
  item=str(item)
  print(item)
  wheatleyTitles.append(item)
```

Which takes the bs4.element.NavigableStrings and turns them into str types. But, then I have a list that looks like this: 

```
['\n      TO\xa0\xa0M AE C E N A S.\n    ', '\n      O N\xa0\xa0V I R T U E.\n    ', '\n      TO THE UNIVERSITY OF CAMBRIDGE, IN NEW-ENGLAND.\n    ', '\n      TO THE KING’S MOST EXCELLENT MAJESTY. 1768.\n    ', '\n      ON BEING BROUGHT FROM AFRICA TO AMERICA.\n    ', '\n      ON THE DEATH OF THE REV. DR. SEWELL, 1769.\n
```

Instead of the nice clean strings I get when I use:

```
title = wheatleySoup.h2.text
print(type(title))
print(title)
```

Return:
```
<class 'str'>

      TO  M AE C E N A S.
```

as shown above. 

I have also used Beautiful Soup's .string to store the navigable strings in a list, but I would prefer to have str instead. 

I have also created a list as shown above and written a regex to clean it, I'm just wondering if I can cut down that step.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Reyot](https://stackoverflow.com/users/14526514)** (2023-07-15): Does this answer your question? [How to remove \xa0 from string in Python?](https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python)
- **[Reyot](https://stackoverflow.com/users/14526514)** (2023-07-15): It's really confusing what you are asking. `\n      TO\xa0\xa0M AE C E N A S.\n ` is raw string and `\      TO  M AE C E N A S.` is encoded string. When you print string, it will show you encoded string but when you print list with that string, it doesn't bother encoding it. The point is that string isn't changing. Your console is only changing the way it is showing you the value.
