---
title: "How to extract the data in between 2 header tags?"
site: stackoverflow
question_id: 75256667
answer_id: 75272195
url: https://stackoverflow.com/a/75272195
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-29T02:07:10Z
last_edited: 2023-01-29T02:13:28Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75272195/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1b145c678e27ac00221e20d45bbf99d4da406c841e22c2a1a9f1028471ead24d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75272195>, 2023-01-29, last edited 2023-01-29; **accepted**; score 0. Text as retrieved 2026-10-12.

This won't work if the `h_` tags don't share a direct [parent](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parent) , but you could try looping through [sibling](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling) tags after each `h_` tag [and stop if the next `h_` tag is reached].

```python
# url = 'https://en.wikipedia.org/wiki/Chris_Yonge' [ for example ]
# soup = BeautifulSoup(requests.get(url).content)

# item_header = soup.find_all(re.compile('^h[1-6]')) # should be same as
item_header = soup.find_all([f'h{i}' for i in range(1,7)])

skipTags = ['script', 'style'] # any tags you don't want text from
hSections = []

for h in item_header:
    sectionLines = []

    for ns in  h.find_next_siblings():
        if ns in item_header: break # stop if/when next header is reached
        if ns.name in skipTags: continue # skip certain tags

        sectionLines.append(' '.join(ns.get_text(' ').split())) 
        # [ split+join to minimize whitespace ] 

    hSections.append({
        'header_type': h.name, 'header_text': h.get_text(' ').strip(),
        'section_text': '\n'.join([l for l in sectionLines if l])
    })    
```

---

I couldn't test this properly since you didn't include any html snippet nor a link to the site you want to scrape, but when tried on a Wikipedia page, `hSections` (after truncating and tabulating) looks like: [![sampop][1]][1]

<sub>You can also take a look at [this solution](https://stackoverflow.com/a/75263236/6146136) if you're interested in nesting subsection into the parent sections.</sub>




  [1]: https://i.sstatic.net/LfuMm.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Akshay Toranagatti](https://stackoverflow.com/users/20786649)** (2023-01-30): Got it! I could modify this as per my requirement.  Thank you :)
