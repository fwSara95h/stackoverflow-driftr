---
title: "How to get data from a combobox using Beautifulsoup and Python?"
site: stackoverflow
question_id: 73979130
answer_id: 73980579
url: https://stackoverflow.com/a/73980579
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-06T22:21:53Z
last_edited: 2022-10-06T23:16:21Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73980579/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a819a8692dc2f9a148762881fc6e057d6ee48721b973352ebdf8dc2427d13aa
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73980579>, 2022-10-06, last edited 2022-10-06; **accepted**; score 0. Text as retrieved 2026-10-12.

From what I can see of the html, there is no `span` with `id="sexo- 
button"`, so `BeautifulSoup(login_request.text, 'lxml').find("span",id="sexo- 
button")` would have returned `None`, which is why you got the error from `get_text`.

As for your second attempt, I don't think bs4 Tags have a `value` property,  which is why you'd be getting `None` that time.

You should actually try combining the two like:

```python
sexo = BeautifulSoup(login_request.text, 'lxml').select_one('select[name=sexo] option[selected]').get_text(strip=True)
```

(If it doesn't work, you should individually print to  see what `...select_one('select[name=sexo]')` and `...select_one('select[name=sexo] option[selected]')` will return, in case the page itself wasn't loaded properly by `session`)

You should also note that with the combined code, you'll actually get `[SELECCIONAR]`, since that's also selected according to the html provided. To skip that, you can instead try:

```python
selectedOpts = BeautifulSoup(login_request.text, 'lxml').select('select[name=sexo] option[selected]')
selectedOpts = [s for s in selectedOpts if s.get('value')]
sexo = selectedOpts[0] if selectedOpts else None
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[AjaxPain](https://stackoverflow.com/users/20092462)** (2022-10-07): I used the code to skip the [SELECT], but when printing it throws me the whole line of code >>>>: <option selected="" value="M">Masculino</option> how can i get only the text "Masculino"? Sorry bro, Im newbie
- **[AjaxPain](https://stackoverflow.com/users/20092462)** (2022-10-07): I only add ".get_text(strip=True)" in the last line of code, Thanks Bro!!!!!
