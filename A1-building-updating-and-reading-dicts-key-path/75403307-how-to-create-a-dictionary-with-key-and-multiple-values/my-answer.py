# Code from my Stack Overflow answer https://stackoverflow.com/a/75404002 (posted 2023-02-09), extracted verbatim; may need the question's context to run.

# --- block 1 ---
qDicts = [ 
    {'question_id': 1, 'question_text': 'How many servers run at max capacity?', 'category_id':  1, 'is_long_survey': 0}, 
    {'question_id': 2, 'question_text': 'Is the database getting replicated?', 'category_id': 1, 'is_long_survey': 0}, 
    {'question_id': 3, 'question_text': 'Where is the infrastructure located?', 'category_id': 1, 'is_long_survey': 0}  
] ## [ FROM YOUR EXAMPLE ] 
chDicts = [
    {'choice_id' : 1, 'choice_text': '2', 'question_id': 1},
    {'choice_id' : 2, 'choice_text': '4', 'question_id': 1}, 
    {'choice_id' : 3, 'choice_text': '6', 'question_id': 1},
    {'choice_id' : 4, 'choice_text': 'Yes', 'question_id': 2},
    {'choice_id' : 5, 'choice_text': 'No', 'question_id': 2},
    {'choice_id' : 6, 'choice_text': 'global', 'question_id': 3},
    {'choice_id' : 7, 'choice_text': 'local', 'question_id': 3}
] ## [ FROM YOUR EXAMPLE ] 


qustionChoices = {q['question_text']: [
    c['choice_text'] for c in chDicts
    if c['question_id']==q['question_id']
] for q in qDicts} ## [ OUTPUT ]

# --- block 2 ---
> {'How many servers run at max capacity?': ['2', '4', '6'],
>  'Is the database getting replicated?': ['Yes', 'No'],
>  'Where is the infrastructure located?': ['global', 'local']}
>

# --- block 3 ---
> [{'question_id': 1,
>   'question_text': 'How many servers run at max capacity?',
>   'category_id': 1,
>   'is_long_survey': 0,
>   'choices': [
>    {'choice_id': 1, 'choice_text': '2', 'question_id': 1},
>    {'choice_id': 2, 'choice_text': '4', 'question_id': 1},
>    {'choice_id': 3, 'choice_text': '6', 'question_id': 1}] },
>  {'question_id': 2,
>   'question_text': 'Is the database getting replicated?',
>   'category_id': 1,
>   'is_long_survey': 0,
>   'choices': [
>    {'choice_id': 4, 'choice_text': 'Yes', 'question_id': 2},
>    {'choice_id': 5, 'choice_text': 'No', 'question_id': 2}] },
>  {'question_id': 3,
>   'question_text': 'Where is the infrastructure located?',
>   'category_id': 1,
>   'is_long_survey': 0,
>   'choices': [
>    {'choice_id': 6, 'choice_text': 'global', 'question_id': 3},
>    {'choice_id': 7, 'choice_text': 'local', 'question_id': 3}] }  ]
>

# --- block 4 ---
for qi, qd in enumerate(qDicts):
    qDicts[qi]['choices'] = [
        c for c in chDicts if c['question_id']==qd['question_id']]

# --- block 5 ---
q_wCh = [{**q, 'choices':[
    c for c in chDicts if c['question_id']==q['question_id']
]} for q in qDicts]
