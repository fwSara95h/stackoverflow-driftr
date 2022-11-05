---
title: "Web Scraping 'Advice to management\" not printing from Glassdoor"
site: stackoverflow
question_id: 74253197
answer_id: 74331123
url: https://stackoverflow.com/a/74331123
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-05T20:07:46Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74331123/revisions
accepted: false
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 15206da37273da6ae4498c4940aceb3989cfe54626044ccfda72878729a5738d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74331123>, 2022-11-05; score 0. Text as retrieved 2026-10-12.

This method is quite similar to the second one added to [@Brze](https://stackoverflow.com/users/10848420/brze)'s [posted answer](https://stackoverflow.com/a/74275374/6146136), but I'm structuring it in a way that fits into the code in your question.

Although it's not in the html, the advice is inside a JavaScript object within a `script` tag, so you should extract that at the **beginning** of you `transform(soup)` function, as well as the ID of each review in the loop so that you can match them up:

```python
def transform(soup): #to get reviews
    try:
        scriptIn = soup.find(
            lambda s: s.name == 'script' and 
            'window.appCache={' in s.text and 
            '"apolloState"' in s.text
        ).text # get the contents of script tag (JavaScript)

        #### apolloJson = .... #### (see next section) ####

        empRevs = [
            v['reviews'] for k, v in apolloJson['ROOT_QUERY'].items() 
            if 'employerReviews' in k and 'reviews' in v
        ][0]
    except:
        empRevs = []
  

    divs = soup.find_all('div', class_='gdReview')
    for item in divs: 
        try:
          revId = int(item.find_parent('li').get('id').replace('empReview_', ''))
        except:
          revId = None

        #### Title, Rating, Employee_Situation, Pros, Cons = ... ####

        try:    
          Advice_To_Management = [
              r['advice'] for r in empRevs if r['reviewId'] == revId
          ][0]
        except: 
          Advice_To_Management = None

        #### Auhtor_Info = ... ####
        #### Reviews = {...}  ####
        #### ReviewsList.append(Reviews) ####
    return
```

<hr>

There are two ways to get the `apolloJson` variable that I skipped defining; the simpler way would be but just splitting the string

```python
# import json

        apolloJson = json.loads(',"apolloState":'.join(
            scriptIn.strip().split(',"apolloState":')[1:]
        )[:-2])
```

However, that assumes that `apolloState` will always be the last item inside the last (or only) object in the script, so I think it will be safer to use a js parser like `slimit`
```python
# import json
# import slimit
# from slimit.visitors import nodevisitor


        tree = slimit.parser.Parser().parse(scriptIn)
        treeDesc = []
        apolloJson = '{}'

        for n in nodevisitor.visit(tree): 
            if n.children()[0].left.to_ecma() == 'window.appCache':
                treeDesc = n.children()[0].right.children() 
                break

        for c in treeDesc:
            if c.left.to_ecma() == '"apolloState"': 
                apolloJson = c.right.to_ecma()
                break

        apolloJson = json.loads(apolloJson)
```
[I don't know if `slimit` has any native functions that work like `find` in `bs4`, so I had to use loops to search....]
