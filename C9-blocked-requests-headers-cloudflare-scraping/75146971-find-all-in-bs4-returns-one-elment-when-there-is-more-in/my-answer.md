---
title: "FInd_all in bs4 returns one elment when there is more in the web page in"
site: stackoverflow
question_id: 75146971
answer_id: 75154564
url: https://stackoverflow.com/a/75154564
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-18T04:01:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75154564/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3eb4279b72c4e9acdd04436c14e20d6049c1ec94428581cb953f6effb9d9286c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75154564>, 2023-01-18; score 0. Text as retrieved 2026-10-12.

I get `[]` with your code; judging by [the text content][1], or when I break it print the response status and url

> ```python
> r = requests.get('https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-> 12g-oc/p/N82E16814137632?Description=gpu&cm_re=gpu-_-14-137-632-_-Product')
> print(f'<{r.status_code} {r.reason}> from {r.url}')
> # soup = bs(r.content , 'lxml')
> ```
 
> output:
> ```
> <200 OK> from https://www.newegg.com/areyouahuman?referer=/areyouahuman?referer=https%3A%2F%2Fwww.newegg.com%2Fmsi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc%2Fp%2FN82E16814137632%3FDescription%3Dgpu%26cm_re%3Dgpu-_-14-137-632-_-Product&why=8&cm_re=gpu-_-14-137-632-_-Product&Description=gpu
> ```

It's been redirected to a CAPTCHA...

---

Anyway, even if you get past that (I couldn't so I just pasted and parsed the response from my browser's [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) to test), all you can get from `page` is the source HTML, which **[does not contain][2]** any elements with `class="rating rating-4"`; using [selenium](https://medium.com/ymedialabs-innovation/2f8ad15efe25) and waiting for the page to finish loading yielded a [bit more][3], but even then there weren't any exact matches. 

<sup>[There were some matches when I inspected in browser, but **only if I wasn't in incognito mode**, which is likely why selenium didn't find them either.]</sup>

So, the site probably adds or removes some classes based on the source of the request. If you just want to get all elements with both the `rating` and `rating-4` classes (that will include the elements with **`class="rating is-large rating-4"`**), you can use `.find...` with [`lambda`](https://www.w3schools.com/python/python_lambda.asp) (or define [a separate function](https://beautiful-soup-4.readthedocs.io/en/latest/#a-function)) or use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) like

```python
the_rating = soup.select('.rating.rating-4') # shorter than 
# .find_all(lambda t: {'rating', 'rating-4'}.issubset(set(t.get('class', []))))
```

[Just make sure you have the full/correct HTML.]


  [1]: https://i.sstatic.net/K26WJ.png
  [2]: https://i.sstatic.net/xgpd5.png
  [3]: https://i.sstatic.net/zMgtk.png
