---
title: "How to deal with variations in web pages while web scrapping using Beautiful Soup"
site: stackoverflow
question_id: 76512508
url: https://stackoverflow.com/q/76512508
asked: 2023-06-20T07:55:32Z
asked_by: "Vedanta Mohapatra"
asked_by_url: https://stackoverflow.com/users/15384651
last_edited: 2023-06-20T12:57:03Z
tags: [python-3.x, beautifulsoup]
score: -1
views_at_snapshot: 27
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f7847a0619597c84a2cf43f8209ee9e07d7c3e64279600ba123982bc7482bb78
---

# How to deal with variations in web pages while web scrapping using Beautiful Soup

Asked by [Vedanta Mohapatra](https://stackoverflow.com/users/15384651) on Stack Overflow, <https://stackoverflow.com/q/76512508>, 2023-06-20, last edited 2023-06-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So, I was scrapping a website for an MRP Attribute. Now, I did something like this:
```
try:
    MRP = soup.find('div', class_ = 'X')
except AttributeError:
    MRP = ""
```
Now, the issue is the website doesn't have a consistent format throughout. Some pages have this price information somewhat differently like some don't have div class = 'X' at all. To deal with this, I put another `try-except` inside the first `try-except` block `except` part. It is working fine. But is there a better way to deal with this? I am not even sure if this is efficient.

I have only seen 2-3 variations of the page; there might be more. This will make the task difficult.

But, the consistent thing is the page displays `MRP: 100` across all its variants. So, is there a way to do it by considering this info so it won't break?

Edit:
What I wanted to say was websites has something like this, I want to extract the number beside MRP. Now, the thing is there are some variations as below. So, using soup's find method with hard corded class is causing the problems. So, I tried to incorporate the different variations with something like this:

    def get_MRP(soup):
        try:
            MRP = soup.find("span", attrs={"class":'a-price a-text-price a-size-base'}).span.text
        except AttributeError:
            try:
                MRP = soup.find("span", attrs={"class":'a-price a-text-price'}).span.text
            except AttributeError:
                MRP = ""
        return MRP

All I am asking if there is a better method to deal with this. As, this is a little bit hardcorded.

[![MRP Variation 1][1]][1]
[![MRP Variation][2]][2]


  [1]: https://i.sstatic.net/Ydimj.png
  [2]: https://i.sstatic.net/1ztvx.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2023-06-20): Please provide a [mre].
- **[Vedanta Mohapatra](https://stackoverflow.com/users/15384651)** (2023-06-20): @baduker Does my added edit help in any way? Sorry, for the trouble.
