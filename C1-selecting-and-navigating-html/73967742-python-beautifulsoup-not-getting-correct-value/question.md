---
title: "Python BeautifulSoup Not Getting Correct Value"
site: stackoverflow
question_id: 73967742
url: https://stackoverflow.com/q/73967742
asked: 2022-10-06T01:10:33Z
asked_by: "kevon cambridge"
asked_by_url: https://stackoverflow.com/users/19840148
last_edited: never
tags: [python, beautifulsoup]
score: -3
views_at_snapshot: 107
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 88cd7d225387f17a8ce501a8def7b59b419fc83181a08fc0fb173a481876638e
---

# Python BeautifulSoup Not Getting Correct Value

Asked by [kevon cambridge](https://stackoverflow.com/users/19840148) on Stack Overflow, <https://stackoverflow.com/q/73967742>, 2022-10-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape movie data from https://www.imdb.com/search/title/?title_type=feature&genres=comedy&explore=genres but when I try to scrape the movie runtime text I get an error saying get_text is not callable and that is because in some of the movies that I am scraping there is no runtime. How can I make my code skip the movies with no runtime? 
```
source = requests.get('https://www.imdb.com/search/title/?title_type=feature&genres=comedy&explore=genres')
source.raise_for_status()
    
soup = BeautifulSoup(source.text, 'html.parser')
    
comedy_movies = soup.find_all('div', class_ = "lister-item mode-advanced")

for movies in comedy_movies:
    #movie title
    movie_title = movies.find('div', class_ = 'lister-item-content').a.text
    #Parental Advisory
    advisory = movies.find('span', class_ = 'certificate') #figure out how to single out advisory-
    #Movie runtime
    runtime = movies.find('span', class_ = 'runtime') #figure out how to single out runtime
    #Movie Genre
    genre = movies.find('span', class_ = 'genre').get_text()
    #Movie Rating
    rating = movies.find('span', class_ = 'global-sprite rating-star imdb-rating') #Figure out how to single out ratings
    #MetaScore
    metascore = movies.find('div', class_ = 'inline-block ratings-metascore') #.span.text same here missing values
    #Movie Description
    description = movies.find('div', class_ = 'lister-item-content').p.text
    print(runtime)
```
Also when I try to scrape the descriptions. I am not getting the descriptions, I am getting another text with the same <p> and class. How can I fix these? I will appreciate it a lot if someone can help.[my code executed with runtime showing the None values][1]


  [1]: https://i.sstatic.net/QxWP3.png
