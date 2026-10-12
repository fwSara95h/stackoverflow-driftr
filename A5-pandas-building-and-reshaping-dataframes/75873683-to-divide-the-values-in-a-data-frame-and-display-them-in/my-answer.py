# Code from my Stack Overflow answer https://stackoverflow.com/a/75874944 (posted 2023-03-29), extracted verbatim; may need the question's context to run.
target_col = 'feature'
other_cols = [c for c in df.columns if c!=target_col]

## before clearing out duplicates
df_exp = df.assign(**{target_col:df['feature'].str.split('/')}).explode(target_col)

## convert whole df into a multiIndex
df_exp_mi = df_exp.set_index(other_cols+[target_col]) 

## just empty out duplicate cells
df_exp_nodup = df_exp.copy() ## not necessary, only copying for demo stages
# df_exp_nodup.loc[df_exp.index.duplicated(), ['model','kind']] = '' # simpler
dups = df_exp.duplicated(subset=['model', 'kind'])
for c in other_cols: df_exp_nodup[c] = df_exp_nodup[c].mask(dups, '')
