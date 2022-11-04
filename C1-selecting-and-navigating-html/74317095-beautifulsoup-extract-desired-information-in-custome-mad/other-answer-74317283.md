---
title: "BeautifulSoup extract desired information in custome-made list from different html snippets"
site: stackoverflow
question_id: 74317095
answer_id: 74317283
url: https://stackoverflow.com/a/74317283
author: "svfat"
author_url: https://stackoverflow.com/users/2419628
posted: 2022-11-04T12:45:52Z
last_edited: 2022-11-04T13:01:30Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6726f239f1d7d7a9af13e4289a4fc8dc0cd6ecbabe7261e6aebd10198cd01720
role: another answer on the same question, kept as context; not my work
---

# Answer by [svfat](https://stackoverflow.com/users/2419628) — 2022-11-04

Posted on Stack Overflow, <https://stackoverflow.com/a/74317283>, 2022-11-04, last edited 2022-11-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I am not providing a solution but this is a clue. If you have a fixed structure and you don't have a way to distinguish between them. I suggest using [soup.find_all()][1] to extract all items with class "ng-star-inserted" and then add them to the list in the desired order:


  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

You can print them all like this:
```
    result = soup.find_all("span", "ng-star-inserted")
    for position, element in enumerate(result):
        print(el)
```
That will iterate over tuples of (position, element) in the list.
Then you need to figure out the location of the desired element, and put it into the appropriate position, for example:
``` 
    if position == you_need_to_figure_this_out:
        desired_list[desired_position] = element
```

If you can't map positions to elements, you need some heuristics to guess them.

"page" is easy ```if el.text.isdigit()``` then it is a "page" 

"publisher" and "city" is harder, but it looks like there is always a "publisher", so the first string (without elements that are already processed in your question's code) will be a "publisher", and the second non-processed (if it exists) is a "city"

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[farid](https://stackoverflow.com/users/5437090)** (2022-11-04): The problem is `find_all` does not return a list with length of 6 to enumerate! That is why I wrote a very high school ish approach using for loop to handle this!
- **[svfat](https://stackoverflow.com/users/2419628)** (2022-11-04): I see, I would somehow guess the position for the "publisher", "city", "page"  page is easy ```if el.text.isdigit()``` then it is a page   publisher and city is harder, but it looks like there is always a publisher, so the first string (without elements that are already processed in your question's code) will be a publisher, and second non-processed (if exists) is a city
- **[farid](https://stackoverflow.com/users/5437090)** (2022-11-04): Actually it is very stochastic in which there can happen any of these info be `None `. So city, publisher, or anything else! these are just three samples I provided to clarify what I aim for as `desired_list`
