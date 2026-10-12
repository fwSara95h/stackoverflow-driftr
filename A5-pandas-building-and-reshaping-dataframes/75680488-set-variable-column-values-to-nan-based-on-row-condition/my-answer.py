# Code from my Stack Overflow answer https://stackoverflow.com/a/75680677 (posted 2023-03-09), extracted verbatim; may need the question's context to run.
for i, cn in enumerate(df.columns,1): 
    df[cn] = [*[np.nan]*i, *df[cn].loc[i:]]
