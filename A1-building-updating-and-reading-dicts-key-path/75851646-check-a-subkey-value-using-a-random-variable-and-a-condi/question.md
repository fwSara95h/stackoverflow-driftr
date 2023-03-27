---
title: "Check a subkey value using a random variable and a condition. KeyError: \"x\""
site: stackoverflow
question_id: 75851646
url: https://stackoverflow.com/q/75851646
asked: 2023-03-27T02:10:28Z
asked_by: "Evangelos Dellas"
asked_by_url: https://stackoverflow.com/users/21374650
last_edited: 2023-03-27T02:19:42Z
last_editor: "cafce25"
last_editor_url: https://stackoverflow.com/users/442760
tags: [python, dictionary, key-value]
score: 0
views_at_snapshot: 111
answer_count: 2
accepted_answer_id: 75851696
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d5ca81a5707969de3382cdb39b59507ef1a19d9299b1c0d0d883dd2df889baa9
---

# Check a subkey value using a random variable and a condition. KeyError: "x"

Asked by [Evangelos Dellas](https://stackoverflow.com/users/21374650) on Stack Overflow, <https://stackoverflow.com/q/75851646>, 2023-03-27, last edited 2023-03-27 by [cafce25](https://stackoverflow.com/users/442760). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm having trouble with the dictionary code for checking the value of a subkey.

I want to get that:
- If `random_data` is a word that matches `"gender": "male"` then I want to print "Word is Male"
- If `random_data` is a word that matches `"gender": "female"`, then I want to print "Word is Female"


I think the problem is the row if `random_data == data["gender"]["male"]`, so I get the error:
```
KeyError: "gender"
```

How to fix?

```
import random

data = {

    #MALE
    "escritorio": {
        "gender": "male",
    },

    "viento": {
        "gender": "male",
    },

    #FEMALE
    "silla": {
        "gender": "female",
    },

    "mesa": {
        "gender": "female",
    },
    
}

#random key: escritorio or viento or silla or mesa
random_data =  random.choice(list(data))

if random_data == data["gender"]["male"]:
    print(random_data, ": word is Male")
else:
    print(random_data, ": word is Female") 

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jasonharper](https://stackoverflow.com/users/1709364)** (2023-03-27): What are you expecting `data["gender"]` to do?  That's not one of the words in your dictionary.  And even if it existed, it wouldn't be another dictionary containing `"male"` as a key.  You want `random_data["gender"] == "male"`.
- **[Evangelos Dellas](https://stackoverflow.com/users/21374650)** (2023-03-27): @jasonharper Thanks, but now using your code i get error:     if random_data["gender"] == "male": TypeError: string indices must be integers
- **me** (2023-03-27): @jasonharper `random_data` is a string not a dictionary `list(<dict>)` just returns a list of keys
