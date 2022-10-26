---
title: "how to interact with page before read data beautifulsoup"
site: stackoverflow
question_id: 74155799
answer_id: 74201794
url: https://stackoverflow.com/a/74201794
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T01:36:39Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74201794/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b7d142bfc63c25042b476230cb801705af49e7f9b7533aafd1ca63bba355d828
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74201794>, 2022-10-26; **accepted**; score 0. Text as retrieved 2026-10-12.

BeautifulSoup is for scraping *static* content - it does not let you interact with the site. Since this site is submitting a form to itself with a POST request to generate the schedules table, and [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/introduction.html) can be used to interact with forms, here's an example of how to get all the schedules:

```python
# import mechanicalsoup

browserS = mechanicalsoup.StatefulBrowser()
browserS.open('http://webapp.ttu.edu.jo/corse_study/Default.aspx')

selOpts = {
    'd_deg': 'جميع الدرجات', 
    'd_coll': 'جميع الكليات', 
    'd_dept': 'جميع الاقسام'
}
for s in selOpts:
    selection = {s: selOpts[s]}
    browserS.select_form('form[id="form1"]').set_select(selection)

    # submit wrapped in print just to log if each request was successful
    print(browserS.submit_selected(), 'for', selection) 

gv1_rows = [
    tuple([c.get_text(strip=True) for c in r.select('th, td')])
    for r in browserS.page.select('table#GridView1 tr')
]
```
With some other forms, you could have simply submitted all the options at once with `...set_select(selOpts)`, but this form has a hidden input that forces you to use only one dropdown at a time, so you have to loop through the dropdowns as above.

<hr>

([mechanize](https://mechanize.readthedocs.io/en/latest/) is another library you could use for this; and if you're interested in more complex web-scrapers, [Selenium](https://medium.com/featurepreneur/an-introduction-to-web-automation-using-selenium-python-2ad84814b11c) is often used for web automation, but *this* interaction is simple enough to not need it.)

<hr>

If you need/want to stick to requests+bs4, you could use the following function to prepare for the POST request:

```python
def prepPayload(curSoup, targetDropdown, optSelected): 
    pl = [('__EVENTTARGET', targetDropdown)]

    for s in curSoup.select('input[name]'):
        pl.append((s.get('name'), s.get('value')))  

    for s in curSoup.select('select[name]'):
        sName = s.get('name') 
        chOpt = s.find('option', {'selected': 'selected'})  

        if sName == targetDropdown: 
            # value match
            selOpt = s.find('option', {'value': optSelected}) 

            # text match
            if selOpt is None: 
                selOpt = s.find(
                    lambda o: o.name == 'option' and 
                    o.get_text(strip=True) == optSelected.strip()
                )

            # partial text match
            if selOpt is None: 
                selOpt = s.find(
                    lambda o: o.name == 'option' and 
                    optSelected.strip() in o.get_text()
                )
            
            # only change chOpt if there was a match
            if selOpt is not None: chOpt = selOpt
        
        if chOpt is not None and chOpt.get('value') is not None:
            pl.append((sName, chOpt.get('value')))
    
    return dict(pl)
```

and then use it to submit the necessary requests:

```python
url = 'http://webapp.ttu.edu.jo/corse_study/Default.aspx'
gReq = requests.get(url)
print('GET request ', gReq.status_code, gReq.reason) # log status
gSoup = BeautifulSoup(gReq.text, 'html.parser')

selOpts = {
    'd_deg': 'جميع الدرجات', 
    'd_coll': 'جميع الكليات', 
    'd_dept': 'جميع الاقسام'
}
postSoup = gSoup
for s in selOpts:
    pPayload = prepPayload(postSoup, s, selOpts[s])
    pReq = requests.post(url, data = pPayload)
    print(f'<POST request {pReq.status_code} {pReq.reason}>', s, selOpts[s]) # log status
    postSoup = BeautifulSoup(pReq.text, 'html.parser')

gv1_rows = [
    tuple([c.get_text(strip=True) for c in r.select('th, td')])
    for r in postSoup.select('table#GridView1 tr')
]
```

<hr>

Whichever method is used, `gv1_rows` should have the same value in the end.

You could view it as a [pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) DataFrame with
```python
# import pandas
pandas.DataFrame(gv1_rows[1:], columns=gv1_rows[0])
```

or print it row by row with 
```python
for r in gv1_rows: print(r)
```

or even simply use `print(gv1_rows)` and get the output in one line:
```python
### [only the first 5 rows are pasted below] ###
[('رقم المادة', 'اسم المادة', 'التسجيلي', 'س.م', 'الوقت', 'الايام', 'القاعة', 'اسم المدرس', 'ملاحظات', 'سعة القاعة', 'اشتغال القاعة', '', 'طربقة تدرسي المادة'), ('0101111', 'الرسم الميكانيكي', '602', '2', '08:00 ص - 11:00 ص', 'ن ر', 'مختبر الحاسوب 10 (كلية الهندسة)', 'د. عمران مسلم ضيف الله العتايقه', '1516', '24', '23', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '620', '1', '02:00 م - 05:00 م', 'ن', 'مشغل اللحام', 'د. مياس محمد صالح المحاسنة', 'اكتمل العدد', '55', '60', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '626', '1', '11:00 ص - 02:00 م', 'ن', 'مشغل النجارة', 'د. تامر سليمان حماد الشقارين', '', '50', '45', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '1071', '1', '08:00 ص - 11:00 ص', 'ح', 'مشغل النجارة', 'عدي عبد القادر سالم العكايلة', '', '50', '42', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '1321', '1', '08:00 ص - 11:00 ص', 'ث', 'مشغل النجارة', 'عدي عبد القادر سالم العكايلة', '', '50', '48', '0', 'وجاهي')]
```
