---
title: "Python Web scraper for Stackoverflow"
site: stackoverflow
question_id: 74129800
answer_id: 74133843
url: https://stackoverflow.com/a/74133843
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-20T02:35:59Z
last_edited: 2022-10-20T02:49:32Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74133843/revisions
accepted: false
score: -1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b10b21b54dd134ab5af94a4d9502ca1025e3aaf03190bf6380674e5577eb422e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74133843>, 2022-10-20, last edited 2022-10-20; score -1. Text as retrieved 2026-10-12.

The correct way to `select` elements with those two classes is:

```python
questions = soup.select('.s-post-summary.js-post-summary')
```
which will select *any* element that has these two classes, or 
```python
questions = soup.select('*[class="js-post-summary s-post-summary"]')
```
which will select only elements that have these two classes - but *only* these two classes, and they would have to be arranged in that order as well.

<hr>

**However**, as pointed out in another answer, the questions also have a `data-post-type-id` attribute [`=1`], and that is likely a much better identifier. You can specify that as well with select:
```python
questions = soup.select('*[data-post-type-id="1"]')
```

<br>

You can actually even target the `id` attribute by using
```python
questions = soup.select('*[id^="question-summary-"]')
```
to select all elements with `id` that starts with `question-summary-`

<hr>

...and since I've already gone this far, if you just want the question titles, you can just directly use a single select statement:
```python
for qLink in soup.select('*[data-post-type-id="1"] a.s-link'):
    print(qLink.get_text())
```

<hr><hr>

And about the two warning messages, I really don't think you need to worry much about them - you can just ignore them; but if they're bothering you, you might want to take a look at [this thread](https://forum.codewithmosh.com/t/hi-im-a-beginner-to-python-as-im-running-my-program-it-works-perfectly-but-i-can-see-a-message-in-problem-saying-that-missing-module-docstring-pylint-missing-module-docstring-can-someone-help-me-to-fix-this-bug/8278) which mentions some ways to either appease or disable the second warning. And for the first warning, you can either disable it similarly or just pass some [timeout](https://datagy.io/python-requests-timeouts/) argument to your request like 
```python
response = requests.get("https://stackoverflow.com/questions", timeout=5)
```
which will raise a `TimeoutError` if the request takes longer than 5sec.
