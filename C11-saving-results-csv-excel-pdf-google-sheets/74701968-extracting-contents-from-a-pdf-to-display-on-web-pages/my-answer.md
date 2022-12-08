---
title: "Extracting contents from a PDF to display on web pages"
site: stackoverflow
question_id: 74701968
answer_id: 74724548
url: https://stackoverflow.com/a/74724548
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-08T01:22:33Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74724548/revisions
accepted: false
score: 0
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b1d865f5ab0b415da955ad8a7e12990d8625efcae31293c5353cacf851f2c858
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74724548>, 2022-12-08; score 0. Text as retrieved 2026-10-12.

For the numbering with `:before` in css, you can try to extract the selector/s for the numbered items with a function like this

```python
def getLctrSelectors(stsh):  
    stsh = stsh.get_text() if stsh else ''

    ll_ids = list(set([
        l.replace('>li', '> li').split('> li')[0].strip() 
        for l in stsh.splitlines() if l.strip()[:1] == '#' 
        and '> li' in l.replace('>li', '> li') and 
        'counter-increment' in l.split('{')[-1].split(':')[0]
    ]))
    for i, l in enumerate(ll_ids): 
        sel = f'{l} > li > *:first-child'
        ll_ids[i] = (sel, 1)
        crl = [
            ll for ll in stsh.splitlines() if ll.strip().startswith(l)
            and 'counter-reset' in ll.split('{')[-1].split(':')[-2:][0] 
        ][:1] 
        if not crl: continue
        
        crl = crl[0].split('{')[-1].split('counter-reset')[-1].split(':')[-1]
        crl = [w for w in crl.split(';')[0].split() if w.isdigit()] 
        ll_ids[i] = (sel, int(crl[-1]) if crl else 1)
    
    return ll_ids
```

(It should take a `style` tag as input and return a list of selectors and starting counts - like `[('#l1 > li > *:first-child', 3)]` for your sample html.)

You can use it in your code to insert the numbers into the text in the bs4 tree:

```python
                soup = BeautifulSoup(fp, "html.parser") 
                for sel, ctStart in getLctrSelectors(soup.select_one('style')):
                    for i, lif in enumerate(soup.select(sel)):
                        lif.insert(0, f'{i + ctStart}. ')
                
                para_counter = 1
                ### REST OF CODE ###
```

---

I'm not sure I can help you with paragraphs and tables issues... Are you sure the site uses the same pdfs as you have? (Or that they use pdfs at all rather than something closer to the original/raw data?) Your pdf itself looked rather different from its corresponding page on the site.
