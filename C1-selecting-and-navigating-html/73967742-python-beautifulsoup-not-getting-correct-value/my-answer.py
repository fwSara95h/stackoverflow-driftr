# Code from my Stack Overflow answer https://stackoverflow.com/a/74118940 (posted 2022-10-19), extracted verbatim; may need the question's context to run.

# --- block 1 ---
runtime = movies.find('span', class_ = 'runtime')
if runtime is not None:
    runtime = runtime.text

# --- block 2 ---
rating = movies.find(
    'span', class_ = 'global-sprite rating-star imdb-rating'
).find_next('strong').text

# --- block 3 ---
rating = movies.find(
    'div', class_ = 'ratings-bar'
).find_next('p', class_ = 'text-muted').text

# --- block 4 ---
metascore = movies.select_one('div.inline-block.ratings-metascore span')
if metascore is not None:
    metascore = metascore.get_text()

# --- block 5 ---
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

# --- block 6 ---
# import pandas
pandas.DataFrame(movieData)
