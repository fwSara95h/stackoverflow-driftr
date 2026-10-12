# Code from my Stack Overflow answer https://stackoverflow.com/a/76444181 (posted 2023-06-09), extracted verbatim; may need the question's context to run.
for every_review in soup.findAll('shreddit-comment-tree', {'id':'comment-tree'}):
  for rev in every_review.findAll('div', {'class':'md pl-[28px] xs:pl-xl text-14'}):
    for d in rev.findAll('div', {'id':'-post-rtjson-content'}):
      print(d.p.text if d.p else '!EMPTY -post-rtjson-content!') ## JUST IN CASE
