---
title: "How to make BeautifulSoup go to the specific webpage I want instead of a random one on the site?"
site: stackoverflow
question_id: 74418118
answer_id: 74419123
url: https://stackoverflow.com/a/74419123
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-13T07:12:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74419123/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: eca9ebd4560686206f9f008058930d6c4c8153f3436d49680a085f5bf06da70c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74419123>, 2022-11-13; score 0. Text as retrieved 2026-10-12.

I got the same results (*"..every time I run the code it seems to jump to a new random fight..."*) when I tried your code. Like some of the comments suggested, it's probably in an effort to evade bots. Maybe the right set of headers could resolve it, but I'm not very good with making requests imitate un-automated browsers - so in situations like these, I sometimes use [`HTMLSession`](https://requests.readthedocs.io/projects/requests-html/en/latest/) (or cloudscraper or even ScrapingAnt, and finally selenium if none of the others work).
```python
# from requests_html import HTMLSession

url = 'https://www.tapology.com/fightcenter/bouts/2093-ufc-76-the-dean-of-mean-keith-jardine-vs-chuck-the-iceman-liddell'
req = HTMLSession().get(url)
soup = BeautifulSoup(req.text, 'html.parser')

fightstats = soup.find_all('td')
fightresult = soup.find_all('div', class_='boutResultHolder')
print('\n\n\n'.join('\n'.join( # remove some whitespaces from text for better readability
    ' '.join(w for w in t.text.split() if w) for t in f if t.text.strip()
) for f in [fightresult, fightstats]))
```
For me, that prints
```lang-none
Keith Jardine defeats Chuck Liddell via 3 Round Decision #30 Biggest Upset of All Time #97 Greatest Light Heavy MMA Fight of All Time


13-3-1
Pro Record At Fight
20-4-0
Climbed to 14-3
Record After Fight
Fell to 20-5
+290 (Moderate Underdog)
Betting Odds
-395 (Moderate Favorite)
United States
Nationality
United States
Albuquerque, New Mexico
Fighting out of
San Luis Obispo, California
31 years, 10 months, 3 weeks, 1 day
Age at Fight
37 years, 9 months, 5 days
204.5 lbs (92.8 kgs)
Weigh-In Result
205.5 lbs (93.2 kgs)
6'1" (186cm)
Height
6'2" (188cm)
76.0" (193cm)
Reach
76.5" (194cm)
Jackson Wink MMA
Gym
The Pit
Invicta FC 50
11.16.2022, 9:00 PM ET
Bellator 288
11.18.2022, 6:00 PM ET
ONE on Prime Video 4
11.18.2022, 7:00 PM ET
LFA 147
11.18.2022, 6:00 PM ET
ONE Championship 163
11.19.2022, 4:30 AM ET
UFC Fight Night
11.19.2022, 1:00 PM ET
Cage Warriors 147: Unplugg...
11.20.2022, 12:00 PM ET
PFL 10
11.25.2022, 5:30 PM ET
Jiří "Denisa" Procházka
Glover Teixeira
Jan Błachowicz
Magomed Ankalaev
Aleksandar "Rocket" Rakić
Anthony "Lionheart" Smith
Jamahal "Sweet Dreams" Hill
Nikita "The Miner" Krylov
```
