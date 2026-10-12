# Code from my Stack Overflow answer https://stackoverflow.com/a/74201794 (posted 2022-10-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
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

# --- block 4 ---
# import pandas
pandas.DataFrame(gv1_rows[1:], columns=gv1_rows[0])

# --- block 5 ---
for r in gv1_rows: print(r)

# --- block 6 ---
### [only the first 5 rows are pasted below] ###
[('رقم المادة', 'اسم المادة', 'التسجيلي', 'س.م', 'الوقت', 'الايام', 'القاعة', 'اسم المدرس', 'ملاحظات', 'سعة القاعة', 'اشتغال القاعة', '', 'طربقة تدرسي المادة'), ('0101111', 'الرسم الميكانيكي', '602', '2', '08:00 ص - 11:00 ص', 'ن ر', 'مختبر الحاسوب 10 (كلية الهندسة)', 'د. عمران مسلم ضيف الله العتايقه', '1516', '24', '23', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '620', '1', '02:00 م - 05:00 م', 'ن', 'مشغل اللحام', 'د. مياس محمد صالح المحاسنة', 'اكتمل العدد', '55', '60', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '626', '1', '11:00 ص - 02:00 م', 'ن', 'مشغل النجارة', 'د. تامر سليمان حماد الشقارين', '', '50', '45', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '1071', '1', '08:00 ص - 11:00 ص', 'ح', 'مشغل النجارة', 'عدي عبد القادر سالم العكايلة', '', '50', '42', '0', 'وجاهي'), ('0101120', 'المشاغل الهندسية 1', '1321', '1', '08:00 ص - 11:00 ص', 'ث', 'مشغل النجارة', 'عدي عبد القادر سالم العكايلة', '', '50', '48', '0', 'وجاهي')]
