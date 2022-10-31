---
title: "Scraping a table Including hyperlinks and upload it to google sheet using python"
site: stackoverflow
question_id: 74263905
answer_id: 74269843
url: https://stackoverflow.com/a/74269843
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-31T22:49:39Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74269843/revisions
accepted: false
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: google-sheets-docs
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 60a4914950534810ee2d49d0a52a0b14e4ff3af75d67b39dbeb8d343f4b59d88
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74269843>, 2022-10-31; score 1. Text as retrieved 2026-10-12.

I'm not sure how to write hyperlinks in a way that Sheets will recognize them as hyperlinks, but the following will create extra columns to hold the links:
```python
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
```
After that, you can create a spreadsheet with `indiadf.to_excel` (DON'T use `index=False` this time unless you want to lose the `الترتيب` column, since that has now been set as the index), and then manually upload it...

<hr>

If you want to automate the google sheets part as well, you can look into [the Sheets API](https://developers.google.com/sheets/api/quickstart/python) and maybe modules like [pydrive](https://medium.com/@annissouames99/how-to-upload-files-automatically-to-drive-with-python-ee19bb13dda) or [pygsheets](https://github.com/nithinmurali/pygsheets).
