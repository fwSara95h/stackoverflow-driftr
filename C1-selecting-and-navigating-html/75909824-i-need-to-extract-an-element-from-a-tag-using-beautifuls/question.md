---
title: "I need to extract an element from a tag using BeautifulSoup4"
site: stackoverflow
question_id: 75909824
url: https://stackoverflow.com/q/75909824
asked: 2023-04-02T02:30:02Z
asked_by: "WhoIsJonGalt"
asked_by_url: https://stackoverflow.com/users/1565926
last_edited: 2023-04-02T07:04:09Z
last_editor: "Marcelo Paco"
last_editor_url: https://stackoverflow.com/users/11286032
tags: [html, beautifulsoup, tags, gettext]
score: 0
views_at_snapshot: 62
answer_count: 1
accepted_answer_id: 75910101
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0d8ed36b115a2b6043a142dda620ee8e3bec2f26d8e4c5400b4fbb769be0d954
---

# I need to extract an element from a tag using BeautifulSoup4

Asked by [WhoIsJonGalt](https://stackoverflow.com/users/1565926) on Stack Overflow, <https://stackoverflow.com/q/75909824>, 2023-04-02, last edited 2023-04-02 by [Marcelo Paco](https://stackoverflow.com/users/11286032). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Simply put, I have the below tag in my soup and I need to extract the date from the `'value'` element.

    <input class="mm-date-field form-control input-sm date-picker" title="Select as of date" type="text" value="03/31/2023"/>



I've tried a number of things after searching online, but my latest attempts were the below:

    date = cmbs_soup.find('input', title = 'Select as of date', type = 'text', value = re.compile('.*'))
    date.text

    date = cmbs_soup.find('input', {"class": "mm-date-field form-control input-sm date-picker", "title": "Select as of date", "type": "text"}).get_text("value")
    print(date)

Both resulted in `''` - an **empty string**. What am I missing?!?! 

Ty!
