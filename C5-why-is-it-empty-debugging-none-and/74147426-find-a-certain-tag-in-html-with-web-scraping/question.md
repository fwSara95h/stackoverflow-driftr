---
title: "Find a certain tag in HTML with web scraping"
site: stackoverflow
question_id: 74147426
url: https://stackoverflow.com/q/74147426
asked: 2022-10-20T23:58:23Z
asked_by: "Giacomo Sanguin"
asked_by_url: https://stackoverflow.com/users/16165375
last_edited: never
tags: [python, html, beautifulsoup]
score: -1
views_at_snapshot: 58
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fb9cf3b4cd729ca5184c7144712b2b7f5cfcac2d7128e5d3b686aa96c5bf2406
---

# Find a certain tag in HTML with web scraping

Asked by [Giacomo Sanguin](https://stackoverflow.com/users/16165375) on Stack Overflow, <https://stackoverflow.com/q/74147426>, 2022-10-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm doing web scraping on different html pages with a for loop, and I need to find for every page a certain tag (I'm using BeautifulSoup and find_all method). But not in all the pages that tag exist. So I need to find a simple way to check if that tag exist. I've tried to write this code in order to check if the tag does not exist, but it does not work.

        ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    Input In [92], in <cell line: 5>()
         36 sal_play = salary.find_all('tr')[1:]
         37 print(sal_play)
    ---> 38 if sal_play.find_all('tr', class_='thead') is None :
         39     print('1')
         40 else:
    
    AttributeError: 'list' object has no attribute 'find'

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[αԋɱҽԃ αмєяιcαη](https://stackoverflow.com/users/7658985)** (2022-10-21): `goal = soup.select("tr.thead"); if goal: print(goal)`
- **[furas](https://stackoverflow.com/users/1832058)** (2022-10-21): first `find_all` gives you list and you have to use `for`-loop to run second `find_all` on every element separatelly.
- **[Giacomo Sanguin](https://stackoverflow.com/users/16165375)** (2022-10-21): thanks @furas, finally understood the problem! I was calling the find_all on the wrong element as you said. Anyway I've used the select method in my code since it was better readable (I'm doing a sort of thesis about web scraping). You saved my day!
