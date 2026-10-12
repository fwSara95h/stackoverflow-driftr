# Code from my Stack Overflow answer https://stackoverflow.com/a/75909936 (posted 2023-04-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75909759')[0] # from your q

parse_cols = [c for c in df.columns if c[:4]=='Tags' or c=='VideoId'] # [filter]
max_cols = 2 # None # [ set None to include all columns ]

new_df = pd.DataFrame([{'VideoId':vi, **{k:v for k,v in [
    rv.split(':',1) for rv in row[:max_cols] if isinstance(rv,str) and ':' in rv
]}} for _, vi, *row in df[parse_cols].itertuples()])
# ]}} for vi, *row in df.itertuples()]) ## if df['VideoId'] is also df.index

# --- block 2 ---
> ╒═══════════╤═════════╤═════════╕
> │   VideoId │ Movie   │ Genre   │
> ╞═══════════╪═════════╪═════════╡
> │      1234 │ None    │ None    │
> ├───────────┼─────────┼─────────┤
> │      3456 │ Rocky   │ Drama   │
> ├───────────┼─────────┼─────────┤
> │      5678 │ Love Me │ Romance │
> ├───────────┼─────────┼─────────┤
> │      7890 │ Scream  │ Horror  │
> ├───────────┼─────────┼─────────┤
> │      9012 │ Shrek   │ None    │
> ╘═══════════╧═════════╧═════════╛
>
