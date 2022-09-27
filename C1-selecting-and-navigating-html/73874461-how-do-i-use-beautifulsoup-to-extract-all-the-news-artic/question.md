---
title: "How do I use BeautifulSoup to extract all the news article urls from this webpage - https://indianexpress.com/article/technology/"
site: stackoverflow
question_id: 73874461
url: https://stackoverflow.com/q/73874461
asked: 2022-09-27T22:42:01Z
asked_by: "psico"
asked_by_url: https://stackoverflow.com/users/18084855
last_edited: never
tags: [python, web-scraping, url, beautifulsoup, python-requests]
score: -3
views_at_snapshot: 386
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 08858de2de807718cff1e8ce440c939b94b3829db453a1da812ee62f3c3602ca
---

# How do I use BeautifulSoup to extract all the news article urls from this webpage - https://indianexpress.com/article/technology/

Asked by [psico](https://stackoverflow.com/users/18084855) on Stack Overflow, <https://stackoverflow.com/q/73874461>, 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Noob trying to work on a news aggregation mini assignment using python.I use VSCode. 
I'm at the step where i'm supposed to grab all the news article urls from this link -  https://indianexpress.com/article/technology/

This is the basic code which is giving me every single link, but I only need the news article urls pls help

    from bs4 import BeautifulSoup
    page = requests.get('https://indianexpress.com/section/technology/')
    bSoup = BeautifulSoup(page.content, 'html.parser')
    links_list = bSoup.find_all('a')
    
    for link in links_list:
        if 'href' in link.attrs:
            print(str(link.attrs['href']) + "\n")

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[toppk](https://stackoverflow.com/users/4744864)** (2022-09-27): theres lots of ways to do this, you could use bs4 to navigate to the div containing the articles, but the simplest way is to do what you did, but just filter on `link.attr['href'].startswith('https://indianexpress.com/article/technology/')`
- **me** (2022-09-27): Just add `and 'article/' in link.attrs['href']` or `and link.attrs['href'].startswith('https://indianexpress.com/article/')` to your `if`
- **[psico](https://stackoverflow.com/users/18084855)** (2022-09-27): i'm sorry but im very bad at this, i don't understand how the final code will look like based on your solutions. can you just paste the code with the modification?
- **[psico](https://stackoverflow.com/users/18084855)** (2022-09-27): its returning True False True False True false as the output when i do     print(str(link.attrs['href'].startswith('https://indianexpress.com/article/')) + "\n")
- **me** (2022-09-28): @psico we meant use it as a CONDITION, not the actual output. Like `if 'href' in link.attrs and 'article/' in link.attrs['href']:....`
- **[psico](https://stackoverflow.com/users/18084855)** (2022-09-28): okay, will do that. thanks.
- **me** (2022-09-28): @psico your print statement was fine. Expect booleans to be meant for conditions most of the time; and also, I had `and` in my suggestion , which should have been another indication
