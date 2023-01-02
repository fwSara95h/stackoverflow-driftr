---
title: "Beautiful Soup Error AttributeError: ResultSet object has no attribute 'get"
site: stackoverflow
question_id: 74986466
url: https://stackoverflow.com/q/74986466
asked: 2023-01-02T19:48:04Z
asked_by: "natan specialist"
asked_by_url: https://stackoverflow.com/users/19565585
last_edited: 2023-01-02T19:59:50Z
tags: [python, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 288
answer_count: 1
accepted_answer_id: 74987772
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: df78f7e6db9ef55aa27862ce59279f275c5a93c006386559d7e8cd683d49a1e3
---

# Beautiful Soup Error AttributeError: ResultSet object has no attribute 'get

Asked by [natan specialist](https://stackoverflow.com/users/19565585) on Stack Overflow, <https://stackoverflow.com/q/74986466>, 2023-01-02, last edited 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to write a program using BeautifulSoup and Requests. There are a bunch of XML files which I have extracted from a large XML document and stored them into a dict called `all_sitemaps` with respective country name. Each dict key is mapped against bunch of xml files associated with each country and looks like below:

```
{'uk/en': ['file-1.xml',
  'file-2.xml',
  'file-3.xml',
  'file-4.xml'],
 'ca/en': ['file-1.xml',
  'file-2.xml',
  'file-3.xml']}
```
Next step is to run a GET requests on each individual .xml files and extract certain nodes and their text.

Below is the code:

```
urls = {}
s = requests.session()

for a,b in all_sitemaps.items():
    for urls in b:
        one_sitemap = urls
        pip_sitemap = s.get(one_sitemap)
        soup= bs4.BeautifulSoup(pip_sitemap.text,'html.parser')
        s = soup.find_all("loc")
        
        for url in s:
            loc = url.getText()

            if loc not in urls:
                urls[loc] = []
            for b in a.findNextSiblings():
                if b.get("href") != None:
                    urls[loc].append(b.get("href"))
```

I wish to scrap all `<loc>urls</loc>` from all the sitemap files stored as sublists in `all_sitemaps` dict but the program runs only one iteration over first list element `https://www.example.com/file-1.xml` and starts throwing an error as below:

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In [231], line 7
      5 for urls in b:
      6     one_sitemap = urls
----> 7     pip_sitemap = s.get(one_sitemap)
      8     soup= bs4.BeautifulSoup(pip_sitemap.text,'html.parser')
      9     s = soup.find_all("loc")

File c:\Users\natan12\Documents\My-Work-Files\python\udemy\vs_code\ARTOO\lib\site-packages\bs4\element.py:2289, in ResultSet.__getattr__(self, key)
   2287 def __getattr__(self, key):
   2288     """Raise a helpful exception to explain a common code fix."""
-> 2289     raise AttributeError(
   2290         "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
   2291     )

AttributeError: ResultSet object has no attribute 'get'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```
When I try to run in small iterations to print all sitemaps as strings it works fine so can someone please suggest how to overcome this? Thanks!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Michael Butscher](https://stackoverflow.com/users/987358)** (2023-01-02): Show the full traceback of the error as properly formatted text in the question.
- **[natan specialist](https://stackoverflow.com/users/19565585)** (2023-01-02): I have added the full stack error in my question. Thanks!
- **[Michael Butscher](https://stackoverflow.com/users/987358)** (2023-01-02): The code snippet doesn't match the code shown in the traceback.
- **[natan specialist](https://stackoverflow.com/users/19565585)** (2023-01-02): my apologies Michael. I was trying to be precise but now I have pasted full code.
- **[Michael Butscher](https://stackoverflow.com/users/987358)** (2023-01-02): You are using variable "s" first for the requests session but overwrite it then with a Beautifulsoup ResultSet so that in the second iteration of the `for urls in b` loop the code tries to access a "get" attribute of the ResultSet.
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2023-01-02): Please see what a [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) is. Either confirm the url of the page you're trying to scrape (if publicly accessible), or alternatively post the page html.
