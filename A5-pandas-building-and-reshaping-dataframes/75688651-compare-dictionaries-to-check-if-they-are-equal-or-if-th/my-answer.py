# Code from my Stack Overflow answer https://stackoverflow.com/a/75702212 (posted 2023-03-11), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd 

## [ can just read tables from your question with: ]
## df1, df2 = pd.read_html('https://stackoverflow.com/questions/75688651')[:2]

df1 = pd.DataFrame([{'NAME': 'Kelly', 'AGE': 15, 'CITY': 'London', 'GENDER': 'F', 'ID': 15}, {'NAME': 'Jack', 'AGE': 12, 'CITY': '', 'GENDER': 'M', 'ID': 98}, {'NAME': 'Josh', 'AGE': 30, 'CITY': 'Austin', 'GENDER': 'M', 'ID': 12}])
df2 = pd.DataFrame([{'NAME': 'Kelly', 'AGE': 15.0, 'CITY': '', 'GENDER': 'F', 'ID': 15}, {'NAME': 'Jack', 'AGE': '', 'CITY': 'Munich', 'GENDER': 'M', 'ID': 98}, {'NAME': 'Josh', 'AGE': 30.0, 'CITY': 'Austin', 'GENDER': 'M', 'ID': 12}])

# --- block 2 ---
ids = []
for (i1,df1_row),(i2,df2_row) in zip(df1.fillna('').iterrows(),df2.fillna('').iterrows()): 
    for df1_val, df2_val in zip(df1_row, df2_row): 
        if not (df1_val==df2_val or df2_val==''): break
    else: ids.append(df2_row['ID'])

# --- block 3 ---
checkPair = lambda df1_val, df2_val: df1_val==df2_val or df2_val=='' 
ids = [df2_row['ID'] for (i_1, df1_row), (i_2, df2_row) in zip(
    df1.fillna('').iterrows(), df2.fillna('').iterrows()
) if all(checkPair(v1, v2) for v1, v2 in zip(df1_row, df2_row))]

# --- block 4 ---
comp_df = df1.set_index('ID').compare(df2.set_index('ID'), keep_shape=True)

# --- block 5 ---
ids = [i for i, r in comp_df.fillna('').iterrows() if not any(list(r!='')[1::2])]

# --- block 6 ---
comp_df = df1.set_index('ID').compare(df2.set_index('ID'), keep_shape=True)
colNames = {c[0] for c in comp_df.columns} # --> {'GENDER', 'AGE', 'CITY', 'NAME'}

ids = []
for i, row in comp_df.fillna('').iterrows():
    for c in colNames:
        if row[c]['other'] != '': break
    else: ids.append(i)
