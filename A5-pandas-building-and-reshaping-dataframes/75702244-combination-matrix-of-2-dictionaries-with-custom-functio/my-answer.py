# Code from my Stack Overflow answer https://stackoverflow.com/a/75702340 (posted 2023-03-11), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd

x = {'a': 1, 'b': 2}
y = {'a': 3, 'c': 4}
custom_function = lambda v1,v2: f'{v1}*{v2} = {v1*v2}'

df = pd.DataFrame({col:{
    ind: custom_function(cv, rv) for ind, rv in y.items()
} for col, cv in x.items()})

# --- block 2 ---
> ╒════╤═════════╤═════════╕
> │    │ a       │ b       │
> ╞════╪═════════╪═════════╡
> │ a  │ 1*3 = 3 │ 2*3 = 6 │
> ├────┼─────────┼─────────┤
> │ c  │ 1*4 = 4 │ 2*4 = 8 │
> ╘════╧═════════╧═════════╛
>

# --- block 3 ---
{col:{ind: custom_function(cv, rv) for ind, rv in y.items()} for col, cv in x.items()}

# --- block 4 ---
> {'a': {'a': '1*3 = 3', 'c': '1*4 = 4'}, 'b': {'a': '2*3 = 6', 'c': '2*4 = 8'}}
>
