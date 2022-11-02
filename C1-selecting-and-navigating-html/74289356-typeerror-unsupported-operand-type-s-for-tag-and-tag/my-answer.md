---
title: "TypeError: unsupported operand type(s) for +=: 'Tag' and 'Tag'"
site: stackoverflow
question_id: 74289356
answer_id: 74292566
url: https://stackoverflow.com/a/74292566
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-02T16:25:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74292566/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3e247e4dd15379168c82eeff0ed7913f8e1b9113b2f4eefa31fea29c08d8a168
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74292566>, 2022-11-02; score 0. Text as retrieved 2026-10-12.

(I **strongly** recommend [reading the docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#append) a bit.)
I think what you're looking for is `.append` 

```python
meaning.append(css)
```
should do what you're wanting to.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ArshiyaZandi](https://stackoverflow.com/users/14927169)** (2022-11-04): Ah yes, that appended the CSS to HTML, but the CSS didn't work which I think is because of the way Beautifulsoup works.  Anyway thanks a lot for your answer, it definitely helped.
- **[Konrad Rudolph](https://stackoverflow.com/users/1968)** (2022-11-04): @ArshiyaZandi What do you mean by "CSS didn't work"? How are you processing the result of your code? Are you writing it to a new HTML file and attempting to open that in a browser?
- **[ArshiyaZandi](https://stackoverflow.com/users/14927169)** (2022-11-04): No, I actually thought CSS can work in tkinter's label widget, but it seems it doesn't. so I actually have to style the widget itself which is proving to be a hard thing to do with the content I have. If you have any tips let me know, anything will be appreciated.  Thanks a lot.
