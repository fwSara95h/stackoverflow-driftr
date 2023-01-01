---
title: "Extract table from PDF - text in different rows"
site: stackoverflow
question_id: 74947257
answer_id: 74973195
url: https://stackoverflow.com/a/74973195
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-01T05:09:41Z
last_edited: 2023-01-01T05:15:27Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74973195/revisions
accepted: true
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [PDF table extractor set]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 811d006b25790941629da6fa7952a8f1586327e245c2fcf464416acff99444fa
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74973195>, 2023-01-01, last edited 2023-01-01; **accepted**; score 1. Text as retrieved 2026-10-12.

It's somewhat understandable that the other solution used the PDFs as images since, as explained in the [pypdf docs](https://pypdf2.readthedocs.io/en/stable/user/extract-text.html#why-text-extraction-is-hard),
> Typically, tables are just absolutely positioned text. In the worst case, ever single letter could be absolutely positioned. That makes it hard to tell where columns / rows are.

If you can find any other source for the data [are the files available in any other format?], I would strongly suggest trying to extract tables from those instead.

<sub>Sometimes there's a pattern is how the table has been scrambled and then you can  try to shift the contents around [[see this example](https://pastebin.com/cK3HXVdY)]; I don't see any patterns, but if you're more familiar with the data, you might...</sub>

But if this is your only option, then I have [**this set of functions**](https://pastebin.com/trKxysh6) which try to extract a [list of dictionaries](https://i.sstatic.net/llbUz.png) [with each dictionary potentially representing a row] from a PDF file using the [minecart](https://github.com/felipeochoa/minecart#installation) library. It's still glitchy and rather limited [it can't blindly find tables from any document like `tabula` tries to - instead, it requires information about the table columns, and preferably the first row/line as well], but you might find it useful for your issue here.

Of them, `pdfPg_table` is the shortest method - along with passing the document, you have to specify the page index and [optionally] the starting positions of the columns and first row. [The first page is the default page to parse; and if first row position isn't specified, it just splits up the whole page; and if the columns' left-border positions aren't specified, you have to instead tell it how many columns there should be, and it just guessed the left borders based on the frequency of character positions.]

You *could* just call it like *`pdfPg_table('045632_2023.pdf', 3)`* for 3 columns [from the first page - by default] [[view output](https://i.sstatic.net/9Umez.png)] and then trim off the unnecessary rows and columns, but **`getRows_fromPdfDoc`** (which depends on *all* the other functions) accepts hints to figure out where the table starts and the column divisions:
  - `startSeq`: the text expected to be at the beginning of the table [*`"Important Questions Answers Why This Matters:"`* in the example below], and
  - `colHint`: can just be the number of columns like in the example above, but it's more reliable to send the horizontal positions of the left-borders, or [more feasibly] substrings from the **beginnings** of **left-aligned** contents from **each** column. [This *can* be the column headers (as below), but not always.]


```python
# import pandas
# PASTE EVERYTHING FROM https://pastebin.com/trKxysh6

colHead = ['Important Questions', 'Answers', 'Why This Matters:']
pandas.DataFrame(getRows_fromPdfDoc(
    pDoc='045632_2023.pdf',  startSeq=' '.join(colHead), colHint=colHead, skipRows=1
)).drop(['col_0'], axis='columns').dropna(thresh=2, axis='rows').set_axis(colHead, axis='columns')
```
[![op1][1]][1]

[Once you have the DataFrame, you can of course use [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) to save as CSV.]

---

`getRows_fromPdfDoc` is also capable of extracting [a table across multiple pages](https://i.sstatic.net/ChMZw.png) [as long as it has the same header in every page]:

```python
csSamps = [ 'Common Medical Event', 'Services You May Need', '$30 copayment', 
            'Non-Preferred: 40% coinsurance', 'Limitations, Exceptions, & Other']
headTxt = ' '.join(csSamps[:2] + ['What You Will Pay'] + csSamps[-1:])
rList = getRows_fromPdfDoc('045632_2023.pdf', headTxt, csSamps, 2)
```

But at this point, you might notice that merged cells are left [empty except the first row](https://i.sstatic.net/vd5pP.png). If it's just [merged across rows](https://i.sstatic.net/6VEhk.png), it's not difficult to [fill them up from the previous rows](https://i.sstatic.net/X7ARK.png):

```python
prev_c1 = ''
for ri, r in enumerate(rList):
    if r['col_1']: prev_c1 = r['col_1']
    else: rList[ri]['col_1'] = prev_c1
```

However, if they're [merged across columns or split in any way](https://i.sstatic.net/kKD1M.png), then the [merged columns are split back up](https://i.sstatic.net/5ZinT.png), and partially filled rows are added for the split row. [I expect splits across columns will remain entirely undetected and the contents will be merged back into a single cell.]

Also, note that there's no way to extract [nested tables][2] with the current functions, although it's definitely not impossible. I might be able to com up with more reliable methods if I can figure out how to detect the background color of the characters and when they cross a cell border....

  [1]: https://i.sstatic.net/KkGHt.png
  [2]: https://i.sstatic.net/2BPK5.png
