# Code from my Stack Overflow answer https://stackoverflow.com/a/75769838 (posted 2023-03-17), extracted verbatim; may need the question's context to run.

# --- block 1 ---
df = df.set_index('Country')

df['Region'] = df['Region'].fillna(revdct)
# df['Region'].fillna(revdct, inplace=True) ## [not sure it won't set off warnings]

df = df.reset_index()
df # print(df.to_markdown(tablefmt='fancy_grid'))

# --- block 2 ---
df['Region'] = df['Region'].fillna(df['Country'].map(revdct))
# df['Region'].fillna(df['Country'].map(revdct), inplace=True)

df
