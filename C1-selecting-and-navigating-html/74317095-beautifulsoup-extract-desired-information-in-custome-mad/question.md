---
title: "BeautifulSoup extract desired information in custome-made list from different html snippets"
site: stackoverflow
question_id: 74317095
url: https://stackoverflow.com/q/74317095
asked: 2022-11-04T12:29:52Z
asked_by: "farid"
asked_by_url: https://stackoverflow.com/users/5437090
last_edited: 2022-11-04T15:46:28Z
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 44
answer_count: 2
accepted_answer_id: 74331712
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7fc1f8066e67dda0ef9eb411f25b69de35041246832bfe70b6dd7629d4f7a2c8
---

# BeautifulSoup extract desired information in custome-made list from different html snippets

Asked by [farid](https://stackoverflow.com/users/5437090) on Stack Overflow, <https://stackoverflow.com/q/74317095>, 2022-11-04, last edited 2022-11-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Apologies in advance for such a long and basic question!

Given the following three `html` snippets which are part of a bigger part as follows:

    <html>
     <body>
      <span _ngcontent-ont-c199="" class="font-weight-bold">
       <span _ngcontent-ont-c199="" class="ng-star-inserted">
        <span _ngcontent-ont-c199="" translate="">
         nro
        </span>
        4 A.
       </span>
       <!-- -->
       <span _ngcontent-ont-c199="" class="ng-star-inserted">
        6.12.1939
       </span>
       <!-- -->
      </span>
      <span _ngcontent-ont-c199="" class="ng-star-inserted">
       , JR 10
      </span>
      <!-- -->
      <!-- -->
      <span _ngcontent-ont-c199="" class="ng-star-inserted">
       :
       <span _ngcontent-ont-c199="" translate="">
        sivu
       </span>
       1
      </span>
     </body>
    </html>

and

    <html>
     <body>
      <span _ngcontent-evu-c199="" class="font-weight-bold">
       <!-- -->
       <span _ngcontent-evu-c199="" class="ng-star-inserted">
        1905
       </span>
       <!-- -->
      </span>
      <span _ngcontent-evu-c199="" class="ng-star-inserted">
       , Aksel Paul
      </span>
      <!-- -->
      <span _ngcontent-evu-c199="" class="ng-star-inserted">
       , Helsinki
      </span>
      <!-- -->
      <span _ngcontent-evu-c199="" class="ng-star-inserted">
       :
       <span _ngcontent-evu-c199="" translate="">
        page
       </span>
       63
      </span>
     </body>
    </html>

and

    <html>
     <body>
      <span _ngcontent-ejj-c199="" class="badge badge-secondary ng-star-inserted">
       22
      </span>
      <span _ngcontent-dna-c199="" class="font-weight-bold">
       <span _ngcontent-dna-c199="" class="ng-star-inserted">
        <span _ngcontent-dna-c199="" translate="">
         nro
        </span>
        12 ZZ
       </span>
       <span _ngcontent-dna-c199="" class="ng-star-inserted">
        10.2016
       </span>
      </span>
      <span _ngcontent-ejj-c199="" class="ng-star-inserted">
       , Arbetarförlaget Ab
      </span>
      <!-- -->
      <span _ngcontent-ejj-c199="" class="ng-star-inserted">
       , Stockholm
      </span>
      <!-- -->
      <span _ngcontent-ejj-c199="" class="ng-star-inserted">
       :
       <span _ngcontent-ejj-c199="" translate="">
        sida
       </span>
       20
      </span>
     </body>
    </html>

I would like to extract 6 different information (if available otherwise `None`) using a desired list which looks as follows:

    desired_list = ["badge", "issue", "date", "publisher", "city", "page"]

So I have the following code (very inefficient using for loop):

    desired_list = [None]*6 # initialize with [None, None, None, None, None, None]

    soup = BeautifulSoup(html, "lxml") # html_1, html_2, html_3

    fwb = soup.find("span", class_="font-weight-bold")
    issue_date = fwb.select("span.ng-star-inserted") # always a list of 2 elements: ['nro XX extension', 'DD.MM.YYYY']

    for el in issue_date:
        element = el.text.split()
        if "nro" in element:
            desired_list[1] = " ".join(element) # handling issue: nro XX extension
        desired_list[2] = " ".join(element) # handling date: DD.MM.YYYY
    badge = soup.find("span", class_="badge badge-secondary ng-star-inserted")
    if badge: desired_list[0] = " ".join(badge.text.split()) # handling badge

Currently, I can only extract info for first three components in my `desired_list`, namely, `badge`, `issue`, `date`. 

    [None, 'nro 4 A.', '6.12.1939', None, None, None] # html_1
    [None, None, '1905', None, None, None]            # html_2
    ['22', 'nro 12 ZZ', '10.2016', None, None, None]  # html_3

Whereas, my desired list for each `html` should looks like this:

    [None, 'nro 4 A.', '6.12.1939', 'JR 10', None, 'sivu 1']                     # html_1
    [None, None, '1905', 'Aksel Paul', 'Helsinki', 'page 63']                    # html_2
    ['22', 'nro 12 ZZ', '10.2016', 'Arbetarförlaget Ab', 'Stockholm', 'sida 20'] # html_3

And I don't know how to manipulate my code to retrieve all 6 fields given the aforementioned `html` snippets since their occurrences are very stochastic meaning that it can happen some information is missing. I really appreciate if someone can recommend me smarter and more efficient way of handling this.

I am aware of `soup.find_all("span", class_="ng-star-inserted")`. However, the problem is that `find_all` does not always return a list with length of 6 to enumerate!

Cheers,
