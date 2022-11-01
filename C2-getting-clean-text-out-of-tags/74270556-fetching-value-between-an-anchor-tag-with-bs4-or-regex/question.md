---
title: "fetching value between an anchor tag with bs4 or regex"
site: stackoverflow
question_id: 74270556
url: https://stackoverflow.com/q/74270556
asked: 2022-11-01T01:16:34Z
asked_by: "ili"
asked_by_url: https://stackoverflow.com/users/15970133
last_edited: never
tags: [python, beautifulsoup]
score: -1
views_at_snapshot: 33
answer_count: 1
accepted_answer_id: 74270713
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a141d074652703fc23032844b15f11151597f5cf50ec8f8885215dd217088442
---

# fetching value between an anchor tag with bs4 or regex

Asked by [ili](https://stackoverflow.com/users/15970133) on Stack Overflow, <https://stackoverflow.com/q/74270556>, 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

is there a way to get the value between the anchor tags? so in this case 'Bjelica, Nemanja' using beautiful soup?

     <a href="/wiki/Nemanja_Bjelica" title="Nemanja Bjelica">Bjelica, Nemanja</a>

I tried to do it like this

    name = k.find('a')['title']

but i want to get the name between the anchor tags. Any hints?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[beepbeep-boop](https://stackoverflow.com/users/12612293)** (2022-11-01): IIRC use the `text` variable attached to it, eg: `soup.find('a').text`
- **[ili](https://stackoverflow.com/users/15970133)** (2022-11-01): no way... i literally spent hours trying to format the titles i got. Thank mate, much love
