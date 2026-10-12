# Code from my Stack Overflow answer https://stackoverflow.com/a/75586443 (posted 2023-02-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# [ just copied from your example ]
Dialogues = {'dialogue_id': '000001', 'dialogue_turns': [
  {'turn_number': 0, 'interlocutor_id': '0001', 'turn_text': 'Hi, how are you?'},
  {'turn_number': 1, 'interlocutor_id': '0002', 'turn_text': "Hi, I'm fine thanks. And you?"},
  {'turn_number': 2, 'interlocutor_id': '0001', 'turn_text': 'I am good too, are you coming to the class today'},
  {'turn_number': 3, 'interlocutor_id': '0002', 'turn_text': 'Yes, see you soon.bye'},
  {'turn_number': 4, 'interlocutor_id': '0001', 'turn_text': 'bye'}]}

# --- block 2 ---
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

# --- block 3 ---
> {'dialogue_id': '000001',
>  'dialogue_analysis': [
>   {'interlocutor_id': '0002', 'total_turns': 2, 'total_words': 10},
>   {'interlocutor_id': '0001', 'total_turns': 3, 'total_words': 16}]}
>

# --- block 4 ---
Dialogues_with_Analysis = {**Dialogues, 'dialogue_analysis': dialogue_analysis}

# --- block 5 ---
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
>

# --- block 6 ---
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

# --- block 7 ---
dKey = 'dialogue_turns'
dialogues_analyses = [analyse_dialogue(d[dKey]) for d in Dialogues_list]

# --- block 8 ---
dialogues_with_analyses = [{
    **d, 'dialogue_analysis': analyse_dialogue(d['dialogue_turns'])
} for d in Dialogues_list]

# --- block 9 ---
dKey, aKey = 'dialogue_turns', 'dialogue_analysis'
for di, d in enumerate(Dialogues_list): 
    Dialogues_list[di][aKey] = analyse_dialogue(d[dKey])
