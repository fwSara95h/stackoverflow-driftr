---
title: "Failing do the scraping"
site: stackoverflow
question_id: 75120430
answer_id: 75121512
url: https://stackoverflow.com/a/75121512
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-14T21:53:49Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75121512/revisions
accepted: false
score: 2
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 91931afd69a924fa59e081838fbee785fe36ea285f99fe33ca0fa41ae03fae85
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75121512>, 2023-01-14; score 2. Text as retrieved 2026-10-12.

> ```python 
> r= requests.get(url, headers) 
> ```

You need to use `headers=headers` because if it's not specified, the second [argument](https://requests.readthedocs.io/en/latest/api/#requests.request) is `params`.

---

> ```python 
> page = requests.get('https://www.google.com/search?q=RaindropsKeepFallinonMyHead+lyrcis&')
> soup = BeautifulSoup(page.content, 'html.parser').find_all('div',jsname="WbKHeb") 
> print(soup) 
> ```

I just get `[]` with this. (Maybe `jsname="WbKHeb"` is only in the html for specific devices?) 

With your second method, I just get `None`....

---

You can try **`.select('div:has(>span:has(>span):has(~span>span))~div div')`** instead of *`.find_all('div',jsname="WbKHeb")`*. 

<sub>**(In case you're not familiar with it, [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) uses [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) to find element tags.)**</sub>

```python
title = 'Raindrops Keep Fallin on My Head'
url = f'https://www.google.com/search?q={title.replace(" ", "+")}+lyrics'
r = requests.get(url)
print('[', r.status_code, r.reason, 'from', r.url, f']\n{"-"*85}\n')
# r.raise_for_status()

lcSel = 'div:has(>span:has(>span):has(~span>span))~div div'
print(('\n\n'+'-'*80+'\n\n').join([el.get_text(' ').strip() + (
    f' ( {el.a.get("href")} )' if el.a else ''
) for el in [soup.select_one(s) for s in [
    f'{lcSel} span>div:has(a)', 
    f'{lcSel} span:has(>div a)+span', 
    f'{lcSel}:not(:has(span))'
]]]))
```

should print

```lang-none
[ 200 OK from https://www.google.com/search?q=Raindrops+Keep+Fallin+on+My+Head+lyrics ]
-------------------------------------------------------------------------------------

Source:  LyricFind ( https://lyrics.lyricfind.com/ )

-------------------------------------------------------------------------------------

Songwriters: Burt F. Bacharach /  Hal David
Raindrops Keep Fallin' on My Head lyrics © BMG Rights Management, Royalty Network

-------------------------------------------------------------------------------------

Raindrops are falling on my head
And just like the guy whose feet are too big for his bed
Nothing seems to fit
Those raindrops are falling on my head, they keep falling

So I just did me some talking to the sun
And I said I didn't like the way he got things done
Sleeping on the job Raindrops are falling on my head
And just like the guy whose feet are too big for his bed
Nothing seems to fit
Those raindrops are falling on my head, they keep falling

So I just did me some talking to the sun
And I said I didn't like the way he got things done
Sleeping on the job
Those raindrops are falling on my head, they keep falling

But there's one thing I know
The blues they send to meet me
Won't defeat me, it won't be long
Till happiness steps up to greet me

Raindrops keep falling on my head
But that doesn't mean my eyes will soon be turning red
Crying's not for me
'Cause I'm never gonna stop the rain by complaining
Because I'm free
Nothing's worrying me

It won't be long till happiness steps up to greet me

Raindrops keep falling on my head
But that doesn't mean my eyes will soon be turning red
Crying's not for me
'Cause I'm never gonna stop the rain by complaining
Because I'm free
Nothing's worrying me
```
