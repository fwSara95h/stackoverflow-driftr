---
title: "Python BeautifulSoup Not Getting Correct Value"
site: stackoverflow
question_id: 73967742
answer_id: 74118940
url: https://stackoverflow.com/a/74118940
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-19T01:22:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74118940/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a10a0f60950f661201c500e9945046d50390d8e365fbebf6e5882a8bf11bb62
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74118940>, 2022-10-19; score 0. Text as retrieved 2026-10-12.

To avoid the error you can simply first check wheteher `find` returned anything that [is not None](https://bobbyhadz.com/blog/python-check-if-not-none), like 
```python 
runtime = movies.find('span', class_ = 'runtime')
if runtime is not None:
    runtime = runtime.text
```

As for ratings, you want the contents of the `<strong>` tag *next* to the `span` you were finding:
```python
rating = movies.find(
    'span', class_ = 'global-sprite rating-star imdb-rating'
).find_next('strong').text
```
and for description, you would need to look for the `p` tag with `class="text-muted"` *after* the `div` with `class="ratings-bar"`:
```python
rating = movies.find(
    'div', class_ = 'ratings-bar'
).find_next('p', class_ = 'text-muted').text
```
although this will `find` None [and then raise error] when ratings is missing...

<br>

You might have noticed by now that some data (description, rating, metascore and title) would need more than one `if...is not None` checks to avoid getting errors if  anything returns `None`, so it might be preferable [especially with nested elements] to [`select_one`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) instead. (If you are unfamiliar with css selectors, [check this for reference](https://www.w3schools.com/cssref/css_selectors.asp).) 

Then, you would be able to get metascore as simply as:
```python
metascore = movies.select_one('div.inline-block.ratings-metascore span')
if metascore is not None:
    metascore = metascore.get_text()
```

In fact, you could define a dictionary with a selector for each piece of information you need and restructure your for-loop to something like
```python
selectorDict = {
    'movie_title': 'div.lister-item-content a', 
    'advisory': 'span.certificate',
    'runtime': 'span.runtime',
    'genre': 'span.genre',
    'rating': 'span.global-sprite.rating-star.imdb-rating~strong',
    'metascore': 'div.inline-block.ratings-metascore span',
    'description': 'div.lister-item-content p~p'
    #'description': 'div.ratings-bar~p.text-muted' 
    # ^--misses description when rating is missing
}

movieData = []
for movie in comedy_movies:
    mData = {}
    for k in selectorDict:
        dTag = movie.select_one(selectorDict[k])
        if dTag is not None:
            mData[k] = dTag.get_text(strip=True)
        else: mData[k] = None # OPTIONAL
    movieData.append(mData)
```

with this, you could easily explore the collected data at once; for example, as a pandas dataframe with
```python
# import pandas
pandas.DataFrame(movieData)
```
[As you might notice in the output below, some cells are blank (because value=`None`), but no errors would have been raised while the for-loop is running because of it.]

|index|movie\_title|advisory|runtime|genre|rating|metascore|description|
|---|---|---|---|---|---|---|---|
|0|Amsterdam|R|134 min|Comedy, Drama, History|6\.2|48|In the 1930s, three friends witness a murder, are framed for it, and uncover one of the most outrageous plots in American history\.|
|1|Hocus Pocus 2|PG|103 min|Comedy, Family, Fantasy|6\.1|55|Two young women accidentally bring back the Sanderson Sisters to modern day Salem and must figure out how to stop the child-hungry witches from wreaking havoc on the world\.|
|2|Hocus Pocus|PG|96 min|Comedy, Family, Fantasy|6\.9|43|A teenage boy named Max and his little sister move to Salem, where he struggles to fit in before awakening a trio of diabolical witches that were executed in the 17th century\.|
|3|The Super Mario Bros\. Movie|||Animation, Adventure, Comedy|||A plumber named Mario travels through an underground labyrinth with his brother, Luigi, trying to save a captured princess\. Feature film adaptation of the popular video game\.|
|4|Bullet Train|R|127 min|Action, Comedy, Thriller|7\.4|49|Five assassins aboard a swiftly-moving bullet train to find out that their missions have something in common\.|
|5|Spirited|PG-13|127 min|Comedy, Family, Musical|||A musical version of Charles Dickens's story of a miserly misanthrope who is taken on a magical journey\.|
|---|---|---|---|---|---|---|---|
|47|Scooby-Doo|PG|86 min|Adventure, Comedy, Family|5\.2|35|After an acrimonious break up, the Mystery Inc\. gang are individually brought to an island resort to investigate strange goings on\.|
|48|Casper|PG|100 min|Comedy, Family, Fantasy|6\.1|49|An afterlife therapist and his daughter meet a friendly young ghost when they move into a crumbling mansion in order to rid the premises of wicked spirits\.|
|49|Ghostbusters|PG|105 min|Action, Comedy, Fantasy|7\.8|71|Three parapsychologists forced out of their university funding set up shop as a unique ghost removal service in New York City, attracting frightened yet skeptical customers\.|
