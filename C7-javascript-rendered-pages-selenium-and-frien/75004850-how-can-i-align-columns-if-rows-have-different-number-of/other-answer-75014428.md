---
title: "How can I align columns if rows have different number of values?"
site: stackoverflow
question_id: 75004850
answer_id: 75014428
url: https://stackoverflow.com/a/75014428
author: "Easty77"
author_url: https://stackoverflow.com/users/2070127
posted: 2023-01-05T06:09:02Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 337dbbbd6d92d03810f30a740d3e9a868e23263e51c93d3724eb49c26505fb67
role: another answer on the same question, kept as context; not my work
---

# Answer by [Easty77](https://stackoverflow.com/users/2070127) — 2023-01-05

Posted on Stack Overflow, <https://stackoverflow.com/a/75014428>, 2023-01-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I think it is worth working a little bit harder to get your data rationalised before putting it in the csv rather than trying to unpick the damage once ragged data has been exported.

A quick look at each record in the page suggests that there are five main items that you want to export and these correspond to the five top-level divs in the a element.

The complexity (as you note) comes because there are sometimes two statuses specified, and in that case there is sometimes a separate date range for each and sometimes a single date range.

I have therefore chosen to put the three ever present fields as the first three columns, followed next by the status + date range columns as pairs.  Finally I have removed the field names (these should effectively become the column headings) to leave only the variable data in the rows. 

    initiatives = [processDiv(item) for item in initiative_item]
    
    def processDiv(item):
        divs = item.find_elements(By.XPATH, "./article/a/div")
        if "\n" in divs[0].text:
            statuses = divs[0].text.split("\n")
            if len(divs) > 5:
                return [divs[1].text, divs[2].text.split("\n")[1], divs[3].text.split("\n")[1], statuses[0], divs[4].text.split("\n")[1], statuses[1], divs[5].text.split("\n")[1]]
            else:
                return [divs[1].text, divs[2].text.split("\n")[1], divs[3].text.split("\n")[1], statuses[0], divs[4].text.split("\n")[1], statuses[1], divs[4].text.split("\n")[1]]
        else:        
            return [divs[1].text, divs[2].text.split("\n")[1], divs[3].text.split("\n")[1], divs[0].text, divs[4].text.split("\n")[1]]

The above approach sticks as close to yours as I can.  You will clearly need to rework the pandas code to reflect the slightly altered data structure.  

Personally, I would invest even more time in clearly identifying the best definitions for the fields that represent each piece of data that you wish to retrieve (rather than as simply divs 0-5), and extract the text directly from them (rather than messing around with split).  In this way you are far more likely to create robust code that can be maintained over time (perhaps not your goal).
