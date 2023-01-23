---
title: "Get full text below h2 tag with BeautifulSoup"
site: stackoverflow
question_id: 75204624
answer_id: 75204878
url: https://stackoverflow.com/a/75204878
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2023-01-23T00:32:42Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2381d168dd9df6b807b984e51a466ca1b20c34cfc6ab18908b96df86db83b9af
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2023-01-23

Posted on Stack Overflow, <https://stackoverflow.com/a/75204878>, 2023-01-23; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can search *backwards* for previous `<h2>` and store result in the dictionary:

```py
from bs4 import BeautifulSoup


html_doc = '''\
<h2><span class="mw-headline" id="Apariencia">Apariencia</span></h2>
<figure class="thumb tleft " style="width: 100px">
<p>T1 ...</p>
<p>T2 ...</p>
<p>T3 ...</p>
<h2><span class="mw-headline" id="Personalidad">Personalidad</span></h2>
<p>T4 ...</p>
<p>T5 ...</p>
<p>T6 ...</p>'''

soup = BeautifulSoup(html_doc, 'html.parser')

out = {}
for p in soup.select('p'):
    previous_h2 = p.find_previous('h2')
    out.setdefault(previous_h2.text, []).append(p.text)

print(out)
```

Prints:

```
{
    'Apariencia': ['T1 ...', 'T2 ...', 'T3 ...'], 
    'Personalidad': ['T4 ...', 'T5 ...', 'T6 ...']
}
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Iván Grzegorczyk](https://stackoverflow.com/users/21062528)** (2023-01-23): I had to make a little modification but it worked :) Thank you very much!
