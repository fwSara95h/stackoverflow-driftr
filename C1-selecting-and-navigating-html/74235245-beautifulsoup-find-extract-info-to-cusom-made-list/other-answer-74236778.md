---
title: "BeautifulSoup find extract info to cusom-made list"
site: stackoverflow
question_id: 74235245
answer_id: 74236778
url: https://stackoverflow.com/a/74236778
author: "d r"
author_url: https://stackoverflow.com/users/19023353
posted: 2022-10-28T14:24:13Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 306bd87760d3e6bd7769080998f645ed137006c99876e9e7e8e659514413e8c7
role: another answer on the same question, kept as context; not my work
---

# Answer by [d r](https://stackoverflow.com/users/19023353) — 2022-10-28

Posted on Stack Overflow, <https://stackoverflow.com/a/74236778>, 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try it like below:
~~~python
from bs4 import BeautifulSoup

pages = [
'''
<html>
 <body>
  <span _ngcontent-dna-c199="" class="font-weight-bold">
   <span _ngcontent-dna-c199="" class="ng-star-inserted">
    <span _ngcontent-dna-c199="" translate="">
     issue_number
    </span>
    4 Näköispainos
   </span>
   <span _ngcontent-dna-c199="" class="ng-star-inserted">
    6.12.1939
   </span>
  </span>
 </body>
</html>
''',
'''
<html>
 <body>
  <span _ngcontent-sut-c199="" class="font-weight-bold">
   <span _ngcontent-sut-c199="" class="ng-star-inserted">
    <span _ngcontent-sut-c199="" translate="">
     issue_number
    </span>
    8
   </span>
   <span _ngcontent-sut-c199="" class="ng-star-inserted">
    1998
   </span>
  </span>
 </body>
</html>
''',
'''
<html>
 <body>
  <span _ngcontent-dgu-c199="" class="font-weight-bold">
   <span _ngcontent-dgu-c199="" class="ng-star-inserted">
    1905
   </span>
  </span>
 </body>
</html>
''' ]
i = -1
my_dct = {}
my_list = []
for page in pages:
    i += 1
    soup = BeautifulSoup(page, "lxml") # html_1, html_2, html_3
    spans = soup.find_all("span", attrs= {"class": "ng-star-inserted"})
    sp_0 = spans[0].span
    if sp_0:
        txt = sp_0.text.replace('\n', '').strip()
        if txt not in my_list:
            my_list.append(txt)
    else:
        my_list.append('None')
        
    sp_1 = spans[0]
    if sp_1 and len(spans) > 1:
        txt_1 = sp_1.text.replace('\n', '').replace(txt, '').strip()
        my_list.append(txt_1.split()[0])
        if len(txt_1.split()) > 1:
            my_list.append(txt_1.split()[1])
        else:
            my_list.append('None')
    else:
        my_list.append('None')
        
    if len(spans) > 1:
        txt_2 = spans[1].text.replace('\n', '').strip()
        my_list.append(txt_2)
    else:
        my_list.append('None')
        txt_2 = spans[0].text.replace('\n', '').strip()
        my_list.append(txt_2)
        
    my_dct['html_' + str(i + 1)] = my_list
    my_list = []
print(my_dct)

'''  R e s u l t :
{
  'html_1': ['issue_number', '4', 'Näköispainos', '6.12.1939'], 
  'html_2': ['issue_number', '8', 'None', '1998'], 
  'html_3': ['None', 'None', 'None', '1905']
}
'''
~~~
Regards...
