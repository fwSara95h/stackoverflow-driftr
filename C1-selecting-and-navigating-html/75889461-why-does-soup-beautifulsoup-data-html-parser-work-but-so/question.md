---
title: "Why does soup=BeautifulSoup(data, \"html.parser\") work but soup2=... does not?"
site: stackoverflow
question_id: 75889461
url: https://stackoverflow.com/q/75889461
asked: 2023-03-30T14:24:24Z
asked_by: "henri.haiti"
asked_by_url: https://stackoverflow.com/users/21406103
last_edited: never
tags: [python, beautifulsoup, xbrl]
score: 0
views_at_snapshot: 368
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 79f70531f90d7761bbf580beb74d9e3587fdddfd49c69885490ee388ae3704b7
---

# Why does soup=BeautifulSoup(data, "html.parser") work but soup2=... does not?

Asked by [henri.haiti](https://stackoverflow.com/users/21406103) on Stack Overflow, <https://stackoverflow.com/q/75889461>, 2023-03-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm a Python beginner, hope my question is not too lenghty, please tell me if I should be more concise for future questions, thank you!

I'm opening a .XHTML file which contains financial data as XML (iXBRL standard). Right now I'm parsing the file with BeautifulSoup4 ("html.parser").
 
```
url = r"tk2021.xhtml"
data = open(url, encoding="utf8")

soup = BeautifulSoup(data, "html.parser")
```

Then I'm creating different lists, which contain all matching tags. I'm using those lists later to iterate and pull out all relevant data from each tag and load it in a pd.DataFrame

```
ix_nonfraction = soup.find_all({"ix:nonfraction"})
xbrli_unit = soup.find_all({"xbrli:unit"})
```

This works as expected. What I'm struggling with is the next step.

I'm trying to create another list containing all `<xbrli:context>` tags. They have `<xbrli:entity>` child-tags, which I need to remove before I create the list. This is how I'm doing that:

```
for tag in soup("xbrli:entity"):
    tag.decompose()

xbrli_context = soup.find_all({"xbrli:context"})
```
This also works fine, but I can't access the original `soup` later in my script (all `<xbrli:entity>` tags are missing). Also I read in the BS4 documentation, that "*the behavior of a decomposed Tag or NavigableString is not defined and you should not use it for anything*". So I thought it would be cleaner to create a new `soup2` for this operation, so the original `soup` can be used later on.

And here's where I don't understand what's happening: When I create a second soup with a different name `soup2 = BeautifulSoup(data, "html.parser")` and use `print(soup2.prettify())` it prints nothing. Doing the same with `soup` work just fine.

**Why does `soup2` seem to be empty? How do I handle multiple versions of one soup, so that I can always start with the original soup, if I want to?**

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Unmitigated](https://stackoverflow.com/users/9513184)** (2023-03-30): `data` was exhausted after you read it once.
- **[jasonharper](https://stackoverflow.com/users/1709364)** (2023-03-30): `data` is an open file object.  Once you've read it - there's nothing more to read.  You either need to reopen the file, or rewind it to the beginning with `data.seek(0)`.
- **[henri.haiti](https://stackoverflow.com/users/21406103)** (2023-03-30): Ah, thanks to all of you! I need to read about what exactly open file objects are and how they work -- thank you! Regarding my question for best practice, would you agree that creating different soups for different operations are a good idea?
