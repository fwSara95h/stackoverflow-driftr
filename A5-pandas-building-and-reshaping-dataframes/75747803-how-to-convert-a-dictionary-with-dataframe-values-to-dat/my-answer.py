# Code from my Stack Overflow answer https://stackoverflow.com/a/75750483 (posted 2023-03-15), extracted verbatim; may need the question's context to run.

# --- block 1 ---
df_join = pd.concat([df1,df2], keys=['R1','R2'])

# for a list of DataFrames of unknown length: 
# df_join = pd.concat(dfs_list, keys=[f'R{i}' for i in range(1, len(dfs_list)+1)])

# --- block 2 ---
dfs_list = [df1, df2]
index_join, data_join = [], []
for di, df in enumerate(dfs_list):
    data_join += df.to_dict('records')

    index_join += [(f'R{di}', *i) for i in df.index] # if df is multi-indexed
    # index_join += list(df.index) # if df is not multi-indexed

df_join = pd.DataFrame(data=data_join, index=pd.MultiIndex.from_tuples(index_join))

# --- block 3 ---
df_join = pd.DataFrame.from_dict({
    (f'R{di}', *df_index): df_row for di,df in enumerate([df1,df2]) 
    for df_index, df_row in df.to_dict('index').items()
}, orient="index")

# --- block 4 ---
dict_val = {}
dict_val.update({('R1',i1,i2):row for (i1,i2), row in df1.to_dict('index').items()})
dict_val.update({('R2',i1,i2):row for (i1,i2), row in df2.to_dict('index').items()})
df_join = pd.DataFrame.from_dict(dict_val, orient="index")
