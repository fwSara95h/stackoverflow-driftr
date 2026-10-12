# Code from my Stack Overflow answer https://stackoverflow.com/a/74709035 (posted 2022-12-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
content=soup.findAll(attrs={'class':'td-post-content'})#extracting only text part
if not content: 
   print('NO .td-post-content CONTENT FROM', j[0])
   continue ## <--- SKIP REST OF LOOP TO NEXT URL'S LOOP
content=content[0].text.replace('\xa0',"  ").replace('\n',"  ")#replace end line symbol with space

# --- block 2 ---
## ADD TO THE BEGINNING OF YOUR CODE:
# import os
# def logError_scrapes... ## PASTE FUNCTION DEFINITION FROM https://pastebin.com/cxGH50Mc

## INSIDE THE LOOP:
   if not content:
      # print('NO .td-post-content CONTENT FROM', j[0])
      logError_scrapes(
           logId=f'row_{i}-url_{url_id}', url=j[0], req=page
         , msg='No .td-post-content in fetched html'
         # , conf={'saveHtml': True} # to save html to file (instead of csv column)

         # if you want to save prettified html in csv column:
         # , rSoup=soup , conf={'saveHtml': True, 'minify': False} 
      )
      continue ## <--- SKIP REST OF LOOP TO NEXT URL'S LOOP

# --- block 3 ---
title=title[16].text.replace('\n',"  ").replace('/',"")
