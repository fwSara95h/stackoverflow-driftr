---
title: "How to find the total number of pages on a website with BeautifulSoup?"
site: stackoverflow
question_id: 73977709
answer_id: 73984323
url: https://stackoverflow.com/a/73984323
author: "ouroboros1"
author_url: https://stackoverflow.com/users/18470692
posted: 2022-10-07T08:19:50Z
last_edited: never
accepted: true
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3bb1bb7f042828d6be19d92bb6468668884ef47ef40350b1e1fccac34125bf3e
role: another answer on the same question, kept as context; not my work
---

# Answer by [ouroboros1](https://stackoverflow.com/users/18470692) — 2022-10-07

Posted on Stack Overflow, <https://stackoverflow.com/a/73984323>, 2022-10-07; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Each of your pages (except the last one) will have an element like this:

```
<a class="page-link" 
href="https://skoodos.com/schools-in-uttarakhand?page=2" 
rel="next">Next »</a>
```
E.g. you can extract the link as follows (here for the first page):

```
link = soup.find('a', class_='page-link', href=True, rel='next')
print(link['href'])
https://skoodos.com/schools-in-uttarakhand?page=2
```
So, you could make your function recursive. E.g. use something like this:

```
import requests
from bs4 import BeautifulSoup

def data_fetch(url, results = list()):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    
    search_results = soup.find('section', {'id': 'search-results'})\
        .find(class_='container').find(class_='row')
    results.append(search_results)
    
    link = soup.find('a', class_='page-link', href=True, rel='next')
    
    # link will be `None` for last page (i.e. `page=11`)
    if link:
        # just adding some prints to show progress of iteration
        if not 'page' in url:
            print('getting page: 1', end=', ')
        url = link['href']
        # subsequent page nums being retrieved
        print(f'{url.rsplit("=", maxsplit=1)[1]}', end=', ')
        
        # recursive call
        return data_fetch(url, results)
    else:
        # `page=11` with no link, we're done
        print('done')
        
    return results

url = 'https://skoodos.com/schools-in-uttarakhand'
data = data_fetch(url)
```
So, a call to this function will print progress as:

```
getting page: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, done
```
And you'll end up with `data` with 11x `bs4.element.Tag`, one for each page.

```
print(len(data))
11
print(set([type(d) for d in data]))
{<class 'bs4.element.Tag'>}
```
Good luck with extracting the required info; the site is very slow, and the HTML is particularly sloppy and inconsistent. (e.g. you're right to note there is a `page-link` elem, which suggests there are 20 pages. But its visibility is set to `hidden`, so apparently this is just a piece of deprecated/unused code.)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[theycallmepix](https://stackoverflow.com/users/12320089)** (2022-10-07): Doesn't it slows down the speed of execution further? Like, calling the function recursively in the beginning just to get the count, then, starting processing/ solving the problem
- **[ouroboros1](https://stackoverflow.com/users/18470692)** (2022-10-08): You could win a few milliseconds by replacing the recursion with a `while link:` and simply repeating `resp = requests.get(url)` etc. But that's a trade-off btw repetitive code and minor gain. The slowness is influenced primarily by loading the urls, which is very slow, because the site is very outdated. E.g. I think you are indeed wise not to assume that `217` (results) is necessarily correct and/or implies a logical distribution across pages (e.g. 20 results per page, with remainder on last page). It probably does, but getting `next` ref seems less prone to error, in my opinion.
