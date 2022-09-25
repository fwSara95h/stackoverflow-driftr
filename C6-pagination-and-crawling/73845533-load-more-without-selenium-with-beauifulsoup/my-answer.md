---
title: "Load more without Selenium with beauifulsoup"
site: stackoverflow
question_id: 73845533
answer_id: 73846749
url: https://stackoverflow.com/a/73846749
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-25T18:06:06Z
last_edited: 2022-09-25T19:44:49Z
revisions: 3
revision_history: https://stackoverflow.com/posts/73846749/revisions
accepted: false
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 72bc28c9d2945dc919b364668395bcbd9ac4c6812e89a55010362e091142a71d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73846749>, 2022-09-25, last edited 2022-09-25; score 1. Text as retrieved 2026-10-12.

If you inspect the "Load More" button in dev tools, [you can see that it's wrapped][1] in a `div` with `class="load-more-data"` and a `data-key` attribute. And if you [observe the "Network" tab of the dev tools][2] after clicking on the "Load More" button, you might see that a GET request has been sent using the `data-key` as the "paginationKey" parameter.

So now you can use something like the function below to keep retrieving the link to load more reviews:

    def getMoreRevs(rSoup, rootUrl='https://www.imdb.com', lmSelector='div.load-more-data'):
      loadMore = rSoup.select_one(lmSelector)
      if loadMore: 

        if 'data-key' not in loadMore.attrs:
          print(f'not data-key attribute in {lmSelector} :\n', loadMore)
          return None

        dKey = loadMore.attrs['data-key']
        daUrl = '/title/tt0120762/reviews/_ajax'
        if 'data-ajaxurl' in loadMore.attrs:
          daUrl = loadMore.attrs['data-ajaxurl']
        if not daUrl.startswith('/'): 
          daUrl = daUrl + '/'

        lmUrl = rootUrl + daUrl + '?ref_=undefined&paginationKey=' + dKey
        return lmUrl 

      #else:
      print(f"! search for {lmSelector} returned {type(loadMore)} ",loadMore)
      return None


Then, you could wrap your code in a `while` loop or something like:

    #imports 
    #excel setup  
    #def getMoreRevs...
    
    reqUrl = "https://www.imdb.com/title/tt0120762/reviews?ref_=tt_urv"
    while reqUrl:
      source = requests.get(reqUrl)
      source.raise_for_status()
      soup = BeautifulSoup(source.text,'html.parser')
    
      reviews = soup.find_all('div', class_="review-container") 
      #for review in reviews ...
    
      reqUrl = getMoreRevs(soup)
    
    #excel.save...

  [1]: https://i.sstatic.net/a2vIr.png
  [2]: https://i.sstatic.net/RzU1v.png
