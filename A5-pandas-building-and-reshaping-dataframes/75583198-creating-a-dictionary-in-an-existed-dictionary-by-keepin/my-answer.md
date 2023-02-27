---
title: "Creating a dictionary in an existed dictionary by keeping keys python"
site: stackoverflow
question_id: 75583198
answer_id: 75586443
url: https://stackoverflow.com/a/75586443
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-27T23:13:16Z
last_edited: 2023-02-27T23:32:25Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75586443/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cf3a3c43fa6eb262d4456ae10bbf6441ac573eff9bc89967099f56c27c41a7df
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75586443>, 2023-02-27, last edited 2023-02-27; score 0. Text as retrieved 2026-10-12.

If you had 

```py
# [ just copied from your example ]
Dialogues = {'dialogue_id': '000001', 'dialogue_turns': [
  {'turn_number': 0, 'interlocutor_id': '0001', 'turn_text': 'Hi, how are you?'},
  {'turn_number': 1, 'interlocutor_id': '0002', 'turn_text': "Hi, I'm fine thanks. And you?"},
  {'turn_number': 2, 'interlocutor_id': '0001', 'turn_text': 'I am good too, are you coming to the class today'},
  {'turn_number': 3, 'interlocutor_id': '0002', 'turn_text': 'Yes, see you soon.bye'},
  {'turn_number': 4, 'interlocutor_id': '0001', 'turn_text': 'bye'}]}
```

and tried

```py
dKey, iKey = 'dialogue_turns', 'interlocutor_id' ## [ just to shorten lines ]
dt_grouped = [
    (iid, [d for d in Dialogues[dKey] if d[iKey]==iid]) 
    for iid in set(dt[iKey] for dt in Dialogues[dKey])
] ## group turns by interlocutor_id
dialogue_analysis = [{
    'interlocutor_id': iid, 'total_turns': len(dt_list),
    'total_words': sum(len(dt['turn_text'].split()) for dt in dt_list)
} for iid, dt_list in dt_grouped]

Dialogues_analyzed = {  'dialogue_id': Dialogues['dialogue_id'],
                        'dialogue_analysis': dialogue_analysis  }
```

then `Dialogues_analyzed` would look like

>```py
> {'dialogue_id': '000001',
>  'dialogue_analysis': [
>   {'interlocutor_id': '0002', 'total_turns': 2, 'total_words': 10},
>   {'interlocutor_id': '0001', 'total_turns': 3, 'total_words': 16}]}
>```

---

If you want to add `dialogue_analysis` into `Dialogues`, you can do so with **<kbd>`Dialogues['dialogue_analysis'] = dialogue_analysis`</kbd>**; or, if you wanted to leave the original `Dialogues` unchanged, you could instead unpack it (with `**`) into a new dictionary which would also contain `dialogue_analysis`:

```py
Dialogues_with_Analysis = {**Dialogues, 'dialogue_analysis': dialogue_analysis}
```

and `Dialogues_with_Analysis` (or `Dialogues` if analysis was added to it) would look like:

>```py
> {'dialogue_id': '000001', 
>  'dialogue_turns': [
>   {'turn_number': 0, 'interlocutor_id': '0001', 'turn_text': 'Hi, how are you?'},
>   {'turn_number': 1, 'interlocutor_id': '0002', 'turn_text': "Hi, I'm fine thanks. And you?"},
>   {'turn_number': 2, 'interlocutor_id': '0001', 'turn_text': 'I am good too, are you coming to the class today'},
>   {'turn_number': 3, 'interlocutor_id': '0002', 'turn_text': 'Yes, see you soon.bye'},
>   {'turn_number': 4, 'interlocutor_id': '0001', 'turn_text': 'bye'}],
>  'dialogue_analysis': [
>   {'interlocutor_id': '0002', 'total_turns': 2, 'total_words': 10},
>   {'interlocutor_id': '0001', 'total_turns': 3, 'total_words': 16}]}
>```


---
---

You can also wrap the logic in a function:

```py
def analyse_dialogue(dialogue_turns:list):
    dt_grouped = [
        (iid, [d for d in dialogue_turns if d['interlocutor_id']==iid]) 
        for iid in set(dt['interlocutor_id'] for dt in dialogue_turns)
    ]
    return [{
        'interlocutor_id': iid, 'total_turns': len(dt_list),
        'total_words': sum(len(dt['turn_text'].split()) for dt in dt_list)
    } for iid, dt_list in dt_grouped]

# dialogue_analysis = analyse_dialogue(Dialogues['dialogue_turns'])
```

so that if you had a list of dialogues like *`Dialogues_list = [{'dialogue_id': '000001', ...}, {'dialogue_id': '000002', ...}, ...]`* then you could either build a list of analyses with

```py
dKey = 'dialogue_turns'
dialogues_analyses = [analyse_dialogue(d[dKey]) for d in Dialogues_list]
``` 

or build a new list of dialogues with analysis included with

```py
dialogues_with_analyses = [{
    **d, 'dialogue_analysis': analyse_dialogue(d['dialogue_turns'])
} for d in Dialogues_list]
``` 

or add analysis into each dialogue dictionary in `Dialogues_list` with

```py
dKey, aKey = 'dialogue_turns', 'dialogue_analysis'
for di, d in enumerate(Dialogues_list): 
    Dialogues_list[di][aKey] = analyse_dialogue(d[dKey])
```
