# Code from my Stack Overflow answer https://stackoverflow.com/a/75439085 (posted 2023-02-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>         if obj in rooms[current_room]['item']:
>

# --- block 2 ---
if obj.lower() in [i.lower() for i in rooms[current_room]['item']]:
