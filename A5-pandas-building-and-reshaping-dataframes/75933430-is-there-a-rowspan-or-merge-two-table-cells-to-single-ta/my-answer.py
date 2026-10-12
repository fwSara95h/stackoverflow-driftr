# Code from my Stack Overflow answer https://stackoverflow.com/a/75935246 (posted 2023-04-05), extracted verbatim; may need the question's context to run.
data={'index': [('LCS', 'sequence1'), ('LCS', 'sequence2')], 'columns': ['alignment', 'score', 'pathcoordinates'], 'data': [['AAAGT', 5, '[4,5] -> [5,5]'], ['GGTAC', 5, '[4,5] -> [5,5]']], 'index_names': ['', 'sequence'], 'column_names': ['']}

df1 = pd.DataFrame.from_dict(data, orient='tight')
df2 = df1.reset_index().set_index(['', 'score', 'pathcoordinates', 'sequence'])
