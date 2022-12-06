---
title: "Extract all text between two specific empty divs"
site: stackoverflow
question_id: 74696257
answer_id: 74699864
url: https://stackoverflow.com/a/74699864
author: "Barry the Platipus"
author_url: https://stackoverflow.com/users/19475185
posted: 2022-12-06T09:08:49Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f11484ba837d8ae71a518531b77b9ff4a69f8fda893249a3b869c690d3173ffc
role: another answer on the same question, kept as context; not my work
---

# Answer by [Barry the Platipus](https://stackoverflow.com/users/19475185) — 2022-12-06

Posted on Stack Overflow, <https://stackoverflow.com/a/74699864>, 2022-12-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is one way to get the text you want:

    from bs4 import BeautifulSoup as bs
    
    html = '''
    many <divs> </divs> and other tags
    
    <div class ="start"> </div>
    <div> bla bla bla </div>
    
    <div class ="start"> </div>
    <div> <i> <a> <span> <p> Text I want </p></span></a></i> </div>
    <div> <p> Text I want </p> <p> Text I want </p> </div>
    <div class ="end"></div>
    
    <div> bla bla bla </div>
    <div class ="end"></div>
    
    many <divs> </divs> and other tags
    '''
    soup = bs(html, 'html.parser')
    start_item = soup.select('div[class="start"]')[-1]
    
    for x in start_item.find_next_siblings():
        x_class = x.get('class')[0] if x.get('class') else None
        if x_class != 'end':       
            print('Wanted text:', x.text)
            
        else:
            print('reached the end')
            break

Result in terminal:

    Wanted text:      Text I want  
    Wanted text:   Text I want   Text I want  
    reached the end

See BeautifulSoup documentation [here](https://beautiful-soup-4.readthedocs.io/en/latest/).
