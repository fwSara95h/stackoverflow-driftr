# Code from my Stack Overflow answer https://stackoverflow.com/a/74269843 (posted 2022-10-31), extracted verbatim; may need the question's context to run.
indiatable_headers = [col for cols in [
    [chead, chead+' [link]'] for chead in [
        c.get_text(strip=True) for c in 
        indiatable.select_one('tr:has(th)').select('th')
]] for col in cols]
# indiatable_headers = ['الترتيب', 'الترتيب [link]', 'الاسم', 'الاسم [link]', 'المؤلف', 'المؤلف [link]', 'البلد', 'البلد [link]', 'الرواية', 'الرواية [link]']

indiatable_data = [[col for cols in [[
        c.get_text(strip=True) if c.text.strip() else (
            c.img.get('alt', '') if c.find('img') else ''
        ), 'https://www.marefa.org'+c.a.get('href') if c.find('a') else None
    ] for c in r.select('td')
] for col in cols] for r in indiatable.select('tr') if not r.find('th')]
# no text --> looks for image with alt attribute

indiadf = pandas.DataFrame(
    indiatable_data, columns=indiatable_headers
).dropna(axis='columns', how='all').set_index(indiatable_headers[0])
# drops empty columns [ie, '[link]' cols with no links], and set first column as index
