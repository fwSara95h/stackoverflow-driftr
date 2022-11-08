---
title: "Getting a dictionary from web-scrapping data sets"
site: stackoverflow
question_id: 74354618
url: https://stackoverflow.com/q/74354618
asked: 2022-11-08T01:05:02Z
asked_by: "Flow"
asked_by_url: https://stackoverflow.com/users/20423609
last_edited: never
tags: [python, web-scraping, beautifulsoup, code-formatting]
score: -1
views_at_snapshot: 352
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 287c7642fbe4d84cd548908b3c9d2281e9f893e24e022c0b714f9b53ada1eb0b
---

# Getting a dictionary from web-scrapping data sets

Asked by [Flow](https://stackoverflow.com/users/20423609) on Stack Overflow, <https://stackoverflow.com/q/74354618>, 2022-11-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
table = soup.find('table')

list_of_states = table.find_all('tr')

for state in list_of_states:
    state_name = state.find('td')
    if state_name is None:
        continue
    hours = state.find_all('td')[1].text

    comparison_state = str(state_name.text.strip().lower())
    sunlight = float(hours.split()[0])

dict = {comparison_state : 1, sunlight : 2}
```



Alright, I am trying to have the state_name and hours associated, like first state_name = first hours...etc. As you can see, the comparison_state is the string of state names, but if you print that it prints all of them, not just one; same thing with the sunlight. The for loop finds the state names and the hours associated already, but how do I put that into a dictionary or array of dictionaries, that I can then use with user input. For example, if the user entered "Washington", they got the hours associated with that state.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-11-09): this would be much easier if you would share the link or html you're working with
