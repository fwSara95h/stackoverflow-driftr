# Code from my Stack Overflow answer https://stackoverflow.com/a/75916413 (posted 2023-04-03), extracted verbatim; may need the question's context to run.
df = pd.read_html(str(table))[0]
with pd.ExcelWriter("hkjc.xlsx", 
                    engine="openpyxl", 
                    mode='a', if_sheet_exists='new') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=True)
