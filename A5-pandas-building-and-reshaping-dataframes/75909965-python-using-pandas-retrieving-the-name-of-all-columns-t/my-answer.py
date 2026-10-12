# Code from my Stack Overflow answer https://stackoverflow.com/a/75910041 (posted 2023-04-02), extracted verbatim; may need the question's context to run.
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75909965')[0] # scraped your q

[c for c in df.columns if df[c].dtype.kind in 'iufc']
