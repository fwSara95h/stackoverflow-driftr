---
title: "Reusable Beautiful Soup Parser/Config?"
site: stackoverflow
question_id: 74098931
answer_id: 74104518
url: https://stackoverflow.com/a/74104518
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-18T00:37:02Z
last_edited: 2022-10-18T00:58:27Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74104518/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0a28746aabfbe0b5f80d122029027da07ebe71172bab940c0156b2abd9e668f4
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74104518>, 2022-10-18, last edited 2022-10-18; **accepted**; score 1. Text as retrieved 2026-10-12.

With BeautifulSoup, I strongly prefer [using `select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) and `select_one` to using `find_all` and `find` when scraping nested elements. (If you're not used to working with CSS selectors, I find the [w3schools reference page](https://www.w3schools.com/cssref/css_selectors.asp) to be a good cheatsheet for them.)

If you defined a function like 
```python
def getSoupData(mSoup, dataStruct, maxDepth=None, curDepth=0):
    if type(dataStruct) != dict:
        # so selector/targetAttr can also be sent as a single string 
        if str(dataStruct).startswith('"ta":'):
            dKey = 'targetAttr'
        else:
            dKey = 'cssSelector'
        dataStruct = str(dataStruct).replace('"ta":', '', 1)
        dataStruct = {dKey: dataStruct}

    # default values: isList=False, items={}
    isList = dataStruct['isList'] if 'isList' in dataStruct else False
    if 'items' in dataStruct and type(dataStruct['items']) == dict:
        items = dataStruct['items']
    else: items = {}

    # no selector -> just use the input directly
    if 'cssSelector' not in dataStruct:
        soup = mSoup if type(mSoup) == list else [mSoup]
    else:
        soup = mSoup.select(dataStruct['cssSelector'])
        # so that unneeded parts are not processed:
        if not isList: soup = soup[:1]

    # return empty nothing was selected
    if not soup: return [] if isList else None

    # return text or attribute values - no more recursion
    if items == {}:
        if 'targetAttr' in dataStruct:
            targetAttr = dataStruct['targetAttr']
        else:
            targetAttr = '"text"'  # default

        if targetAttr == '"text"':
            sData = [s.get_text(strip=True) for s in soup]
        # can put in more options with elif
        else:
            sData = [s.get(targetAttr) for s in soup]

        return sData if isList else sData[0]

    # return error - recursion limited
    if maxDepth is not None and curDepth > maxDepth:
        return {
            'errorMsg': f'Maximum [{maxDepth}] exceeded at depth={curDepth}'
        }

    # recursively get items
    sData = [dict([(i, getSoupData(
        s, items[i], maxDepth, curDepth + 1
    )) for i in items]) for s in soup]

    return sData if isList else sData[0]
    # return list only if isList is set
```
you can make your data structure as nested as your html structure [because the function is recursive]....if you want that for some reason; but also, you can set `maxDepth` to limit how nested it can get - if you don't want to set any limits, you can get rid of both `maxDepth` and `curDepth` as well as any parts involving them.

Then, you can make your config file something like
```json
{
    "name": "Paedriactia",
    "data_structure": {
        "cssSelector": "div.section__inner",
        "items": {
            "Issue": "p.section__spitzmarke",
            "Articles": {
                "cssSelector": "article",
                "items": {
                    "Title": "h3.teaser__title",
                    "Author": "p.teaser__authors" 
                },
                "isList": true
            }
        },
        "isList": true
    }
    "url": "https://www.paediatrieschweiz.ch/zeitschriften/"
}
```
[`"isList": true` here is equivalent to your `"find_all": true`; and your "subunits" are also defined as "items" here - the function can differentiate based on the structure/dataType.]

Now the same data that you showed [at the beginning of your question] can be extracted with
```python
# import json
configC = json.load(open('crawlerConfig_paedriactia.json', 'r'))

url = configC['url']
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

dStruct = configC['data_structure']
getSoupData(soup, dStruct)
```

For this example, you could add the article links by adding `{"cssSelector": "a.teaser__inner", "targetAttr": "href"}` as `...Articles.items.Link`. 

<br>

Also, note that [because of the defaults set at the beginning in the function], `"Title": "h3.teaser__title"` is the same as
```json
"Title": { "cssSelector": "h3.teaser__title" }
```
and 
```json
"Link": "\"ta\":href"
```
 would be the same as 
```json
"Link": {"targetAttr": "href"}
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[frumsky](https://stackoverflow.com/users/13085376)** (2022-10-19): this is fantastic and exactly what I was trying to get at. I have tested this out and achieves the intended output, I will test out a few other scenarios. In the meantime I'm still trying to understand the function code for myself. I really appreciate this help!
- **me** (2022-10-19): Glad to help! (BTW, if it helps understand the function's code quicker : just focus on the lines with `sData` first- those are the essential bits; the rest are just setting defaults to make parts of the config format optional, and some error handling.)
