# Code from my Stack Overflow answer https://stackoverflow.com/a/75657608 (posted 2023-03-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import pandas as pd

tRef_fp = 'map_old_new.xlsx' ## path to file with new&old names
tRef_dict = pd.read_excel(tRef_fp).to_dict('split')
tRef_dict = {k:v for v,k,*_ in tRef_dict['data']} # colA->new, colB->old
# tRef_dict = dict(tRef_dict['data']) # only 2 cols, colA->old, colB->new

# --- block 2 ---
{'apple-er3': 'horse-er45', 'alk-er43': 'erk-bf43'}
# 'apple-er3' will get translated to  'horse-er45'

# --- block 3 ---
{'horse-er45': 'apple-er3', 'erk-bf43': 'alk-er43'}
# 'horse-er45' will get translated to  'apple-er3'

# --- block 4 ---
old_fp = 'old.xlsx' ## path to file with old names
new_fp = 'new.xlsx' ## [can be the same as old_fp]

names_df = pd.read_excel(old_fp) #, header=None) ## if there is no header row, specify
names_df = names_df.applymap(lambda x: tRef_dict.get(x,x)) ## [update names]
names_df.to_excel(new_fp, index=False) #, header=False) ## [save updated]
