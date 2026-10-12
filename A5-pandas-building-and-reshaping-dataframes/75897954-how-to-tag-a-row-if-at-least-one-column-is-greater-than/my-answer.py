# Code from my Stack Overflow answer https://stackoverflow.com/a/75898435 (posted 2023-03-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75897954')[0] # scraped from your q

valCols = [c for c in df.columns if c.startswith('Value')]
df['Flag'] = df[valCols].apply(lambda r: int(any(v>10 for v in r)), axis='columns')

# --- block 2 ---
# flag_df_new = lambda df_row: 1 if any(v>10 for v in df_row[1:]) else 0 ## same as
def flag_df_new(df_row):
    return 1 if any(v>10 for v in df_row[1:]) else 0
