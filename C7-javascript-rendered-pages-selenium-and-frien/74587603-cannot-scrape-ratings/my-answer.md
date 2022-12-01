---
title: "cannot scrape ratings"
site: stackoverflow
question_id: 74587603
answer_id: 74643531
url: https://stackoverflow.com/a/74643531
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-01T14:32:56Z
last_edited: 2022-12-02T14:59:38Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74643531/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 685c75b2ae33726fc44b18331c74fab95a532458b5f572a841043ada30bd8d65
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74643531>, 2022-12-01, last edited 2022-12-02; **accepted**; score 0. Text as retrieved 2026-10-12.

For getting the star rating breakdown (which seems to have no numeric display or meta value), I don't think there's any very simple-and-straight-forward short method since it's done [by css in a `style` tag connected by a class of the container element](https://i.sstatic.net/pATGa.png).

You could use something like `soup.select('style:-soup-contains(".css-1nuumx7")')` [ the `css-1nuumx7` part is specific to rating mentioned above], but [`:-soup-contains`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:-soup-contains) needs [`html5lib`](https://pypi.org/project/html5lib/) parser and can be a bit slow, so it's better to figure out the `data-emotion-css` attribute of the `style` tag instead:
```python
def getDECstars(starCont, mSoup, outOf=5,  isv=False):
    classList = starCont.get('class', [])
    if type(classList) != list: classList = [classList]
    classList = [str(c) for c in classList if str(c).startswith('css-')] 
    if not classList: 
        if isv: print('Stars container has no "css-" class')
        return None
    
    demc = classList[0].replace('css-', '', 1)
    demc_sel = f'style[data-emotion-css="{demc}"]'
    cssStyle = mSoup.select_one(demc_sel)
    if not cssStyle:
        if isv: print(f'Nothing found with selector {demc_sel}')
        return None
    
    cssStyle = cssStyle.get_text()
    errMsg = ''
    if '90deg,#0caa41 ' not in cssStyle: errMsg += 'No #0caa41'
    if '%' not in cssStyle.split('90deg,#0caa41 ', 1)[-1][:20]: 
        errMsg += ' No %'
    if not errMsg:
        rPerc = cssStyle.split('90deg,#0caa41 ', 1)[-1]
        rPerc = rPerc.split('%')[0]
        try:  
            rPerc = float(rPerc)
            if 0 <= rPerc <= 100:
                if type(outOf) == int and outOf > 0: rPerc = (rPerc/100)*outOf
                return float(f'{float(rPerc):.3}')
            errMsg = f'{demc_sel} --> "{rPerc}" is out of range'
        except: errMsg = f'{demc_sel} --> cannot convert to float "{rPerc}"' 
    if isv: print(f'{demc_sel} --> unexpected format {errMsg}')
    return None
``` 
**OR**, if you don't care so much about why there's a missing rating:
```python
def getDECstars(starCont, mSoup, outOf=5, isv=False):
    try:
        demc = [c for c in starCont.get('class', []) if c[:4]=='css-'][0].replace('css-', '', 1)
        demc_sel = f'style[data-emotion-css="{demc}"]'
        rPerc = float(mSoup.select_one(demc_sel).get_text().split('90deg,#0caa41 ', 1)[1].split('%')[0])
        return float(f'{(rPerc/100)*outOf if type(outOf) == int and outOf > 0 else rPerc:.3}')
    except: return None
```

---

Here's an example of how you might use it:
```python
pcCon = 'div.px-std:has(h2 > a.reviewLink) + div.px-std'
pcDiv = f'{pcCon} div.v2__EIReviewDetailsV2__fullWidth'
refDict = {
    'rating_num': 'span.ratingNumber',
    'emp_status': 'div:has(> div > span.ratingNumber) + span',
    'header': 'h2 > a.reviewLink',
    'subheader': 'h2:has(> a.reviewLink) + span',
    'pros': f'{pcDiv}:first-of-type > p.pb',
    'cons': f'{pcDiv}:nth-of-type(2) > p.pb'
}

subRatSel = 'div:has(> .ratingNumber) ~ aside ul > li:has(div ~ div)'
empRevs = []
for r in soup.select('li[id^="empReview_"]'):
    rDet = {'reviewId': r.get('id')}
    for sr in r.select(subRatSel):
        k = sr.select_one('div:first-of-type').get_text(' ').strip()
        sval = getDECstars(sr.select_one('div:nth-of-type(2)'), soup)
        rDet[f'[rating] {k}'] = sval
    
    for k, sel in refDict.items():
        sval = r.select_one(sel)
        if sval: sval = sval.get_text(' ').strip()
        rDet[k] = sval
    
    empRevs.append(rDet)
```
If `empRevs` is viewed as a table:


| reviewId           |   [rating] Work/Life Balance |   [rating] Culture & Values |   [rating] Diversity & Inclusion |   [rating] Career Opportunities |   [rating] Compensation and Benefits |   [rating] Senior Management |   rating_num | emp_status                          | header                                         | subheader                                                            | pros                               | cons                              |
|:-------------------|-----------------------------:|----------------------------:|---------------------------------:|--------------------------------:|-------------------------------------:|-----------------------------:|-------------:|:------------------------------------|:-----------------------------------------------|:---------------------------------------------------------------------|:-----------------------------------|:----------------------------------|
| empReview_71400593 |                            5 |                           4 |                                4 |                               4 |                                    5 |                            3 |            3 |                                     | great pay but bit of obnoxious enviornment     | Nov 26, 2022 - Sales Associate/Cashier   in   Bensalem, PA           | -Walmart's fair pay policy is ...  | -some locations wont build emp... |
| empReview_70963705 |                            3 |                           3 |                                2 |                               2 |                                    2 |                            2 |            2 | Former Employee                     | Walmart Employees Trained Thrown to the Wolves | Nov 10, 2022 - Data Entry                                            | Getting a snack at break was e...  | I worked at Walmart for a very... |
| empReview_71415031 |                            4 |                           4 |                                4 |                               4 |                                    4 |                            4 |            5 | Current Employee, more than 1 year  | Work                                           | Nov 27, 2022 - Warehouse Associate   in   Springfield, GA            | The money there is good during...  | It can get stressful at times ... |
| empReview_69136451 |                          nan |                         nan |                              nan |                             nan |                                  nan |                          nan |            4 | Current Employee                    | Walmart                                        | Sep 16, 2022 - Sales Associate/Cashier                               | I'm a EXPERIENCED WORKER.  I ✨... | In my opinion I believe that W... |
| empReview_71398525 |                            4 |                           3 |                                4 |                               3 |                                    4 |                            3 |            4 | Current Employee                    | Depends heavily on your team                   | Nov 26, 2022 - Personal Digital Shopper                              | I have a generally excellent t...  | Generally, departments are sho... |
| empReview_71227029 |                            1 |                           1 |                                1 |                               1 |                                    3 |                            1 |            1 | Former Employee, less than 1 year   | Managers are treated like a slave.             | Nov 19, 2022 - Auto Care Center Manager (ACCM)   in   Cottonwood, AZ | Great if you like working with...  | you only get to work in your a... |
| empReview_71329467 |                            1 |                           3 |                                3 |                               3 |                                    4 |                            1 |            1 | Current Employee, more than 3 years | No more values                                 | Nov 23, 2022 - GM Coach   in   Houston, TX                           | Pay compare to other retails a...  | Walmart is not a bad company t... |
| empReview_71512609 |                            5 |                           5 |                                5 |                               5 |                                    5 |                            5 |            5 | Former Employee                     | Walmart midnight stocker                       | Nov 30, 2022 - Midnight Stocker   in   Taylor, MI                    | 2 paid 15 min breaks and 1 hou...  | Honestly nothing that I can th... |
| empReview_70585957 |                            3 |                           4 |                                4 |                               4 |                                    4 |                            4 |            4 | Former Employee                     | Lots of Opportunity                            | Oct 28, 2022 - Human Resources People Lead                           | Plenty of opportunities if one...  | As with any job, management is... |
| empReview_71519435 |                            3 |                           4 |                                4 |                               5 |                                    4 |                            4 |            5 | Current Employee, more than 3 years | Lot of work but worth it                       | Nov 30, 2022 - People Lead                                           | I enjoy making associates live...  | Sometimes an overwhelming amou... |


> <sub>Markdown for the table above was printed with pandas:</sub>
> ```python
> erdf = pandas.DataFrame(empRevs).set_index('reviewId')
> erdf['pros'] = [p[:30] + '...' if len(p) > 33 else p for p in erdf['pros']]
> erdf['cons'] = [p[:30] + '...' if len(p) > 33 else p for p in erdf['cons']]
> print(erdf.to_markdown())
> ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jaevapple](https://stackoverflow.com/users/20143343)** (2022-12-01): Could not thank you even more! This is ABSOLUTELY the answer I am looking for. I will learn your code by heart. It looks very awesome to me, and I will google to learn it. Thank you so much.
- **me** (2022-12-01): @Jaevapple I'd be glad to help as much as I can, but I'm afraid I can't see any edits to your q and I don't quite understand what you mean by *"each review has the same total number of reviews"*... you can find number of pages by splitting the text from `soup.select_one('div[data-test="pagination-footer-text"]')` [ [at the bottom of the page](https://i.sstatic.net/MPqBX.png) ], and the next page link from the `href` of `soup.select_one('li:has(a.page.selected) + li a.page[href]')` [ see [this](https://stackoverflow.com/a/74334463/6146136) for an example of how to scrape paginated results ]
- **me** (2022-12-02): @Jaevapple I saw the bit in your q about missing 4-part sub-ratings. I've added updated version[s] of `getDECstars` at [https://pastebin.com/Q0GLwRv9](https://pastebin.com/Q0GLwRv9) (new/changed lines are marked with `## edit`), and that should take care of that particular issue
- **me** (2022-12-02): @Jaevapple but the problem remains of the `requests` failures... you could easily use selenium by replacing your `extract(pg)` function with [something like this](https://pastebin.com/VLZ2vPYK), but it appears that some of the needed `style` tags  disappear after the page loads so *none* of the sub-ratings might show
