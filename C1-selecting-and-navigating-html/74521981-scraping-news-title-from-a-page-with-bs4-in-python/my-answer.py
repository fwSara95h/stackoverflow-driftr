# Code from my Stack Overflow answer https://stackoverflow.com/a/74522447 (posted 2022-11-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
names = [h.a for h in soup.find_all('h2', class_='entry-title')]

# --- block 2 ---
names = soup.select('h2.entry-title > a[href]')

# --- block 3 ---
for a in names: print(a.get_text().strip(), a.get('href'))

# --- block 4 ---
asText = '\n'.join([f'{a.get_text().strip()} {a.get("href")}' for a in names])

# --- block 5 ---
with open('./resources/titles.txt', 'w', encoding='utf-8') as f: 
    f.write(asText)

# --- block 6 ---
asDF = pandas.DataFrame([{
    'title': a.get_text().strip(), 'link': a.get('href')
} for a in names])
asText = asDF.to_markdown(index=False)

# --- block 7 ---
asDF.to_csv('./resources/titles.csv', index=False)
