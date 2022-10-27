---
title: "scraping data and collecting all href values"
site: stackoverflow
question_id: 74216932
url: https://stackoverflow.com/q/74216932
asked: 2022-10-27T04:47:19Z
asked_by: "PutsandCalls"
asked_by_url: https://stackoverflow.com/users/5801127
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 132
answer_count: 1
accepted_answer_id: 74217161
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 84ed870cb8d4b55fc93e8db8ed9def7c7609980a33e49ffda07dcf452a0dbb91
---

# scraping data and collecting all href values

Asked by [PutsandCalls](https://stackoverflow.com/users/5801127) on Stack Overflow, <https://stackoverflow.com/q/74216932>, 2022-10-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape the following webpage: https://opensea.io/rankings?sortBy=total_volume

And I want to collect all the href values so for example: 

[![value to scrape][1]][1]


  [1]: https://i.sstatic.net/fb8Gr.png


However, it seems like I can't do it and I get some sort of error when using beautiful soup. This is the code that I have so far:

    page = requests.get("https://opensea.io/rankings?sortBy=total_volume").content
    soup = BeautifulSoup(page, 'html.parser')
    values = soup.findAll('a')

I'm not too sure why, but I would like to get all the values that is shown in the href values which contain the word "/collection/"

Would really appreciate some help.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rahul K P](https://stackoverflow.com/users/4407666)** (2022-10-27): You are redirected to an error page here.
