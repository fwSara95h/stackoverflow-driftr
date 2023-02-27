---
title: "Creating a dictionary in an existed dictionary by keeping keys python"
site: stackoverflow
question_id: 75583198
url: https://stackoverflow.com/q/75583198
asked: 2023-02-27T16:39:28Z
asked_by: "Donya"
asked_by_url: https://stackoverflow.com/users/8553867
last_edited: 2023-02-27T17:07:27Z
tags: [python, pandas, list, dictionary]
score: 0
views_at_snapshot: 74
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b330d11522cfbba33da2079a59281e75ae872c71c782f5719d31280472880a12
---

# Creating a dictionary in an existed dictionary by keeping keys python

Asked by [Donya](https://stackoverflow.com/users/8553867) on Stack Overflow, <https://stackoverflow.com/q/75583198>, 2023-02-27, last edited 2023-02-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this dictionary: 
```Python
Dialogues = {
   "dialogue_id": "000001", 
   "dialogue_turns": [
      { "turn_number": 0,
        "interlocutor_id": "0001",
        "turn_text": "Hi, how are you?" },
      { "turn_number": 1,
        "interlocutor_id": "0002",
        "turn_text": "Hi, I'm fine thanks. And you?" },
      { "turn_number": 2,
        "interlocutor_id": "0001",
        "turn_text": "I am good too, are you coming to the class today" },
      { "turn_number": 3,
        "interlocutor_id": "0002",
        "turn_text": "Yes, see you soon.bye" },
      { "turn_number": 4,
        "interlocutor_id": "0001",
        "turn_text": "bye" }
   ]
}
```

And I want to add a nested dictionary inside it by doing some counting on data as this:

```Python
Dialogues_analyzed = {
   "dialogue_id": "000001", 
   "dialogue_analysis": [
      {"interlocutor_id": "0001",
       "total_turns":"3",
       "total_words":"number of words in all turns of id=1"},
      {
         {"interlocutor_id": "0002",
          "total_turns":"2",
          "total_words":"number of words in all turns of id=2"}
      }
   ]
}
```

How can I get the output without nested for loops? I tried to make a new dictionary and then merge it to primary dictionary. However, I lost the keys in new dictionary.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ignatius Reilly](https://stackoverflow.com/users/15032126)** (2023-02-27): What do you mean by " I lost the keys in new dictionary"? If you tried a solution, show it even if it didn't worked as expected.
- **[Ignatius Reilly](https://stackoverflow.com/users/15032126)** (2023-02-27): In your example, the new dictionary is not _added_ to the previous one. Could you please shown _exactly_ how the desired output should look like?
