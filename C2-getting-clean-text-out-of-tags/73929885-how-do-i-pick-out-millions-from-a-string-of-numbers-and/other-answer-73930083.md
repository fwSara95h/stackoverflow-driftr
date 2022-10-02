---
title: "How do I pick out millions from a string of numbers and commas?"
site: stackoverflow
question_id: 73929885
answer_id: 73930083
url: https://stackoverflow.com/a/73930083
author: "bitflip"
author_url: https://stackoverflow.com/users/20027803
posted: 2022-10-02T23:50:06Z
last_edited: never
accepted: false
score: 4
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a605a568fb6492cee68222f577a6b0a19a9056e7c42e65dd52c48d0ea71be9e6
role: another answer on the same question, kept as context; not my work
---

# Answer by [bitflip](https://stackoverflow.com/users/20027803) — 2022-10-02

Posted on Stack Overflow, <https://stackoverflow.com/a/73930083>, 2022-10-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I'd suggest to change the code you used to extract the data and use this instead (which I feel like is a lot safer than trying to get the right cut offs in a string...):

get data:

    import requests
    from bs4 import BeautifulSoup
    resp = requests.get("https://finance.yahoo.com/quote/NUE/financials?p=NUE",
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})

parse data and select "Total Revenue" row

    soup = BeautifulSoup(resp.text, "html.parser")
    total_revenue = [row for row in soup.find("div", {"data-test": "fin-row"}) if "Total Revenue" in row.text]

now you can select your columns and work with them

    columns = total_revenue[0].find_all("div", {"data-test": "fin-col"})
    for col in columns:
        print(col.text)

output:

    42,965,391
    36,483,939
    20,139,658
    22,588,858
    25,067,279
