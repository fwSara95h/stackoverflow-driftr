---
title: "How to convert json file to csv file in python"
site: stackoverflow
question_id: 75586203
url: https://stackoverflow.com/q/75586203
asked: 2023-02-27T22:33:19Z
asked_by: "ibrahim maghfoul"
asked_by_url: https://stackoverflow.com/users/14560147
last_edited: 2023-02-27T22:42:06Z
tags: [python, json, python-3.x, csv, data-conversion]
score: -1
views_at_snapshot: 1776
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d2d43c41f9512b63eccca6faf087b9e6ae4817d58311a49215d4b5b547f8e97f
---

# How to convert json file to csv file in python

Asked by [ibrahim maghfoul](https://stackoverflow.com/users/14560147) on Stack Overflow, <https://stackoverflow.com/q/75586203>, 2023-02-27, last edited 2023-02-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this json file which contains a list of objects 
```
[ {
    "infos": [
      { "localisation": "Kassel" },
      { "date": "01.08.2023" },
      { "places": "1 freier Platz" }
    ],

    "applying email": "exemple@starke.ma",
    "additional infos": { 
       "name": "jhon", 
       "position": "RH", 
       "email": "email@email.com" }
  },
  {
    "infos": [
      { "places": "1 freier Platz" }
    ],
    "applying email": "",
    "applying link": "www.exemple.com",
    "additional infos": {
       "name": "jhon", 
       "position": "RH", 
       "email": "email@email.com"
    }
  },] 
```
and I want to convert it into csv file (the object contains other fields but I wanted to make is as simple as possible)  the problem is that the file contains nested objects and some field in the nested objects are missing from other objects in the list as what you can see in the infos fields (in the first item on the list you can see a localisation field under the infos field but it's missing in the second object of the list), what i want to achieve is that my csv file header will contain all the field (the missing ones too) and if it didn't find that missing field in the json object while appending data to it , i want to ignore it and let the place empty

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[wescpy](https://stackoverflow.com/users/305689)** (2023-02-28): One issue you have is that a CSV file is generally a flat piece of 2D-structured data whereas JSON is more tree-like in nature and doesn't necessarily "translate" into rows of columns easily. While someone can give you an answer for the specific use-case you describe, it likely can't be universally-applied for all JSON data, so you should be more specific in your question.
