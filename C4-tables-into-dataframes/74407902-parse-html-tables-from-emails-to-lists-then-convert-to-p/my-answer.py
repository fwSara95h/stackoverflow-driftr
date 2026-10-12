# Code from my Stack Overflow answer https://stackoverflow.com/a/74421202 (posted 2022-11-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[         0        1
 0  Column1  Value1a
 1  Column2  Value2a
 2  Column3  Value3a
 3  Column4  Value4a
 4  Column5  Value5a
 5  Column6  Value6a
 6  Column7  Value7a
 7  Column8  Value8a,
          0        1
 0  Column1  Value1b
 1  Column2  Value2b
 2  Column3  Value3b
 3  Column4  Value4b
 4  Column5  Value5b
 5  Column6  Value6b
 6  Column7  Value7b
 7  Column8  Value8b,
          0        1
 0  Column1  Value1c
 1  Column2  Value2c
 2  Column3  Value3c
 3  Column4  Value4c
 4  Column5  Value5c
 5  Column6  Value6c
 6  Column7  Value7c
 7  Column8  Value8c]

# --- block 2 ---
[         0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1a  Value2a  Value3a  Value4a  Value5a  Value6a  Value7a  Value8a,
          0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1b  Value2b  Value3b  Value4b  Value5b  Value6b  Value7b  Value8b,
          0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1c  Value2c  Value3c  Value4c  Value5c  Value6c  Value7c  Value8c]

# --- block 3 ---
pd.concat([d.rename(columns=d.iloc[0]).drop(d.index[0]) for d in df], ignore_index=True)

# --- block 4 ---
pd.concat([mdf.set_index(mdf.columns[0]) for mdf in [
    (pd.read_html(str(mtable))[0] if mtable else None) for mtable in 
    [BeautifulSoup(m.HTMLBody, "lxml").find('table') for m in Mail_Messages] 
] if mdf is not None], axis='columns', ignore_index=True).T

# --- block 5 ---
output = []
for mail in Mail_Messages:
    html_tables = BeautifulSoup(mail.HTMLBody, "lxml").find('table')

    # read html table to dataframe list
    df = pd.read_html(str(html_tables))[0]
    output.append(df.set_index(df.columns[0]))

    ## WHATEVER ELSE YOU NEED TO DO IN THE LOOP ##

output = pd.concat(output, axis='columns', ignore_index=True).T
print(output)
