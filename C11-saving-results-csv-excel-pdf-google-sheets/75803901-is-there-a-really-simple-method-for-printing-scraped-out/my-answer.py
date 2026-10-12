# Code from my Stack Overflow answer https://stackoverflow.com/a/75805366 (posted 2023-03-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
csv_filename = 'x.csv' #<--name or path to file

th_fields = ['Plaintiff', 'Defendant', 'Case Number', 'Filed', 'Court', 
             'Nature of Suit', 'Cause of Action', 'Jury Demanded By']
case_rows = []
for c in cases:
    title = c.find("div", class_ = "title-wrapper")
    row = {'title': title.text.strip()} if title else {}
    for td in c.find_all('td',{'data-th':(lambda th: th in th_fields)}): 
        row[td['data-th']] = td.text.strip()
    case_rows.append(row)

pd.DataFrame(case_rows).to_csv(csv_filename, index=False)
# pd.DataFrame(case_rows).T.to_csv(csv_filename, index=False, header=False)

# --- block 2 ---
# import pandas as pd
url=f'https://dockets.justia.com/docket/puerto-rico/prdce/3:2023cv01127/175963'
csv_filename = 'x.csv'
for ti, df in enumerate(pd.read_html(url)):
    df.to_csv(csv_filename, mode='a' if ti else 'w', index=False)
    pd.DataFrame({'':[]}).to_csv(csv_filename, mode='a')
