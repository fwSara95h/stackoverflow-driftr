# Code from my Stack Overflow answer https://stackoverflow.com/a/75922226 (posted 2023-04-03), extracted verbatim; may need the question's context to run.
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75922021')[0]

unstacked_df = df.set_index(['User ID','Status']).unstack()

kList = {c[0] for c in unstacked_df.columns} ## {'Name','Favorite'}
dfList = [unstacked_df[k] for k in kList] ## [u__df['Name'],u__df['Favorite']]
conc_df = pd.concat(dfList, keys=kList, names=['Attribute Changed', 'User ID'])

df2Cols = ['User ID', 'Attribute Changed', 'After', 'Before']
df2 = conc_df.reset_index().rename_axis(None,axis='columns')[df2Cols]
