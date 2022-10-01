---
title: "Beautifulsoup output with indentation"
site: stackoverflow
question_id: 73915440
url: https://stackoverflow.com/q/73915440
asked: 2022-10-01T02:33:08Z
asked_by: "Outbound"
asked_by_url: https://stackoverflow.com/users/20134661
last_edited: never
tags: [beautifulsoup, python-3.7]
score: -1
views_at_snapshot: 420
answer_count: 1
accepted_answer_id: 73932397
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8b7b629ba6a64ad95dac4733209f65d477e5ffa2b71e5952430ea1f619c99398
---

# Beautifulsoup output with indentation

Asked by [Outbound](https://stackoverflow.com/users/20134661) on Stack Overflow, <https://stackoverflow.com/q/73915440>, 2022-10-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

New to Python webscraping and BeautifulSoup. 

I'd like to format the following so when it outputs the tags, it does so indented

    H1 text
       H2 text
          H3 text
       H2 text
       ...

etc. 

    from bs4 import BeautifulSoup
    import requests
    soup = BeautifulSoup(website.content, 'html.parser')
    tags = soup.find_all(['h1', 'h2'])
    for soups in tags:
    print(soups.string)

Your help is much appreciated.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[αԋɱҽԃ αмєяιcαη](https://stackoverflow.com/users/7658985)** (2022-10-01): soups.prettify()
- **[Outbound](https://stackoverflow.com/users/20134661)** (2022-10-03): Sadly this did not help.  I'm not sure how to use the 'soups.prettify()  If I don't use soups.string - but soups.prettify() I get the html code, not just the text.
