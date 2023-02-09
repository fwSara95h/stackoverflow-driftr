---
title: "How to create a dictionary with key and multiple values based on the data queried from database"
site: stackoverflow
question_id: 75403307
url: https://stackoverflow.com/q/75403307
asked: 2023-02-09T19:06:15Z
asked_by: "husain"
asked_by_url: https://stackoverflow.com/users/11985584
last_edited: 2023-02-09T19:07:11Z
last_editor: "Scott Hunter"
last_editor_url: https://stackoverflow.com/users/535275
tags: [python, dictionary]
score: 0
views_at_snapshot: 61
answer_count: 1
accepted_answer_id: 75404002
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 42b58757e110e126aa4a7262d04b85f14522cb84e340d149bea013aa071a7649
---

# How to create a dictionary with key and multiple values based on the data queried from database

Asked by [husain](https://stackoverflow.com/users/11985584) on Stack Overflow, <https://stackoverflow.com/q/75403307>, 2023-02-09, last edited 2023-02-09 by [Scott Hunter](https://stackoverflow.com/users/535275). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

New to python and was wondering how to create a dictionary with key and multiple values so that I can pass it to HTML to display it on the UI. Below is the data format. 

Questions from questions table - 

```
 [{'question_id': 1, 'question_text': 'How many servers run at max capacity?', 'category_id':  1, 'is_long_survey': 0}, 
    {'question_id': 2, 'question_text': 'Is the database getting replicated?', 'category_id': 1, 'is_long_survey': 0}, 
    {'question_id': 3, 'question_text': 'Where is the infrastructure located?', 'category_id': 1, 'is_long_survey': 0}]"
```

Choices for these questions come from choice table with question_id as the foreign key. 

    [{'choice_id' : 1, 'choice_text': '2', 'question_id': 1},
     {'choice_id' : 2, 'choice_text': '4', 'question_id': 1}, 
     {'choice_id' : 3, 'choice_text': '6', 'question_id': 1},
     {'choice_id' : 4, 'choice_text': 'Yes', 'question_id': 2},
     {'choice_id' : 5, 'choice_text': 'No', 'question_id': 2},
     {'choice_id' : 6, 'choice_text': 'global', 'question_id': 3},
     {'choice_id' : 7, 'choice_text': 'local', 'question_id': 3}]

So each question has lets say 3 choices as shown below. 

To display question text and their choices on the UI, how do I create a dictionary of question text as key and may be choices as multiple array values? Any other data structure I can use to format the data?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Scott Hunter](https://stackoverflow.com/users/535275)** (2023-02-09): You forgot to include your attempt to solve this problem.
- **[buran](https://stackoverflow.com/users/4046632)** (2023-02-09): Also, why not combine (join) the two queries into one and work from there? And what is the desired result at the end?
- **[husain](https://stackoverflow.com/users/11985584)** (2023-02-09): I tried with the join, but the result set has questions duplicated based on the choices. so thought it will be difficult to work form there.
- **[JonSG](https://stackoverflow.com/users/218663)** (2023-02-09): Are you concerned about performance? If not, iterate over `questions` and set a new key "choices" using `fliter()` based on `choices`.  Hopefully that gets you started
