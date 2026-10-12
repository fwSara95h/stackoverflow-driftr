# Code from my Stack Overflow answer https://stackoverflow.com/a/75105219 (posted 2023-01-13), extracted verbatim; may need the question's context to run.
filepath = r"C:\__Imagens e Planilhas Python\Facebook\Youtube.xlsx"
df = df.read_excel(filepath) #, header=None) # if there is no header row
df['Video'] = links
df.to_excel(filepath, engine='xlsxwriter') #, index=False)
