---
title: "How to extract the details from particular HTML text"
site: stackoverflow
question_id: 75410558
answer_id: 75410739
url: https://stackoverflow.com/a/75410739
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2023-02-10T11:50:52Z
last_edited: 2023-02-11T17:09:41Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9afc739f3c865502eedc5be0f459770b2efa9af0f7c258522bae5dafcdfc8982
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2023-02-10

Posted on Stack Overflow, <https://stackoverflow.com/a/75410739>, 2023-02-10, last edited 2023-02-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

*In newer code avoid old syntax `findAll()` instead use `find_all()` or `select()` with `css selectors` - For more take a minute to [check docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#method-names)*

----

You could select all `<td>` with `<label>` in your element and use `stripped_strings` to extract the contents - In case it is the same motive as in https://stackoverflow.com/questions/75407616/how-to-scrape-data-from-the-website-which-is-not-aligned-properly you could get a nicly structured `dict` of label and text

    dict(e.stripped_strings for e in soup.select('#formContents td:has(label)'))

or this if it is close to the requirements from https://stackoverflow.com/questions/75421490/how-to-extract-the-data-from-the-html-content:

    dict((e.text,e.find_next('td').get_text(strip=True)) for e in soup.select('label'))



#### Example

    from bs4 import BeautifulSoup
    html_content = """<div id="formContents" class="dformDisplay ">        
    <div class="sectionDiv expanded">
    <div class="Title expanded ToggleSection shead"
      style="margin-top:1em"
     id="sect_s11Header">
    <div><!--The div around the table is so that the toggling can be animated smoothly-->
    <table id="sect_s1" class="formSection LabelsAbove">
    <tr class="formRow ">
    <td id="tdl_8" class="label lc" >
    <label class="fieldLabel " ><b >Address</b></label>
     <table class="EmailFieldPadder" border="0" cellspacing="0" cellpadding="0" valign="top" style="width:98%;margin-top:.3em;margin-right:1.5em;">
     <tr><td class="EmailDivWrapper" style="background-color:#f5f5f5;padding: 0.83em;border-radius:3px;margin:0;border:0px;">
        <div id="tdf_8" class="cell cc" >
        <a
    href="https://maps.google.com/?q=1183+Pelham+Wood+Dr%2C+Rock+Hill%2C+SC+29732">1183
    Pelham Wood Dr, Rock Hill, SC 29732</a>
    </span></div>               
    </td></tr></table>
    </td>
    """
    
    soup = BeautifulSoup(html_content)
    
    dict(e.stripped_strings for e in soup.select('#formContents td:has(label)'))

#### Output

    {'Address': '1183\nPelham Wood Dr, Rock Hill, SC 29732'}

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ajay Kk](https://stackoverflow.com/users/20631223)** (2023-02-10): There are multiple datas in html your code is not working for that case. How to make changes in labels = datas.findAll("label",{"class":"fieldLabel"}) to get td text
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2023-02-10): So there would be scope to improve your question and provide appropriate examples and details to take these circumstances into account. however, to get just this string use `soup.select_one('#formContents td:has(label)').get_text(':',strip=True).replace('\n', ' ')`
