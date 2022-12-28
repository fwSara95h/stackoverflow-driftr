---
title: "Scraping specific pdfs from different websites"
site: stackoverflow
question_id: 74934432
answer_id: 74940312
url: https://stackoverflow.com/a/74940312
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-28T12:34:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74940312/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8fb9910c7911fb953310a13bd093ccd72c35637d156730f4e8eb50b9ecc68682
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74940312>, 2022-12-28; **accepted**; score 1. Text as retrieved 2026-10-12.

The links in your html file all seem to be to the same pdf [or at least they have the same filename], so it'll just be downloading and over-writing the same document. Still, if you just want to target only the first of those links, you could include the class *`externalDocument`*  in your selector.

```python
 for link in soup.select('a.externalDocument[href$="EN.pdf"]'):
```

---

If you want to target a specific event like *'Legislative proposal published'*, then you could do something like this:

```python
# urls....os.mkdir(folder_location)

evtName = 'Legislative proposal published'

tdSel, spSel, aSel = 'div.ep-table-cell', 'span.ep_name', 'a[href$="EN.pdf"]'
dlSel = f'{tdSel}+{tdSel}+{tdSel} {spSel}>{aSel}' 
trSel = f'div.ep-table-row:has(>{dlSel}):has(>{tdSel}+{tdSel} {spSel})'

for url in urls:
    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")

    pgPdfLinks = [
        tr.select_one(dlSel).get('href') for tr in soup.select(trSel) if 
        evtName.strip().lower() in 
        tr.select_one(f'{tdSel}+{tdSel} {spSel}').get_text().strip().lower()
        ## if you want [case sensitive] exact match, change condition to
        # tr.select_one(f'{tdSel}+{tdSel} {spSel}').get_text() == evtName
    ]     
    for link in pgPdfLinks[:1]:
        filename = os.path.join(folder_location, link.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link)).content)
```

[The `[:1]` of *`pgPdfLinks[:1]`* is probably unnecessary since more than one match isn't expected, but it's there if you want to absolutely ensure only one download per page.]

**Note:** you need to be sure that there will be an event named `evtName` with a link matching `aSel` (*`a[href$="EN.pdf"]`* in this case) - otherwise, no PDF links will be found and nothing will be downloaded for those pages.

---

>  if it keeps the name of the link it could be also easier for me

It's already doing that in your code, since there doesn't seem to be much difference between `link['href'].split('/')[-1]` and `link.get_text().strip()`, but if you meant that you want the page link [i.e. the `url`], you could include the **`procnum`** (since that seems to be an identifying part of `url`) in your `filename`:

```python    
    # for link in...
        procnum = url.replace('?', '&').split('&procnum=')[-1].split('&')[0]
        procnum = ''.join(c if (
            c.isalpha() or c.isdigit() or c in '_-[]'
        ) else ('_' if c == '/' else '') for c in procnum)
        filename = f"proc-{procnum} {link.split('/')[-1]}"
        # filename = f"proc-{procnum} {link['href'].split('/')[-1]}" # in your current code

        filename = os.path.join(folder_location, filename)
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url, link)).content)
            # f.write(requests.get(urljoin(url['href'], link)).content) # in your current code
```

So, [for example] instead of saving to *"COM_COM(2020)0791_EN.pdf"*, it will save to "**proc-OLP_2020_0350 COM_COM(2020)0791_EN.pdf**".

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Cesare](https://stackoverflow.com/users/18899582)** (2022-12-28): Ahhh thank you so much, it works perfectly. Now I will match it with each its own proposal. I can't upvote you because I don't have enough reputation but you really helped me a lot (:
- **me** (2022-12-28): @DarioMarino glad it helped! [And welcome to StackOverflow.] If this (or any other) answer resolves your issue satisfactorily, please mark [as accepted](https://meta.stackexchange.com/questions/5234/how-does-accepting-an-answer-work) by clicking the checkmark button to the the top-left of it.
