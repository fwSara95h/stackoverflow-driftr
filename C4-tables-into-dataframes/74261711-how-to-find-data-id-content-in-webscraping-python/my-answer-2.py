# Code from my Stack Overflow answer https://stackoverflow.com/a/74279923 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# (pretty much the same as before)
dataType_tables = [{
    'type': t.get('data-subtype', 'NO_SUBTYPE') + ' - ' + t.get('data-type'), 
    'headers': ['Data-ID'] + [
        col.get_text(strip=True) for col in t.select('th')], 
    'data': [[r.get('data-id')] + [
        col.get_text(strip=True) for col in r.select('td')
    ] for r in t.select('tr:has(td)')]
} for t in doc.select('div[data-type]')]

# --- block 2 ---
with pd.ExcelWriter("albelli_prijsoverzicht.xlsx") as w:
    for table_i in dataType_tables:
        pd.DataFrame(
            table_i['data'], columns=table_i['headers']
        ).set_index('Data-ID').to_excel(w, sheet_name=table_i['type'])
