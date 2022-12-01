---
title: "How to extract the information from XML beautiful soup?"
site: stackoverflow
question_id: 74642521
answer_id: 74645871
url: https://stackoverflow.com/a/74645871
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-01T17:26:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74645871/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 48927439353bcd41aa3a39dfd7ea198f96fd1562ef48548e348d49f753d12eb7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74645871>, 2022-12-01; **accepted**; score 1. Text as retrieved 2026-10-12.

(With *"list of XML beautifulsoup tag elements"* in variable `xTagList`,) you could try something like this
```python 
bsParser = 'html.parser' # 'xml' # 
# xTagList = [BeautifulSoup(str(x), bsParser) for x in xTagList] # should fix some formatting
wCont_xstrs = ['\n'.join([
    str(d) for d in x.descendants if hasattr(d, 'find_all') 
    and not d.find_all() and d.get_text().strip()
]) for x in xTagList]
```
to get html/xml **string.**

---

with `bsParser = 'xml'`, `wCont_xstrs` looks like
```html
[
<DateFormattedForTHForm>07/01/2022</DateFormattedForTHForm>
<DateFormattedForTHForm>07/01/2023</DateFormattedForTHForm>
<FormDescription>Notification Of Settlement</FormDescription>
<FormNumber>WC 99 06 04</FormNumber>
,
<DisplayName>Mallesham Yamulla</DisplayName>
<FEINOrSSN>123-45-6789</FEINOrSSN>
<formsMaskedSSN_and_NoMaskFEIN>**-***-8834</formsMaskedSSN_and_NoMaskFEIN>
<AddressLine1>A</AddressLine1>
<AddressLine123>B</AddressLine123>
<CityStateZip>ENID, OK 73703</CityStateZip>
<Country>IND</Country>
]
```
[btw, if your xml had namespaces (as well formed xmls usually do), they would be lost after using xml parser. Using html parser will preserve namespaces, but there will be another issue as you will see below.]

---

with `bsParser = 'html.parser'` (and probably any other parser other than `xml`),  `wCont_xstrs` looks like
```html
[
<dateformattedforthform>07/01/2022</dateformattedforthform>
<dateformattedforthform>07/01/2023</dateformattedforthform>
<formdescription>Notification Of Settlement</formdescription>
<formnumber>WC 99 06 04</formnumber>
,
<displayname>Mallesham Yamulla</displayname>
<feinorssn>123-45-6789</feinorssn>
<formsmaskedssn_and_nomaskfein>**-***-8834</formsmaskedssn_and_nomaskfein>
<addressline1>A</addressline1>
<addressline123>B</addressline123>
<citystatezip>ENID, OK 73703</citystatezip>
<country>IND</country>
]
```
(notice how capitalization has been lost from tag names)

---

If you want a list bs4 objects, you can do something like 
```python
wCont_xtags = [BeautifulSoup(x, bsParser) for x in wCont_xstrs]
```
**UNLESS** you're using `bsParser = 'xml'`, because then you need to wrap them in some tag first like 
```python
wCont_xtags = [BeautifulSoup(f'<Entry>{x}</Entry>', bsParser).Entry for x in wCont_xstrs]
```
