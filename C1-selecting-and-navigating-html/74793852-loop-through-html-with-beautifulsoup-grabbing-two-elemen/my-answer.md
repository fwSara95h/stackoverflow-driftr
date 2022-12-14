---
title: "Loop through html with beautifulsoup grabbing two elements from each <hr> tag then move on to the next and do the same"
site: stackoverflow
question_id: 74793852
answer_id: 74799439
url: https://stackoverflow.com/a/74799439
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-14T14:02:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74799439/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5b4b5c6eca31577714a8797d8be7cadfebbc02b6310fbb26f0ac74d4221d5f72
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74799439>, 2022-12-14; score 1. Text as retrieved 2026-10-12.

> How do I loop through the entire html page grabbing the same info ***from*** each `<hr>`?

Actually, `hr` tag is for displaying a horizontal line across a page (like you might see below this, and probably several more times in my answer), so there isn't anything *in* it that you can get *from* it. 

---

What you seem to want is the some content that comes from the `li` tag *after* each `<hr>`.

> It would also be nice to know why it is repeating

That's because you're doing the same thing every loop - `soup` was defined outside the loop, and it's not changed again, and it refers to the whole document, so ofc `soup.find("li")...` is not a thing that will differ in the next loop.

The thing that changes is **`hr`** [from `for hr in hrs`], so that's what you need to use for new content. However, there is no use applying `.find(...)` to `hr` since, like I explained, there's nothing *in* it; but you *can* use [`.find_next(...)`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all-next-and-find-next) instead:

```python 
    for hr in soup.find_all('hr'):
        title = hr.find_next("li").b.text
        text = hr.find_next("li").contents[-1].strip(" .\n")
```

---

But it's rather redundant to call `.find_next("li")` twice; and also, if there are two `hr` tags with no `li` tags between them, then the `li` from before the first (of those 2 `hr`s) will be repeated. So, it's better to first get the next-`li` tags and then get [eliminate repetition](https://www.programiz.com/python-programming/set) before extracting `title` and `text`.

```python
    liList = [li for li in set([
        hr.find_next("li") for hr in soup.select('hr')
    ]) if li.b] # remove risk of error when getting title
    for li in liList:
        title = li.b.text
        text = li.contents[-1].strip(" .\n")
```

(You can use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) like `liList = soup.select('hr ~ * li:has(b)')`, but that will have another issue - if there are multiple `li` tags between two `hr` tags. [But if you *want* all of the `li` tags, not just one after each `hr`, then this is useful.])

---

Now, the possibility of error at `title = li.b.text` if an `li` does not have any `b` tags has been avoided, but there is still an issue with *`li.contents[-1].strip(" .\n")`* - it assumes that the last content of the li tag will be a string, but even in your sample HTML snippet, after the 3r `hr`, the `li` ends with a `p` tag, so you will get an error there. You can get the last string content of every `li` with

```python
        text = [t for t in li.contents if isinstance(t, str)]
        text = (text[-1] if text else '').strip(" .")
```

or you can get the text from the last content [full code this time]

```python
soup = BeautifulSoup(page.content, "html.parser")

with open("test1.txt", "w") as file:
    liList = [li for li in set([
        hr.find_next("li") for hr in soup.select('hr')
    ]) if li.b] # remove risk of error when getting title
    for li in liList:
        title = li.b.text
        text = [getattr(
            c, 'text', c if isinstance(c, str) else ''
        ) for c in li.contents]
        text = (text[-1] if text else '').strip(" .")
        file.write("Today in #Space #History- "+title+" "+text.strip()+"\n")
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[qLu](https://stackoverflow.com/users/3923696)** (2022-12-14): My goodness. Thank you so much for correcting my thinking here. It was an aha moment, I'd totally donate to your patreon.
- **me** (2022-12-14): @qLu now I wish I had a patreon haha...glad it helped!
