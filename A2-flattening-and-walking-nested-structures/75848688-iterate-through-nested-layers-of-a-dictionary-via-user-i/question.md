---
title: "Iterate through nested layers of a dictionary via user input python"
site: stackoverflow
question_id: 75848688
url: https://stackoverflow.com/q/75848688
asked: 2023-03-26T15:25:29Z
asked_by: "Sphenoidale"
asked_by_url: https://stackoverflow.com/users/17817552
last_edited: never
tags: [python, json, dictionary]
score: -1
views_at_snapshot: 95
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dc44e462ce4cc3342e5e1ae701714591fe42ebfc231b6e13ca56c52acbb9f00a
---

# Iterate through nested layers of a dictionary via user input python

Asked by [Sphenoidale](https://stackoverflow.com/users/17817552) on Stack Overflow, <https://stackoverflow.com/q/75848688>, 2023-03-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

posted a similar question before, however, the conditions changes a bit so that I want to rephrase it.

I have the following dict structure:

```
[{
        "id": "id01",
        "system": 
                    {
                    "0": "initial question \n Choice A \n Choice B",
                    "1": {"0": "Answer Choice A\n Second Choice C \n Second Choice D",
                          "1":"Final Answer Choice AC", 
                          "2":"Final Answer Choice AD"},
                    "2": {"0": "Answer Choice B\n Second Choice A \n Second Choice B", 
                          "1": "Final Answer Choice BA", 
                          "2":"Final Answer Choice BB"}
                    }         
    
}]
```
It is a tree like dictonary, where the user can iterate through via console inputs.
Thats my code:

```
while True:
            qloop = input("Select an option: ", )

            if qloop == "R":
                break
            else:
                print(data[i]["system"][qloop]) #here I want to use the qloop input to stepwise iterate through the nested layers of my tree-like dict.
            break
        if qloop == "R":
            continue
        else:
            break
```

So, I over my console the user is asked to make a choice for an item (in this example "id01"). Lets say the user types "1" after the inital question the code should print Answer Choice A and then again the user can choose until the end of one path in this decision tree like dict is reached.

Any ideas how I can achieve that, resp. it would be a great bonus if you could also undo your choices stepwise with lets say the "R" key.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Samwise](https://stackoverflow.com/users/3799759)** (2023-03-26): In your example, it looks like sometimes you have a list of dictionaries with an `id` key, and sometimes you have a dictionary with numbered options.  Are there other ways the nested dictionaries might be formatted?  It's not easy to write code that can handle completely arbitrary structures in a way that's user-friendly, but if you come up with a regular format and use it consistently it's easy.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-26): Not a code writing service, but I'll answer in general terms since it's a general question. Simple recursion is your answer. Write a function that takes a dict. Present the keys as choices, then returns the key-value as the result. If the value is a dict, call the function again with that dict.
- **[OysterShucker](https://stackoverflow.com/users/10292330)** (2023-03-26): Your `0` entry should be: `"0": {"0":"initial question \n Choice A \n Choice B"}`. You are changing your structure based on the amount of possibilities, and it is going to give you nothing but headaches.
- **me** (2023-03-26): @OneMadGypsy I think `"0"` is always supposed to be keyed a question, so it's fine. Would be better to explicitly have a `{'prompt':str, 'choices':[choice_1_dict, choice_2_dict,...]}` structure though
- **[Jamiu S.](https://stackoverflow.com/users/19290081)** (2023-03-27): Does this answer your question? [Iterate through dict hierarchy in json with python loop](https://stackoverflow.com/questions/75817241/iterate-through-dict-hierarchy-in-json-with-python-loop)
