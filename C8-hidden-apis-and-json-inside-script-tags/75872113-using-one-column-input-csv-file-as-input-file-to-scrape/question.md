---
title: "Using one-column input csv file as input file to scrape webpages (with potential next pages)"
site: stackoverflow
question_id: 75872113
url: https://stackoverflow.com/q/75872113
asked: 2023-03-29T00:32:04Z
asked_by: "PressMeister"
asked_by_url: https://stackoverflow.com/users/21433696
last_edited: 2023-03-29T18:08:28Z
tags: [csv, beautifulsoup]
score: 0
views_at_snapshot: 71
answer_count: 1
accepted_answer_id: 75894956
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a4138a4cf6daaa47239839286301c0cfa2531fed6a18e9f563910bff8777618d
---

# Using one-column input csv file as input file to scrape webpages (with potential next pages)

Asked by [PressMeister](https://stackoverflow.com/users/21433696) on Stack Overflow, <https://stackoverflow.com/q/75872113>, 2023-03-29, last edited 2023-03-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Baby Pythonite here. I have a script (see below) with which I'm currently able to scrape a single URL that may or not have "next pages." 

I'm now trying to **expand **the functionality of the script to read **multiple URLs** from a one-column csv file. Currently, my input file has the following URLs:

`https://dockets.justia.com/search?parties=Agfa&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Aggregate+Industries+Management&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Agility+Fuel+Solutions&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Agrana&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Agtek+Development&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Ahead&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27
https://dockets.justia.com/search?parties=Ahold&cases=between&sort-by-last-update=false&after=2015-1-1&before=2015-1-1&before=2023-3-27`

How do I make my script read these URLs from the csv file; and then use those URLs to capture/pick up/scrape the case URLs in those html pages. The element looks like this:

`<div class="has-padding-content-block-30 -zb">
                <a href="https://dockets.justia.com/docket/illinois/ilndce/1:2017cv02145/337903" class="case-name"><strong>RAH Color Technologies LLC v. Agfa Gevaert N V et al</strong></a>`

I just need it to print to the console as with the current script. I hope that's a reasonably clear description of my dilemma.

This is my script in its current state:



```
from aiohttp import ClientSession
from pyuseragents import random
from bs4 import BeautifulSoup
from asyncio import run

class DocketsJustia:

    def __init__(self):
        self.headers = {
            'authority': 'dockets.justia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.5',
            'cache-control': 'max-age=0',
            'referer': 'https://dockets.justia.com/search?parties=Agfa&cases=between&sort-by-last-update=false&after=2015-1-1&before=2023-3-27',
            'user-agent': random(),
        }

        self.PatchFile = "nametxt.txt"

    async def Parser(self, session):
        count = 1

        while True:

            params = {
                'parties': 'Agfa',
                'page': f'{count}',
            }

            async with session.get(f'https://dockets.justia.com/search?parties=Agfa&cases=between&sort-by-last-update=false&after=2015-1-1&before=2023-3-27&page={count}',
                                   params=params) as response:
                links = BeautifulSoup(await response.text(), "lxml").find_all("div", {
                    "class": "has-padding-content-block-30 -zb"})

                for link in links:
                    try:
                        case_link = link.find("a", {"class": "case-name"}).get("href")
                        case_number = link.find("span", {"class": "citation"}).text
                        print(case_number + "\t" + case_link + "\n")

                        with open(self.PatchFile, "a", encoding='utf-8') as file:
                            file.write(case_number + "\t" + case_link + "\n")
                    except:
                        pass
            count += 1

    async def LoggerParser(self):
        async with ClientSession(headers=self.headers) as session:
            await self.Parser(session)

def StartDocketsJustia():
    run(DocketsJustia().LoggerParser())

if __name__ == '__main__':
    StartDocketsJustia()

```

As suggested, but I'm getting a SyntaxError:

    from aiohttp import ClientSession
    from pyuseragents import random
    from bs4 import BeautifulSoup
    from asyncio import run
    
    class DocketsJustia:
    
        def __init__(self):
            self.headers = {
                'authority': 'dockets.justia.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.5',
                'cache-control': 'max-age=0',
                'referer': 'https://dockets.justia.com/search?parties=Agfa&cases=between&sort-by-last-update=false&after=2015-1-1&before=2023-3-27',
                'user-agent': random(),
            }
    
            self.PatchFile = "nametxt.txt"
    
    #    old line: async def Parser(self, session):
        async def Parser(selfself, session, searchUrl):
            count = 1
    
            while True:
    
                params = {
                    'parties': 'Agfa',
                    'page': f'{count}',
                }
    
                async with session.get(searchUrl, params=params as response:
                    links = BeautifulSoup(await response.text(), "lxml").find_all("div", {
                        "class": "has-padding-content-block-30 -zb"})
    
                    for link in links:
                        try:
                            case_link = link.find("a", {"class": "case-name"}).get("href")
                            case_number = link.find("span", {"class": "citation"}).text
                            print(case_number + "\t" + case_link + "\n")
    
                            with open(self.PatchFile, "a", encoding='utf-8') as file:
                                file.write(case_number + "\t" + case_link + "\n")
                        except:
                            pass
                count += 1
    
        async def LoggerParser(self):
    #       old line: async with ClientSession(headers=self.headers) as session:
            searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])
                for url in searchUrls: await self.Parser(session, url)
    
    def StartDocketsJustia():
        run(DocketsJustia().LoggerParser())
    
    if __name__ == '__main__':
        StartDocketsJustia()

I had to import pandas (as suggested in `searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])` and I don't seem to be getting any error message. I changed the script as suggested but seem to be getting no output (at all)). This is what I'm running:

    from aiohttp import ClientSession
    from pyuseragents import random
    from bs4 import BeautifulSoup
    from asyncio import run
    import pandas as pd
    
    class DocketsJustia:
    
        def __init__(self):
            self.headers = {
                'authority': 'dockets.justia.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.5',
                'cache-control': 'max-age=0',
                'user-agent': random(),
            }
    
            self.PatchFile = "nametxt.txt"
    
    #    old line: async def Parser(self, session):
        async def Parser(selfself, session, searchUrl):
            count = 1
    
            while True:
                async with session.get(f"{searchUrl}&page={count}") as response:
                    links = BeautifulSoup(await response.text(), "lxml").find_all("div", {
                        "class": "has-padding-content-block-30 -zb"})
    
                    for link in links:
                        try:
                            case_link = link.find("a", {"class": "case-name"}).get("href")
                            case_number = link.find("span", {"class": "citation"}).text
                            print(case_number + "\t" + case_link + "\n")
    
                            with open(self.PatchFile, "a", encoding='utf-8') as file:
                                file.write(case_number + "\t" + case_link + "\n")
                        except:
                            pass
                count += 1
    
        async def LoggerParser(self):
            async with ClientSession(headers=self.headers) as session:
                searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])
                for url in searchUrls:
                    await self.Parser(session, url)
    
    def StartDocketsJustia():
        run(DocketsJustia().LoggerParser())
    
    if __name__ == '__main__':
        StartDocketsJustia()

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-03-29): parametrize the search url for `Parser` like *`def Parser(self, session, searchUrl)`* and then have *`...session.get(searchUrl, params=params) as response:....`*
- **me** (2023-03-29): and in `LoggerParser` read in the URLs with something like *`searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])`* and loop through them with something like `for url in searchUrls: await self.Parser(session, url)`
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-29): @Driftr95 Thanks a million... assuming that I implemented your suggestion correctly (see addendum to my original posting above), I'm getting a syntax error in line 31 - is it the "response" that is the issue. Also, quick question - and I'm still struggling with understanding how everything works, so bear with me - should the 'referrer' be static? It is currently set to https://dockets.justia.com/search?parties=Agfa&cases= ... 2023-3-27.
- **me** (2023-03-29): As for the [referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer), it's generally used just to indicate which page you were on just before that request, but I suggest omitting it entirely unless it's absolutely necessary (is it? I don't remember needing headers at all for requests to this site - did you encounter any issues?)
- **me** (2023-03-29): And the syntax error is likely because you forgot to close the brackets after `params=params`; btw, I think you only need either the `params` or the part of the URL after the `?` and since you're getting the whole URL you don't need to be using `params` at all - just *`...session.get(f'{searchUrl}&page={count}') as response:..`*.
- **me** (2023-03-29): However, if you want to pass the parameters as `params`, I suggest looking into [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) - after importing what you need with *`from urllib.parse import urljoin, urlsplit, parse_qsl`*, use `split_url = urlsplit(searchUrl)` to break it down, and then form `params` with *`params = dict(parse_qsl(split_url.query)+[('page',f'{count}')])`* and then form the request like *`...session.get(urljoin(f'{split_url.scheme}://{split_url.netloc}', split_url.path), params=params) as response:...`*
- **me** (2023-03-29): Btw, you still need the *`async with ClientSession(headers=self.headers) as session:`* line in `LoggerParser` [and `searchUrls` can be defined before it, I think] - `await` probably doesn't make sense without `async` and you definitely need `session` to pass to the `Parser` function. I'm not entirely sure about the order of things because I don't have much experience with `async...await`
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-29): @Driftr95 Thanks so much for your suggestions (again!!)! Encouragingly, with your suggested changes I'm no longer getting any error messages. Less encouragingly, I'm not getting any messages at all... the script just seems to "hang". I've appended the script in its current state to the original post.
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-29): @Driftr95 Sorry, my mistake - it does seem to scrape. I lost my internet connection for a while! Again, thanks so much for your help!
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-29): @Driftr95 Ha, ha... I was wondering why I received so many hits on so few URLs until I terminated it.  I just noticed that the script captures the same 83 URLs in a loop. Have to figure that one out...
- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-03-29): @Driftr95  I believe I've finally figured out what is going on. The current script -- i.e., the last script iteration in my posting -- takes the first URL item in the input_file.csv (i.e., Row 1). If nothing is found, it shows nothing/just hangs. If I rerun the script, it moves on to the URL in the second row and continues to loop that page until I stop it manually (but doesn't move on to next pages) . Third row, same pattern. You wouldn't happen to have any nifty suggestions as to how to have it move from item to item in the csv file, scrape the next pages (if any), and stop looping?
- **me** (2023-03-29): About why they don't move to the next page, [I can't tell but] **is the *`count += 1`* line properly indented to be included in the `while` loop?** It should be at the same indentation as *`async with session.get...`* otherwise the loop keeps iterating over the same `count`/`page`
- **me** (2023-03-29): As for why you have to stop it manually, the *`while True:...`* inside `Parser`  is an [**infinite loop**](https://www.tutorialspoint.com/How-to-prevent-loops-going-into-infinite-mode-in-Python) with nothing to break it.
- **me** (2023-03-29): You should add `if not links: break` at the end of it just before [or just after] `count += 1` to stop looping when you reach a *`page={count}`* url that doesn't have any more links for you; and maybe also add an *`if count>max_page: break`* with `max_page` set to a [high enough] number that you would have manually stopped at.... Btw you can find [the line with the pagination progress](https://i.sstatic.net/pZjx6.png) with `soup.find('div', class_='row-label')` if you want to print that as well [could also use that as a condition for breaking, since it will disappear after the last page].
- **me** (2023-03-31): Glad to help! [I only answered through comments before since I wasn't sure about any of it since idk how much behaviors change when using `async...await`, so it's quite good to know it worked out.]
