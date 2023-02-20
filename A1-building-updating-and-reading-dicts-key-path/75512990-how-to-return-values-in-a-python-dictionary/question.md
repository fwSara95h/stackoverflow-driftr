---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
url: https://stackoverflow.com/q/75512990
asked: 2023-02-20T18:35:39Z
asked_by: "Mohamed Salem"
asked_by_url: https://stackoverflow.com/users/21252814
last_edited: 2023-02-21T09:38:29Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary, variables, calling-convention]
score: 3
views_at_snapshot: 15713
answer_count: 5
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 77908e9fa726d96dbb5c1ed0f1b5c51e61d6974bc2d6c1f233c25d2a9bdf6524
---

# how to return values in a python dictionary

Asked by [Mohamed Salem](https://stackoverflow.com/users/21252814) on Stack Overflow, <https://stackoverflow.com/q/75512990>, 2023-02-20, last edited 2023-02-21 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm fairly new to python and I am trying to work with a dictionary filled with keys that resemble the following layout:

```py
    dict = {
        'Tim': ['red', 'pizza', 'soda'],
        'Jake': ['green', 'burger', 'juice'],
        'Mary': ['blue', 'salad', 'water']
    }
```

How would I go about letting a user input a name and then set the contents of that person's information as values of variables in the code? 
For example, if a user chooses to view information about Jake, then:

```
    favoriteColor = green
    favoriteFood = burger
    favoriteDrink = juice
```



I really just don't know how to call specific values in this specific type dictionary in python. Would it be something similar to this:

```py
favoriteColor = dict.Jake[0]
favoriteFood = dict.Jake[1]
favoriteDrink = dict.Jake[2]
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jackal](https://stackoverflow.com/users/17580381)** (2023-02-20): Using lists like this is not a good pattern. See my answer for a different approach
- **[Thomas Kimber](https://stackoverflow.com/users/4137061)** (2023-02-21): It's no biggie, but I'd avoid naming your dictionary as `dict` - it wont break anything, but normally, dict is a reserved(ish) keyword that describes the dictionary data-type. In our house style guide, we often place an underscore_d at the end of the variable name if we want to signify something is a dict, like `person_preferences_d`, that way, the variables describe what they're about, but retain a signifier as to their "dict-ness".
