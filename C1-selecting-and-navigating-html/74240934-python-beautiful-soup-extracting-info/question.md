---
title: "python: beautiful soup extracting info"
site: stackoverflow
question_id: 74240934
url: https://stackoverflow.com/q/74240934
asked: 2022-10-28T21:08:13Z
asked_by: "JFerro"
asked_by_url: https://stackoverflow.com/users/7168098
last_edited: never
tags: [python, beautifulsoup]
score: 1
views_at_snapshot: 61
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4a4b677d611a6c294878c03435c1ceb7ce28680b490f1d4b305fdc5eba329973
---

# python: beautiful soup extracting info

Asked by [JFerro](https://stackoverflow.com/users/7168098) on Stack Overflow, <https://stackoverflow.com/q/74240934>, 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am using beautiful soup to parse HTML as follows:

    html_content2 ="""
    <h3 style="cear: both;">
    <abbr title="European Union">EU</abbr>Investment</h3>
    <div class="conditions">
    <p>bla bla bla
    </p>
    </div>
    <p style="margin-bottom: 0;">
    <span class="amount">66000 €</span>
    </p>"""

I would like to extract the amount of money and the code I have is:

    from bs4 import BeautifulSoup
    html_content=html_content1
    soup = BeautifulSoup(html_content, "lxml")
    t3 = soup.find(lambda tag:tag.name=="h3" and ": Investment").find_next_sibling().find_next_sibling("p").find("span").contents
    print(t3)

The intention here is the following:
get h3 tag WITH text Investment and from there get next sibling and another next sibling with tag p then span and get the contents

In this previous code I dont how to include the word "Investiment" in the lambda function.
I tried:

    tag.name=="h3" and tag.contents==": Investment"

this does not work.
