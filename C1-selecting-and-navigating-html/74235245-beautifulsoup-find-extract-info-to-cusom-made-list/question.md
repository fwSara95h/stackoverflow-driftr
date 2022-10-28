---
title: "BeautifulSoup find extract info to cusom-made list"
site: stackoverflow
question_id: 74235245
url: https://stackoverflow.com/q/74235245
asked: 2022-10-28T12:13:37Z
asked_by: "farid"
asked_by_url: https://stackoverflow.com/users/5437090
last_edited: 2022-10-28T12:21:57Z
tags: [python, html, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 68
answer_count: 2
accepted_answer_id: 74237349
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 17108dd03e528d19e431b1129682054438d494a0c3c9d6f8e30fc82e6ffe5927
---

# BeautifulSoup find extract info to cusom-made list

Asked by [farid](https://stackoverflow.com/users/5437090) on Stack Overflow, <https://stackoverflow.com/q/74235245>, 2022-10-28, last edited 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have 3 different type of`html` snippets which are part of a bigger part as follows:

    <html>
     <body>
      <span _ngcontent-dna-c199="" class="font-weight-bold">
       <span _ngcontent-dna-c199="" class="ng-star-inserted">
        <span _ngcontent-dna-c199="" translate="">
         issue_number
        </span>
        4 Näköispainos
       </span>
       <span _ngcontent-dna-c199="" class="ng-star-inserted">
        6.12.1939
       </span>
      </span>
     </body>
    </html>

and

    <html>
     <body>
      <span _ngcontent-sut-c199="" class="font-weight-bold">
       <span _ngcontent-sut-c199="" class="ng-star-inserted">
        <span _ngcontent-sut-c199="" translate="">
         issue_number
        </span>
        8
       </span>
       <span _ngcontent-sut-c199="" class="ng-star-inserted">
        1998
       </span>
      </span>
     </body>
    </html>

and

    <html>
     <body>
      <span _ngcontent-dgu-c199="" class="font-weight-bold">
       <span _ngcontent-dgu-c199="" class="ng-star-inserted">
        1905
       </span>
      </span>
     </body>
    </html>

Given the following code:

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml") # html_1, html_2, html_3
    res = soup.find("span", class_="font-weight-bold")
    print(res.text.split())

I get the following results:

    ['issue_number', '4', 'Näköispainos', '6.12.1939'] # html_1
    ['issue_number', '8', '1998']                      # html_2
    ['1905']                                           # html_3

However, my desired custom-made list should have 4 elements and looks like this:

    desired_list = ["issue_number", "number", "extension", "date"]

so if there is no info available in html snippet, I'd like to get `None` or simply `"-"` in that specific element of my desired custom list as follows:

    ['issue_number', '4', 'Näköispainos', '6.12.1939'] # html_1
    ['issue_number', '8', None, '1998']                # html_2
    [None, None, None, '1905']                         # html_3


Is there anyway to manipulate the result list to obtain the desired list using `soup.find()`?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[furas](https://stackoverflow.com/users/1832058)** (2022-10-28): you should search every element separatelly and then you have better control because when it can't find element then you can put `None`.
