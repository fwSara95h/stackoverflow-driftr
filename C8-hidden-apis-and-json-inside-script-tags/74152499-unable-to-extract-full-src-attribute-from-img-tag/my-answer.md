---
title: "Unable to extract full src attribute from img tag"
site: stackoverflow
question_id: 74152499
answer_id: 74152500
url: https://stackoverflow.com/a/74152500
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-21T10:46:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74152500/revisions
accepted: true
score: 1
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cd00ec707101df31f8117e5ffa29f914c8334f5368bb23016700dc7c775d028d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74152500>, 2022-10-21; **accepted**; score 1. Text as retrieved 2026-10-12.

I figured it out as I was writing in the question about inspecting the saved html file - I only used devtools and didn't open and see all the saved html code itself.

When I open the html on vscode, there are actually *two* occurrences of the id `dimg_179` - the one in the img tag itself, and another in a `script` tag:

```html
<script nonce="w8n56Ul9BxlnjUkznIswGw">(function(){var s='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEIAdwMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwAEBQYBB//EADYQAAEDAgQDBQYFBQEAAAAAAAEAAgMEEQUhMUESUZETUmFxgQYiQmKh8COxwdHhFTIzNJIH/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAIBA//EABsRAQEBAQEBAQEAAAAAAAAAAAABESECURJB/9oADAMBAAIRAxEAPwDouIX2CfG830BQcR7xPqUbX2XJ0WGuPdTWvdySA8b26J0ZaeXQIHCR1rL0PduChbwd1vRGCwbNWseXdffovRI7fL0VukopqrOOMBnfcLD+Vr0uF08BDngSyDdwyHkFsiWRSUFVVWLBwRn43D8ua0n4XBHTObm+UjJ7jofJaZcEqTNVkNcbKXNu1wIINkk6rVxmAxTdq2/C/J1uazSeL4iud4qFkHnZecJ5jqjJHNASPsLNUAhyiIlu9v8AlRNFFvu/ynMft+iSHHl9U1hvshphva7dR9U2CUP1Nj5oGE8h0Ks4bLQsxAQ1kd3vbxRXyaba5dOq2dZbFujpaipP4LPd77tAtykwuCGzprSyeIs0eiY2dvCAywbsAj7RdJ5xNqzxC1gvC5I7Rc37Q+3GEYBilJh9bUNM9Q5rOzY4F7C5wDS4GwDcySSdt7qkuqLkBcldpfdCXoE18LaiBzDuMvNcjVSmE2e03vYm+i7F7lzWPUo7YS/C/J3mo9+dX5uKTi5wBubbZoT5nqlnJoAfpzQEnvBRjdh+R1Jt5qKvxHmOiiz81v6JDj8qYxzuTeiQ1/ypzXju/Vaw9rjy+iTiMMktMHw/7ELu0jtzG3roj4/l+qJsmoLL+qdZxuYFibK6ijladRmOS12y5L5/h9V/TcZfDm2nqbvjF8g74h+vquwhqOJuq66lpiRcV7Yf+c4V7VYxDiVTPPTyNAZOIbfjNGmuh2vnlsun7a268NRbdA7D6eDDsPpqGlBbBTRNijBNyGtFhn6JjpgFnTVzWDN1lj4hj0UDbukAubDxPIcz4Jo6CasazUrIxXGKVkRZO4DjyaBm5x8BqT5LDNVX1xu0Opoe+9t3nyboPM9E2np6emcXtjc+UizpZDxPPry8NFN9fG4dxv4QS21x0S3PN9E0vadWBKcWnRqiNLMmai8e0P8AhsvVRDI6aZzQ5sUjgdCGnNQsLHcLg5pGoI0VqHtDAHguDGtYCBfMEi6r1cv451vwt/u1/tGq5dVxGWumBv3ZIEiMSD7C3pxWxagNVSHsSBPGe0iPzD99PVOwPFxU0rHOycBZzTqCrDZABt0XJ41N/RMRNQz/AAVRvYaCTceuvVdPN+osdrJiLWDNyya32hjjyDs72HiVhUlPieLEPkcaSnPxSNPER4N/ey6DD8NoMO/EYOObQzSZu/j0sl9EimxuKYj71jTRH4pB7xHg3b16K9S4ZBTO7QNL5iLGWTNx9dh4CwV4TNcAWkEHdeOf4KdqshThmlSOa21y65NhZNcSdMkpznN0sm0xOEnn6oSzxUdI7x6JbpHX3KdOCLAN/wA1EPEfsKJ04COonZ7rZpGgaAPOS94nPPE9xc46km5Xiin+BjQOSJRRIGRbIyootBtJsUJztfPNeKLQSiiiAXIFFFlCyTdeO0CiiADqoootH//Z';var i=['dimg_179'];_setImagesSrc(i,s);})();</script>
```

so I *can* extract it with a bit of extra effort:
```python
dimgTags = soup.find_all(lambda l: 'dimg_179' in str(l))

# get rid of parent tags
dimgTags = [d for d in dimgTags if not [t for t in dimgTags if d in t.parents]]
dimgTags = [d for d in dimgTags if d.name != 'img']

if dimgTags:
    dimgSrc = str(dimgTags[0]).split("var s='")[1].split("'")[0]
    display(HTML(f'<img src="{dimgSrc}">'))
```

<br>

I'd still love to know if there are better ways though!
