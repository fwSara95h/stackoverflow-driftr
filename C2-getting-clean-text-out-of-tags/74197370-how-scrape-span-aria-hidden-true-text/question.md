---
title: "how scrape - span aria-hidden=\"true\" - text"
site: stackoverflow
question_id: 74197370
url: https://stackoverflow.com/q/74197370
asked: 2022-10-25T16:30:37Z
asked_by: "LaC"
asked_by_url: https://stackoverflow.com/users/20332244
last_edited: 2022-10-25T16:31:31Z
tags: [python, web-scraping, beautifulsoup, hidden-field]
score: 0
views_at_snapshot: 1310
answer_count: 1
accepted_answer_id: 74198014
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 437d4e11809e66dc39e820b5078aab961a957045f79cf77345f929f161885260
---

# how scrape - span aria-hidden="true" - text

Asked by [LaC](https://stackoverflow.com/users/20332244) on Stack Overflow, <https://stackoverflow.com/q/74197370>, 2022-10-25, last edited 2022-10-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to web scrape using selenium and beautiful soupe but i cannot get selenium to find the element I need and return the text.

here is the html:

```
<span class="t-14 t-normal">
            <span aria-hidden="true"><!---->Crédit Agricole CIB · Full-time<!----></span><span class="visually-hidden"><!---->Crédit Agricole CIB · Full-time<!----></span>
          </span>
```
Do you know how to get the text 'Crédit Agricole CIB Full-time' from this html?




I am trying to do something like this:


```
src = driver.page_source
soup = BeautifulSoup(src, 'lxml')                                    # Now using beautiful soup
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

text_loc = intro.find( ???? )                                        # Extracting the text
text = text_loc.get_text().strip()                                   # Removing extra blank space
```

I do not know what to put in the ????

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-10-25): Can you confirm the page url?
- **[Community](https://stackoverflow.com/users/-1)** (2022-10-25): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
