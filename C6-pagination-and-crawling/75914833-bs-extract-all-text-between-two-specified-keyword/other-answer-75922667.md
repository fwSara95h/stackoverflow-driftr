---
title: "BS Extract all text between two specified keyword"
site: stackoverflow
question_id: 75914833
answer_id: 75922667
url: https://stackoverflow.com/a/75922667
author: "Atbjbiye"
author_url: https://stackoverflow.com/users/21552291
posted: 2023-04-03T18:30:07Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 873f62412844e21dbad1722baf221a680eec946a617d506c16183305e7b8f20b
role: another answer on the same question, kept as context; not my work
---

# Answer by [Atbjbiye](https://stackoverflow.com/users/21552291) — 2023-04-03

Posted on Stack Overflow, <https://stackoverflow.com/a/75922667>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Maybe you can try to convert the lines of text into one string. I am thinking that the type of your text is actually a list and not a string. 

    print(type(text)) to find the type of your text

If it's a list then:

    list = ["Adresse : fffgdfdgfrrrere",
    "rrgegreggregr",
    "Téléphone : egrrgerererg"]
    
    text = ' '.join(list)
    print(text)

Then: 

    text = "Adresse: fffgdfdgfrrrere rrgegreggregr Téléphone: egrrgerererg"
    def get_textchunk(word1, word2, text):
                new_text = text.split(word1)
                new_text = new_text[1]
                newnew_text = new_text.split(word2)
                return newnew_text
    print(get_textchunk('Adresse: ',' Téléphone', text)[0])

Answer: "fffgdfdgfrrrere rrgegreggregr"
