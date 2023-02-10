---
title: "How to extract the details from particular HTML text"
site: stackoverflow
question_id: 75410558
url: https://stackoverflow.com/q/75410558
asked: 2023-02-10T11:33:27Z
asked_by: "Ajay Kk"
asked_by_url: https://stackoverflow.com/users/20631223
last_edited: 2023-02-10T12:24:44Z
tags: [python, html, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 113
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cde40106281c7a1a00268dc2dde79f819b4e179a147f1502c48f19cfc77c8aad
---

# How to extract the details from particular HTML text

Asked by [Ajay Kk](https://stackoverflow.com/users/20631223) on Stack Overflow, <https://stackoverflow.com/q/75410558>, 2023-02-10, last edited 2023-02-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

from bs4 import BeautifulSoup

    html_content = """<div id="formContents" class="dformDisplay ">
    <div class="sectionDiv expanded">
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
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        form_data = soup.find("div",{"id":"formContents"})
        if form_data:
            section_data = soup.findAll("div",{"class":"sectionDiv expanded"})
            for datas in section_data:
                labels = datas.findAll("label",{"class":"fieldLabel"})
                for item in labels:
                    labels = item.text
                    print(labels)
                    entity_data = item.findAll("td").text
                    print(entity_data)
    
    except Exception as e:
        print(e)

My required output: 

    Address : 183 Pelham Wood Dr, Rock Hill, SC 29732. 

Is there any solution to get the particular output using `beautifulsoup`. I need to the address of the particular HTML source content.


  [1]: https://i.sstatic.net/dcRvL.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mkrieger1](https://stackoverflow.com/users/4621513)** (2023-02-10): Yes, beatifulsoup is made for this. What was the problem?
- **[Ajay Kk](https://stackoverflow.com/users/20631223)** (2023-02-10): I am unable to get the address 183 Pelham Wood Dr, Rock Hill, SC 29732 from the html content. But I get the label
