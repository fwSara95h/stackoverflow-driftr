# Code from my Stack Overflow answer https://stackoverflow.com/a/75910689 (posted 2023-04-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# topics = ['general_topic', 'born', 'to', 'fly']
set_val = 100

cur_dict = gen_dict ## gen_dict MUST BE a dictionary
for k in topics[:-1]:
    if isinstance(cur_dict.get(k), dict): cur_dict = cur_dict[k]
cur_dict[topics[-1]] = set_val 
# if topics[-1] in cur_dict: cur_dict[topics[-1]] = set_val ## only set if path exists
# if cur_dict[topics[-1]]!=set_val: cur_dict[topics[-1]] = set_val # redundant condition

# --- block 2 ---
> {'other': 'blah', 'general_topic': {'born': {'to': {'fly': 100}}}, 'another': 324}
>

# --- block 3 ---
set_val = 100

cur_dict = gen_dict ## gen_dict MUST BE a dictionary
for i, k in enumerate(topics[:-1]):
    if not i and not isinstance(cur_dict.get(k), dict): continue
    kval = cur_dict.setdefault(k, {})

    if not isinstance(kval, dict): cur_dict[f'prev_{k}'], cur_dict[k] = kval, {}
    cur_dict = cur_dict[k]
cur_dict[topics[-1]] = set_val

# --- block 4 ---
> {'other': 'blah', 'general_topic': {'born': {'to': {'fly': 100}}}, 'another': 324}
>
