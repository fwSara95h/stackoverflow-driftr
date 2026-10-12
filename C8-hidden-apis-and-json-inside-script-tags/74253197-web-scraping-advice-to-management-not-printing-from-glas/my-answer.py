# Code from my Stack Overflow answer https://stackoverflow.com/a/74331123 (posted 2022-11-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
# import json

        apolloJson = json.loads(',"apolloState":'.join(
            scriptIn.strip().split(',"apolloState":')[1:]
        )[:-2])

# --- block 3 ---
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
