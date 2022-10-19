---
title: "Any easy way to extract details from a HTM webpage?"
site: stackoverflow
question_id: 74129022
url: https://stackoverflow.com/q/74129022
asked: 2022-10-19T16:44:26Z
asked_by: "Andrew Hicks"
asked_by_url: https://stackoverflow.com/users/13084623
last_edited: never
tags: [python, beautifulsoup]
score: -1
views_at_snapshot: 72
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a41d591b111330e0918cb6d6e9e93d968543e805fd8cf6d10d83ae1990a9118
---

# Any easy way to extract details from a HTM webpage?

Asked by [Andrew Hicks](https://stackoverflow.com/users/13084623) on Stack Overflow, <https://stackoverflow.com/q/74129022>, 2022-10-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to extract the following address from the 10-Q on this webpage and need help getting it to work: https://www.sec.gov/ix?doc=/Archives/edgar/data/1318605/000095017022012936/tsla-20220630.htm

1 Tesla Road
Austin, Texas

    URL = f'https://www.sec.gov/ix?doc=/Archives/edgar/data/{cik}/{accessionNumber}/{primaryDocument}'
    response = requests.get(URL, headers = headers)
    soup = BeautifulSoup(response.content, "html.parser")
    soup.find_all('dei:EntityAddressAddressLine1')

Where:

 - cik = 0001318605 
 - accessionNumber = 000095017022012936 
 - primaryDocument
   = tsla-20220630.htm

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[nigh_anxiety](https://stackoverflow.com/users/17030540)** (2022-10-19): It looks like that page is relying heavily on JavaScript to load the page contents, so you're going have to use a webdriver and a tool like Selenium to actually load the pages you want in a browser in order to generate the content.
