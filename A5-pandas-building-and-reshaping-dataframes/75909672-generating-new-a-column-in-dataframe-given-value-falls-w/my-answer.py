# Code from my Stack Overflow answer https://stackoverflow.com/a/75909789 (posted 2023-04-02), extracted verbatim; may need the question's context to run.
range_limit = 2

lower_limits = df['B'] - range_limit
upper_limits = df['B'] + range_limit
df['Eq'] = ((lower_limits < df['A']) & (df['A'] < upper_limits)).astype(int)

# df['Eq'] = (((df['B'] - 2) < df['A']) & (df['A'] < (df['B'] + 2))).astype(int)
