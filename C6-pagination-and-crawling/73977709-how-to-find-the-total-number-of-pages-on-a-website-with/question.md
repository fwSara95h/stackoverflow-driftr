---
title: "How to find the total number of pages on a website with BeautifulSoup?"
site: stackoverflow
question_id: 73977709
url: https://stackoverflow.com/q/73977709
asked: 2022-10-06T17:15:46Z
asked_by: "theycallmepix"
asked_by_url: https://stackoverflow.com/users/12320089
last_edited: 2022-10-06T19:00:55Z
tags: [python, web-scraping, beautifulsoup, pagination]
score: -1
views_at_snapshot: 2836
answer_count: 2
accepted_answer_id: 73984323
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c0b7830968957d33d078ea7aadcb369a3b02d64a727e53619baf55f7bacee3cf
---

# How to find the total number of pages on a website with BeautifulSoup?

Asked by [theycallmepix](https://stackoverflow.com/users/12320089) on Stack Overflow, <https://stackoverflow.com/q/73977709>, 2022-10-06, last edited 2022-10-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Context: I'm working on pagination of this website: https://skoodos.com/schools-in-uttarakhand. When I inspected, this website has no proper number of pages visible except the `next button` which is `?page=2` after the url. Also, searching for `page-link` gave me number 20 at the end. So I assumed that the total number of pages is 20, upon checking manually, I learnt that, there only exist 11 pages. 

After many trials and errors, I finally decided to go with just the indexing from 0 until 12 (12 is excluded by python however).   
What I want to know is that, how wold you go about figuring out the number of pages on a particular website that doesn't show the actual number of pages other than `previous` and `next` button  and how can I optimize this in terms of the same?

Here's my solution to pagination. Any way to optimize this other than me manually finding the number of pages? 
```
from myWork.commons import url_parser, write


def data_fetch(url):
    school_info = []

    for page_number in range(0, 4):

        next_web_page = url + f'?page={page_number}'
        soup = url_parser(next_web_page)
        search_results = soup.find('section', {'id': 'search-results'}).find(class_='container').find(class_='row')

        # rest of the code
    for page_number in range(4, 12):

        next_web_page = url + f'?page={page_number}'
        soup = url_parser(next_web_page)
        search_results = soup.find('section', {'id': 'search-results'}).find(class_='container').find(class_='row')

        # rest of the code


def main():
    url = "https://skoodos.com/schools-in-uttarakhand"
    data_fetch(url)


if __name__ == "__main__":
    main()
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-07): Why have you split `data_fetch` into two separate but identical `for` loops? Is there any significance to the 0:4-4:12 split?
- **[theycallmepix](https://stackoverflow.com/users/12320089)** (2022-10-07): Yes, I had to do that as pages that are greater than 3 are a bit different compared to the starting 3.
