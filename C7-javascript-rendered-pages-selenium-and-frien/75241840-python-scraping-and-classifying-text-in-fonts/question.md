---
title: "Python - Scraping and classifying text in \"fonts\""
site: stackoverflow
question_id: 75241840
url: https://stackoverflow.com/q/75241840
asked: 2023-01-26T02:37:16Z
asked_by: "Clara HL"
asked_by_url: https://stackoverflow.com/users/20705247
last_edited: 2024-08-07T06:40:03Z
last_editor: "VLAZ"
last_editor_url: https://stackoverflow.com/users/3689450
tags: [python, selenium-webdriver, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 123
answer_count: 1
accepted_answer_id: 75259313
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3033743500f0e23111295181e1f06e86a67ba8887fe3a7e066a9ace0453a8b13
---

# Python - Scraping and classifying text in "fonts"

Asked by [Clara HL](https://stackoverflow.com/users/20705247) on Stack Overflow, <https://stackoverflow.com/q/75241840>, 2023-01-26, last edited 2024-08-07 by [VLAZ](https://stackoverflow.com/users/3689450). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I would like to scrape the content of this website https://web.archive.org/web/20130318062052/http://internet.csr.nih.gov/Roster_proto1/member_roster.asp?srg=ACE&SRGDISPLAY=ACE&CID=102283 and create a table with the columns NAME, TITLE, LOCATION. I know some individuals have more or less "lines", but I am just trying to understand how I could even classify the first 3 lines for each person given that the text is in between "fonts" for all.

So far I have:

     url="https://web.archive.org/web/20130318062052/http://internet.csr.nih.gov/Roster_proto1/member_roster.asp?srg=ACE&SRGDISPLAY=ACE&CID=102283"
     driver.maximize_window()
     driver.implicitly_wait(5) # wait up to 3 seconds before calls to find elements time out
     driver.get(url)
    
     content = driver.page_source.encode('utf-8').strip()
     soup = BeautifulSoup(content,"html.parser")
    
     column = soup.find_all("font")


But once I am there and I have all the text within "font" in my "column" variable, I don't know how to proceed to differentiate between each person and build a loop where I would retrieve name, title, location etc. for each. 

Any help would be highly appreciated!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[tromgy](https://stackoverflow.com/users/9508635)** (2023-01-26): The way that document is structured makes it tough to analyze with BS4. I think you should look for pairs `<br><br>`, as those serve as separators for each record. A custom [function](https://beautiful-soup-4.readthedocs.io/en/latest/#a-function) might help.
- **[Clara HL](https://stackoverflow.com/users/20705247)** (2023-01-26): Thanks for your reply, would you have any idea about how to look for pairs of <br>, or using something else than BS? Thanks in advance
- **[atinjanki](https://stackoverflow.com/users/11631110)** (2023-01-27): Are you getting the text from font tags inside the table or you have not reached there ? The expected text appears to be inside the third table, within fint tags.
