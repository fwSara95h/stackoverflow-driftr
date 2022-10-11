---
title: "Extract Text from a word document"
site: stackoverflow
question_id: 74024323
url: https://stackoverflow.com/q/74024323
asked: 2022-10-11T07:17:19Z
asked_by: "Lalit Joshi"
asked_by_url: https://stackoverflow.com/users/19430670
last_edited: 2022-10-12T09:57:11Z
tags: [python, dataframe, beautifulsoup, selenium-chromedriver, python-docx]
score: 0
views_at_snapshot: 2036
answer_count: 1
accepted_answer_id: 74051264
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80580f80ec2bd0f1f7647ba2996c069a71e59ecaa914a889036fdbe001769c5c
---

# Extract Text from a word document

Asked by [Lalit Joshi](https://stackoverflow.com/users/19430670) on Stack Overflow, <https://stackoverflow.com/q/74024323>, 2022-10-11, last edited 2022-10-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape data from a word document available at:-
https://dl.dropbox.com/s/pj82qrctzkw9137/HE%20Distributors.docx 

I need to scrape the Name, Address, City, State, and Email ID. I am able to scrape the E-mail using the below code. 

        import docx
        
        content = docx.Document('HE Distributors.docx')
        
        location = []
        for i in range(len(content.paragraphs)):
            stat = content.paragraphs[i].text
            if 'Email' in stat:
                location.append(i)
    
    for i in location:
        print(content.paragraphs[i].text)


I tried to use the steps mentioned:
https://stackoverflow.com/questions/71703267/how-to-read-data-from-docx-file-in-python-pandas

I need to convert this into a data frame with all the columns mentioned above. 
Still facing issues with the same.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jthorpe](https://stackoverflow.com/users/1519199)** (2023-03-31): Consider using the [simplify-docx](https://github.com/microsoft/simplify-docx) package which simplifies away a lot of the structure of docx files that typically gets in the way of scraping documents for their content.
