---
title: "Is there a really simple method for printing scraped output to a csv file?"
site: stackoverflow
question_id: 75803901
answer_id: 75803955
url: https://stackoverflow.com/a/75803955
author: "JNevill"
author_url: https://stackoverflow.com/users/2221001
posted: 2023-03-21T16:36:49Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1c15042ce3183b18008ba1abf77043c71345804c1a9c333cb0a06aef3155e7ca
role: another answer on the same question, kept as context; not my work
---

# Answer by [JNevill](https://stackoverflow.com/users/2221001) — 2023-03-21

Posted on Stack Overflow, <https://stackoverflow.com/a/75803955>, 2023-03-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Generate a list of lists with your data and dump that out to a csv:

    from bs4 import BeautifulSoup
    import requests
    import csv
    
    html_text = requests.get("https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963").text
    soup = BeautifulSoup(html_text, "lxml")
    cases = soup.find_all("div", class_ = "wrapper jcard has-padding-30 blocks has-no-bottom-padding")
    
    output = []
    for case in cases:
        case_title = case.find("div", class_ = "title-wrapper").text.replace(" "," ")
        case_plaintiff = case.find("td", {"data-th": "Plaintiff"}).text.replace(" "," ")
        case_defendant = case.find("td", {"data-th": "Defendant"}).text.replace(" "," ")
        case_number = case.find("td", {"data-th": "Case Number"}).text.replace(" "," ")
        case_filed = case.find("td", {"data-th": "Filed"}).text.replace(" "," ")
        court = case.find("td", {"data-th": "Court"}).text.replace(" "," ")
        case_nature_of_suit = case.find("td", {"data-th": "Nature of Suit"}).text.replace(" "," ")
        case_cause_of_action = case.find("td", {"data-th": "Cause of Action"}).text.replace(" "," ")
        jury_demanded = case.find("td", {"data-th": "Jury Demanded By"}).text.replace(" "," ")
    
        output.append([
                        case_title.strip()
                        ,case_plaintiff.strip()
                        ,case_defendant.strip()
                        ,case_number.strip()
                        ,case_filed.strip()
                        ,court.strip()
                        ,case_nature_of_suit.strip()
                        ,case_cause_of_action.strip()
                        ,jury_demanded.strip()
                      ])
    
    
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(output)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): Oops, I'm getting the following message - need to figure out what that means ;-) : Traceback (most recent call last):   File "C:\Users\cs\PycharmProjects\pythonProject1\beautsoup.py", line 36, in <module>     writer.writerows("output") TypeError: a bytes-like object is required, not 'str'
- **[JNevill](https://stackoverflow.com/users/2221001)** (2023-03-21): `writer.writerows(output)` instead. We don't want to write the word `"output"` to the file, we want to write the list-of-lists object stored in variable `output` to the file.
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-21): Not sure exactly what that means. But I changed the line with open("output.csv", "bw") as f:  to with open("output.csv", "w") as f:  and it works! I just hope that I've not committed an act that will cause the Pythonverse to melt down in doing that. Thanks so much to both you and AKX for your help!
- **[JNevill](https://stackoverflow.com/users/2221001)** (2023-03-21): *"Not sure exactly what that means."*: I was pointing out the diffferent in `writer.writerows("output")` and `write.writerows(output)`. You used the former, and it errored. I used the latter in my answer, and it should work fine.
