# Code from my Stack Overflow answer https://stackoverflow.com/a/75949375 (posted 2023-04-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
input_fp = 'x.txt' ## set the path to the ACTUAL file
sep_str = None # ' ' # ',' # ' | ' # '\t' # 

with open(input_fp) as f:
    # text_lines = [l.rstrip() for l in f.readlines()] # keep empty lines
    text_lines = [l.rstrip() for l in f.readlines() if l.strip()] ## no empty lines

dKeys = text_lines[0].split(sep_str) if text_lines else [] 

maxSplits = len(dKeys) - 1
dict_list = [dict(zip(dKeys, tl.split(sep_str,maxSplits))) for tl in text_lines[1:]]

# --- block 2 ---
dict_list = [dict(zip(dKeys, tl.split(sep_str))) for tl in text_lines[1:]]

# --- block 3 ---
First_Name Last_Name Gender Age Phone Occupation
Penelope Miller Female 23 069-5515-87 Teacher
Julian Watson Male 19 355-0427-79 Cook
Gianna Barnes Female 27 641-6494-91 Mechanic
Walter Walker Male 28 164-8407-47 Mechanic
Chelsea Scott Female 28 272-2601-10 Florist

# --- block 4 ---
> [
>   {'First_Name': 'Penelope', 'Last_Name': 'Miller', 'Gender': 'Female', 'Age': '23', 'Phone': '069-5515-87', 'Occupation': 'Teacher'},
>   {'First_Name': 'Julian', 'Last_Name': 'Watson', 'Gender': 'Male', 'Age': '19', 'Phone': '355-0427-79', 'Occupation': 'Cook'},
>   {'First_Name': 'Gianna', 'Last_Name': 'Barnes', 'Gender': 'Female', 'Age': '27', 'Phone': '641-6494-91', 'Occupation': 'Mechanic'},
>   {'First_Name': 'Walter', 'Last_Name': 'Walker', 'Gender': 'Male', 'Age': '28', 'Phone': '164-8407-47', 'Occupation': 'Mechanic'},
>   {'First_Name': 'Chelsea', 'Last_Name': 'Scott', 'Gender': 'Female', 'Age': '28', 'Phone': '272-2601-10', 'Occupation': 'Florist'}
> ]
>
