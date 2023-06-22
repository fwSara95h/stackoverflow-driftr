---
title: "how to extract the texts after the first h1 Tag?"
site: stackoverflow
question_id: 76530572
answer_id: 76532532
url: https://stackoverflow.com/a/76532532
author: "CupOfTea"
author_url: https://stackoverflow.com/users/22114870
posted: 2023-06-22T13:39:22Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ea6a2e1bfd1351e8c123789cb95a833b06b34d5b19d6308b2cd543406885b59c
role: another answer on the same question, kept as context; not my work
---

# Answer by [CupOfTea](https://stackoverflow.com/users/22114870) — 2023-06-22

Posted on Stack Overflow, <https://stackoverflow.com/a/76532532>, 2023-06-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Maybe BeautifulSoup parser would be helpful here.
https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/

    `response = requests.get('https://economictimes.indiatimes.com/news/international/business/volkswagen-sets-5-7-revenue-growth-target-preaches-cost-discipline/articleshow/101168014.cms', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup = BeautifulSoup(response.content, 'html.parser')
    
    h1_tags = soup.body.find_all('h1')
    if len(h1_tags) > 1:
        for sibling in h1_tags[0].next_siblings:
            if sibling.name == 'p':
                text_after_h1 = sibling.get_text(strip=True)
                break
    
    print(text_after_h1)`

**"soup.body.find_all('h1')"**  - This will find all the "<h1>" elements within the "<body>"
-we iterate through their next siblings until we find a "<p" tag (assuming that the p tag is the text).
**get_text()**  - will grab the text under the p tag. ** strip=True** - removes any leading or whitespace.

Had a simillar issue once.
Hope that this helps
