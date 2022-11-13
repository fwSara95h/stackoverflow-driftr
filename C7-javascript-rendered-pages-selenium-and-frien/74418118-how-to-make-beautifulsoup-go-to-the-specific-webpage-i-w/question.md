---
title: "How to make BeautifulSoup go to the specific webpage I want instead of a random one on the site?"
site: stackoverflow
question_id: 74418118
url: https://stackoverflow.com/q/74418118
asked: 2022-11-13T02:45:40Z
asked_by: "Skipper1504"
asked_by_url: https://stackoverflow.com/users/20489832
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 116
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 97a3f81dfc00c17b5d268eda32253ed8f6c218c7a64a5d7fdd2927a8bb56cca4
---

# How to make BeautifulSoup go to the specific webpage I want instead of a random one on the site?

Asked by [Skipper1504](https://stackoverflow.com/users/20489832) on Stack Overflow, <https://stackoverflow.com/q/74418118>, 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to learn web scraping using BeautifulSoup by scraping UFC fight data off of the website Tapology. I have entered in the URL of a specific fight's webpage but every time I run the code it seems to jump to a new random fight on the page instead of this fight. Here is the code:
```
from bs4 import BeautifulSoup
import requests

url = 'https://www.tapology.com/fightcenter/bouts/2093-ufc-76-the-dean-of-mean-keith-jardine-vs-chuck-the-iceman-liddell'
html_text = requests.get(url, timeout=5).text
soup = BeautifulSoup(html_text, 'html.parser')

fightstats = soup.find_all('td')
fightresult = soup.find_all('div', class_='boutResultHolder')
print(fightresult, fightstats)
```


Honestly I have no idea how it could be switching to other webpages when I have a very specific URL like the one I am using.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ScottC](https://stackoverflow.com/users/20174226)** (2022-11-13): I just ran your code - and for me it seemed to navigate to the correct page. What happens when you navigate to that page using a browser? Any issues ?
- **[Parham Alvani](https://stackoverflow.com/users/4242097)** (2022-11-13): Can you please share your invalid results? I think maybe the websites bans you for many requests.
- **[ScottC](https://stackoverflow.com/users/20174226)** (2022-11-13): They are probably protecting their information. Based on their privacy policy : `We automatically collect certain information, including information pertaining to your IP address, browser type, browser language, operating system, computer type (including mobile device type), access time and duration, landing page, and the pages you accessed during your visit, as well as any web pages and URLs you utilized to arrive on or depart from the Site. We collect and store this information when you use the Site, even if you have not created an account on the Site.`
- **[Skipper1504](https://stackoverflow.com/users/20489832)** (2022-11-13): @ParhamAlvani Printing the fightresult variable I can see that it is scraping pages for fights other than the one I am trying to scrape. Some of them are as follows: Timi Ogundipe defeats Angel Pacheco via 3 Round Decision, Dan Christison defeats Brad Imes via Submission at 3:37 of Round 3, and Oscar Delgado defeats Joe Johnson via KO/TKO at 1:35 of Round 1
- **[Skipper1504](https://stackoverflow.com/users/20489832)** (2022-11-13): @ScottC When I put in the URL in a browser it goes to the right page every time. When I run the code it seems to go to a random fights webpage. If it is the case that they are banning me from scraping the page I want, is there any way to get around this or do some websites just not allow webscraping?
- **[ScottC](https://stackoverflow.com/users/20174226)** (2022-11-13): you could perhaps use or implement proxies
