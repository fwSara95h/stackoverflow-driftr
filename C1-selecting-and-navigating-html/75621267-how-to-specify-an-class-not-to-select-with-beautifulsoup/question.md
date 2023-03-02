---
title: "How to specify an class NOT to select with BeautifulSoup 4"
site: stackoverflow
question_id: 75621267
url: https://stackoverflow.com/q/75621267
asked: 2023-03-02T22:06:23Z
asked_by: "MrPigsWorth"
asked_by_url: https://stackoverflow.com/users/20717275
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 389
answer_count: 1
accepted_answer_id: 75643095
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e61f9edb73c9e2dbd0f17fc2398cb52b6d25e6f1b4ec059102ab4759ded4b55b
---

# How to specify an class NOT to select with BeautifulSoup 4

Asked by [MrPigsWorth](https://stackoverflow.com/users/20717275) on Stack Overflow, <https://stackoverflow.com/q/75621267>, 2023-03-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am currently working on a web-scraping project that extracts links out of an article and I want to be able to specify the search to just the main body of text, but am running into trouble with false-positives on the navigational links at the bottom. 

I know that all of these false positives fall under the same specific class in the html, but I don't know how to specify *not* to search there.


This is the code I currently have and I want to specify not to search descendants of class="footer-wikiwalk-nav"

```
        url = searchlinks.get()
        c = requests.get(url)
        bs = BeautifulSoup(c.content, 'lxml')

        parent_url = 'https://EXAMPLEURL.com'
        surfacelinks = [parent_url + str(l) for l, t in list(set([(a.get('href'), 
                    a.get_text()) for a in bs.select('[href*="str"]')])) 
                    if 'STR' in t]
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-03-02): Use `:not(.footer-wikiwalk-nav)` in the selector.
- **[hc_dev](https://stackoverflow.com/users/5730279)** (2023-03-06): Most of the SCP Wiki pages with their [source-text can be found on GitHub: extracted with _wikidot-css-extractor_](https://emmiegit.github.io/wikidot-css-extractor/).
