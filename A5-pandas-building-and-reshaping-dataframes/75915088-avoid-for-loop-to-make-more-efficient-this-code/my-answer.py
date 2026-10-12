# Code from my Stack Overflow answer https://stackoverflow.com/a/75920208 (posted 2023-04-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def my_formula(di_dm_dmm_vals):
    di_val, dm_val, dmm_val = di_dm_dmm_vals
    if di_val >= dm_val + 5*dmm_val: return dm_val + 5*dmm_val
    if di_val <= dm_val - 5*dmm_val: return dm_val - 5*dmm_val
    return di_val ## [ no need for elif/else after return ]

# --- block 2 ---
listify = lambda x: [x]
df_new = di.applymap(listify) + dm.applymap(listify) + dmm.applymap(listify) 
df_new = df_new.applymap(my_formula)
