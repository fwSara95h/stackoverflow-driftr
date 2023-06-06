---
title: "How to handle the \"tel:\" and \"mailto:\" parameters using BeautifulSoup4?"
site: stackoverflow
question_id: 76413914
answer_id: 76414759
url: https://stackoverflow.com/a/76414759
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-06T12:40:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76414759/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4df4162c1e24abef45cddc1ba2ce9c94edb328e83dca814173e6cf93bac1859a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76414759>, 2023-06-06; **accepted**; score 0. Text as retrieved 2026-10-12.

You need to check for valid url *before* using *`requests.get`* at the beginning of `extract_url` - maybe redefine it to something like:

```py
def extract_url(url):
    ## check BEFORE request
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        return []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []

    ## add href=True to find_all --> no need to check if href
    for link in soup.find_all('a', href=True):
        urls.append(urljoin(url, link.get('href') ))
```

---

If you want to also parse and check `href`:

```py
    for link in soup.find_all('a', href=True):
        parsed_href = urlparse(href := link.get('href'))
        if parsed_href.scheme in ['', 'http', 'https']:
            urls.append(urljoin(url, href))
```

---

On another note:

- It's a bit dangerous to crawl recursively, as you are with `crawl_helper`, since you risk running into [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError). 
- A queue-based crawler might be better - where you loop through a list but add new URLs to that list within the loop. Even then, you risk getting stuck in an infinite loop unless you set some kind of limit on the size of the queue or on the size of `visited`. Something like
  ```py
  def crawl(url, word, max_visits=1000):
      visited = set()
      dead_pages = set()
      url_queue = [url]

      for url in url_queue:  # loop instead of recursion
          if url in visited:
              return
          visited.add(url)

          status_code = check_url(url)
          if status_code == 404:
              dead_pages.add(url)

          if word in url:
              print(f'URL "{url}" contains "{word}".')

          urls = extract_url(url)

          ## add to queue instead of recursive call
          url_queue += [u for u in urls if u not in url_queue] 

          if not len(visited) < max_visits:
              break ## stop when limit is reached


      return dead_pages
  ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[yuji09](https://stackoverflow.com/users/22029363)** (2023-06-06): Thank you @Driftr95, I've modified my code based on yours and now it is working. And also thank you for the heads up for the RecursionError, I'll keep that in mind.
