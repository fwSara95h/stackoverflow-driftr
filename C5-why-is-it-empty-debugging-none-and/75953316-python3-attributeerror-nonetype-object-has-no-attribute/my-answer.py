# Code from my Stack Overflow answer https://stackoverflow.com/a/75955830 (posted 2023-04-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> genre_links = genres_div.find_all('a')
>                   ^^^^^^^^^^^^^^^^^^^
> AttributeError: 'NoneType' object has no attribute 'find_all'
>

# --- block 2 ---
genre_links = [] if genres_div is None else genres_div.find_all('a') ## OR
# genre_links = genres_div.find_all('a') if genres_div else []

# --- block 3 ---
> genres_div = soup.find('div', class_='genres')
>

# --- block 4 ---
genre_links = soup.select('ul.genres a[href]') ## OR
# genre_links = soup.select('.genres a[href]') 
## '.genres a[href]' <-- any a tags inside any tag with a "genres" class

# --- block 5 ---
# genre_links = soup.select(f'a[href][title^="View all posts in "]') ## OR 

title_check = lambda t: t and t.startswith("View all posts in ")
genre_links = soup.find_all('a', href=True, title=title_check)

# --- block 6 ---
genre_links = soup.select(f'.genres a[href]')
path, text = [a['href'] for a in genre_links], [a.text for a in genre_links]
# path_text_pairs = list(zip(path, text))

# --- block 7 ---
path_text_pairs = [(a['href'], a.text) for a in soup.select('.genres a[href]')]
path, text = [list(l) for l in zip(*path_text_pairs)]

# --- block 8 ---
> path_text_pairs = [('/genres/action/', 'Action'), ('/genres/adventure/', 'Adventure'), ('/genres/comedy/', 'Comedy'), ('/genres/demons/', 'Demons'), ('/genres/drama/', 'Drama'), ('/genres/ecchi/', 'Ecchi'), ('/genres/fantasy/', 'Fantasy'), ('/genres/game/', 'Game'), ('/genres/harem/', 'Harem'), ('/genres/historical/', 'Historical'), ('/genres/horror/', 'Horror'), ('/genres/josei/', 'Josei'), ('/genres/magic/', 'Magic'), ('/genres/martial-arts/', 'Martial Arts'), ('/genres/mecha/', 'Mecha'), ('/genres/military/', 'Military'), ('/genres/music/', 'Music'), ('/genres/mystery/', 'Mystery'), ('/genres/psychological/', 'Psychological'), ('/genres/parody/', 'Parody'), ('/genres/police/', 'Police'), ('/genres/romance/', 'Romance'), ('/genres/samurai/', 'Samurai'), ('/genres/school/', 'School'), ('/genres/sci-fi/', 'Sci-Fi'), ('/genres/seinen/', 'Seinen'), ('/genres/shoujo/', 'Shoujo'), ('/genres/shoujo-ai/', 'Shoujo Ai'), ('/genres/shounen/', 'Shounen'), ('/genres/slice-of-life/', 'Slice of Life'), ('/genres/sports/', 'Sports'), ('/genres/space/', 'Space'), ('/genres/super-power/', 'Super Power'), ('/genres/supernatural/', 'Supernatural'), ('/genres/thriller/', 'Thriller'), ('/genres/vampire/', 'Vampire')]
> 
> path = ['/genres/action/', '/genres/adventure/', '/genres/comedy/', '/genres/demons/', '/genres/drama/', '/genres/ecchi/', '/genres/fantasy/', '/genres/game/', '/genres/harem/', '/genres/historical/', '/genres/horror/', '/genres/josei/', '/genres/magic/', '/genres/martial-arts/', '/genres/mecha/', '/genres/military/', '/genres/music/', '/genres/mystery/', '/genres/psychological/', '/genres/parody/', '/genres/police/', '/genres/romance/', '/genres/samurai/', '/genres/school/', '/genres/sci-fi/', '/genres/seinen/', '/genres/shoujo/', '/genres/shoujo-ai/', '/genres/shounen/', '/genres/slice-of-life/', '/genres/sports/', '/genres/space/', '/genres/super-power/', '/genres/supernatural/', '/genres/thriller/', '/genres/vampire/']
> text = ['Action', 'Adventure', 'Comedy', 'Demons', 'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Historical', 'Horror', 'Josei', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Psychological', 'Parody', 'Police', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Slice of Life', 'Sports', 'Space', 'Super Power', 'Supernatural', 'Thriller', 'Vampire'] 
>

# --- block 9 ---
import requests
from bs4 import BeautifulSoup

url = 'https://otakudesu.lol/genre-list/'
soup = BeautifulSoup((r:=requests.get(url)).content, 'html.parser')
print(f'<{r.status_code} {r.reason}> from {r.url}\n') ## for debugging

genre_links = soup.select(f'.genres a[href]')
paths, texts = [a['href'] for a in genre_links], [a.text for a in genre_links]

if not genre_links: ## for debugging [ if no results ]
    dump_fp = 'x.html'
    with open(dump_fp, 'wb') as f: f.write(soup.prettify('utf-8'))
    print(f'No genre links found - saved html to {dump_fp!r}')
else: print(f'{paths = }\n{texts = }') ## print results
