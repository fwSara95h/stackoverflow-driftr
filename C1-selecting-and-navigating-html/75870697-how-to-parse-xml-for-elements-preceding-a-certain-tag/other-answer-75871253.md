---
title: "How to parse XML for elements preceding a certain tag?"
site: stackoverflow
question_id: 75870697
answer_id: 75871253
url: https://stackoverflow.com/a/75871253
author: "Saxtheowl"
author_url: https://stackoverflow.com/users/1616622
posted: 2023-03-28T21:32:53Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 62f29602689dffd01e8c64c4e8606bbba6920b0c52429a25ce5c6da151e001e3
role: another answer on the same question, kept as context; not my work
---

# Answer by [Saxtheowl](https://stackoverflow.com/users/1616622) — 2023-03-28

Posted on Stack Overflow, <https://stackoverflow.com/a/75871253>, 2023-03-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You should use the find_all method of beautifulsoup for the <xref> then do a loop through each tags, like that:

    from bs4 import BeautifulSoup
    
    xml = '...' # Your XML input
    
    soup = BeautifulSoup(xml, 'html.parser')
    
    citations = soup.find_all('xref', {'ref-type': 'bibr'})
    
    for citation in citations:
        previous_element = citation.previous_element
        if previous_element:
            sentence = previous_element.strip()
            citation_text = citation.text.strip()
            print(f"{sentence} : ({citation_text})")
