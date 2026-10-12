# Code from my Stack Overflow answer https://stackoverflow.com/a/75850955 (posted 2023-03-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def traverse_choices(q_ch:dict): 
    while isinstance(q_ch, dict):
        print(q_ch['0'])
        if (user_resp:=input("Select an option: ")) not in ['R', *q_ch]:
            print('Invalid selection. Please enter a valid option [or "R" to exit].')
            continue
        if user_resp=='R': return 'R'
        if user_resp!='0': q_ch = q_ch[user_resp]
    print(q_ch)

# --- block 2 ---
        qloop = traverse_choices(data[i]["system"]) ## will return "R" or None
    if qloop != "R": break
    continue ## ONLY IF THERE IS ANYTHING AFTER IT [IN THE OUTER LOOP] TO SKIP
#### REST OF OUTER LOOP ####

# --- block 3 ---
>         if qloop == "R":
>             continue
>         else:
>             break
>
