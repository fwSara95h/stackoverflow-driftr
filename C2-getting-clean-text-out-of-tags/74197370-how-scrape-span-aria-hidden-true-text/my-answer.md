---
title: "how scrape - span aria-hidden=\"true\" - text"
site: stackoverflow
question_id: 74197370
answer_id: 74198014
url: https://stackoverflow.com/a/74198014
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-25T17:27:47Z
last_edited: 2022-10-26T18:38:01Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74198014/revisions
accepted: true
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 43abbe557485bceed4185554d84be1ea386d1bec8a2fb9ba104a3c8c74e44e85
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74198014>, 2022-10-25, last edited 2022-10-26; **accepted**; score 0. Text as retrieved 2026-10-12.

I can't confirm without knowing exactly what the full HTML looks like - there might be other very similarly nested elements before the snippet shared in the question, but if there aren't then you can use `soup.select_one` with the [css selectors](https://www.w3schools.com/cssref/css_selectors.php) used below:

```python
spanTxt1 = soup.select_one('span.t-14.t-normal span[aria-hidden="true"]')
if spanTxt1 is not None: spanTxt1 = spanTxt1.get_text(strip=True)

spanTxt2 = soup.select_one('span.t-14.t-normal span.visually-hidden')
if spanTxt2 is not None: spanTxt2 = spanTxt2.get_text(strip=True)

print(f' Text1: "{spanTxt1}" \n Text2: "{spanTxt2}" ')
```

should give the output

```markdown
 Text1: "Crédit Agricole CIB · Full-time" 
 Text2: "Crédit Agricole CIB · Full-time" 
```

<hr><hr>

**EDIT:**

I think the `ember..` section ids are dynamically generated and might be different every time. A more reliable selector for the jobs listed in the experience section might be
```python
expSel = 'div#experience ~ div.pvs-list__outer-container ul.pvs-list li'
```
(It's going for the list *next* to the [empty] `div id="experience"` anchor)

You can even choose a specific experience from the list by changing the end to `li:nth-child(2)` for the second experience, `li:last-child` for the last experience,  `li:nth-last-child(2)` for the *second-to-last* experience,  etc...

You could directly add on to the selector to get the first company:
```python
c1span =  soup.select_one(expSel+' span.t-14.t-normal span')
if c1span is not None:
    print(c1span.get_text(strip=True))
```
and that should print `Crédit Agricole CIB · Full-time`

<hr>

You could also use `expSel` to get *all* the listed experience:
```python
expSelRef = {
    'Position': 'span.mr1.t-bold',  
    'Company+Type': 'span.t-14.t-normal',
    'Dates': 'span.t-14.t-normal.t-black--light', 
    'Location': 'span.t-14.t-normal.t-black--light + span'
}
for e in soup.select(expSel):
    for r in expSelRef:
        eDet = e.select_one(expSelRef[r]+' span[aria-hidden="true"]')
        if eDet is not None: 
            print(f' [ {r}: "{eDet.get_text(strip=True)}" ] ', end='')
    print()
```
output:
```lang-none
 [ Position: "Structured Products & Equity Derivatives Sales" ]  [ Company+Type: "Crédit Agricole CIB · Full-time" ]  [ Dates: "Jan 2020 - Present · 2 yrs 10 mos" ]  [ Location: "Paris, Île-de-France, France" ] 
 [ Position: "Equity Sales Trader Assistant" ]  [ Company+Type: "ODDO BHF · Internship" ]  [ Dates: "Jun 2019 - Jan 2020 · 8 mos" ]  [ Location: "Paris, Île-de-France, France" ] 
 [ Position: "Wealth Management Analyst" ]  [ Company+Type: "HSBC · Internship" ]  [ Dates: "Mar 2018 - Sep 2018 · 7 mos" ]  [ Location: "Paris, Île-de-France, France" ] 
 [ Position: "Business Developper" ]  [ Company+Type: "Capgemini · Internship" ]  [ Dates: "Jan 2017 - Aug 2017 · 8 mos" ] 
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): Hi, it works but it returns another 'span text' above, as you expected it to. Do you know how to select the second one? The text I want is exactly the same but the second one.
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): The span class above appears to be different from the first one: <span class="mr1 t-bold">               <span aria-hidden="true"><!---->Structured Products &amp; Equity Derivatives Sales<!----></span><span class="visually-hidden"><!---->Structured Products &amp; Equity Derivatives Sales<!----></span>             </span>
- **me** (2022-10-26): @HugoChikli To print "Structured Products & Equity Derivatives Sales" from the second span, use `print(soup.select_one('.mr1.t-bold').get_text(strip=True))`
- **me** (2022-10-26): @HugoChikli or did you mean that you're getting "Structured Products & Equity Derivatives Sales" but you don't want to? Because then you might try my answer with `spanTxt2 = soup.select_one('span.t-14.t-normal > span.visually-hidden')` [the added `>` specifies direct descendants (children) only] - can't really tell for sure without seeing full html though
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): When I use your code, I get a text from a section a little before on the website that has precisely the same division HTML. The website is a LinkedIn profile page where I wanted to get the information about the experience.
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): I want the text from this section <section id="ember941" class="artdeco-card ember-view relative break-words pb3 mt2 " tabindex="-1"><!----> and not ember940
- **me** (2022-10-26): @HugoChikli try `spanTxt2 = soup.select_one('section#ember941 span.t-14.t-normal > span.visually-hidden')` ?
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): I am getting a 'None'
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): spanTxt1 = soup.select_one('span.t-14.t-normal span[aria-hidden="true"]')     if spanTxt1 is not None: spanTxt1 = spanTxt1.get_text(strip=True)      spanTxt2 = soup.select_one('section#ember941 span.t-14.t-normal span.visually-hidden')     if spanTxt2 is not None: spanTxt2 = spanTxt2.get_text(strip=True)      print(f' Text1: "{spanTxt1}" \n Text2: "{spanTxt2}" ')
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): Text1: "Thibault’s recent posts and comments will be displayed here."   Text2: "None"
- **me** (2022-10-26): @HugoChikli I can't debug without the actual link/ full html
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): here is the link: https://www.linkedin.com/in/thibault-arrighi-a43296130/
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): So I want to get the first experience and after ideally the company and start date ! Let me know if you can help
- **me** (2022-10-26): @HugoChikli please see my edits and let me know if it works. I addeda few more details than asked for; feel free to ignore the second part of my edit
- **me** (2022-10-26): @HugoChikli ....I do wish you had shared the link earlier - I actually once posted [another answer](https://stackoverflow.com/a/73957068/12652373) about the experience section of LinkedIn which might have helped you
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): Yes, it is working now thank you!! I am just not sure what refers to what? So if I want to export this in pandas data frame should I just use expSelRef?
- **[LaC](https://stackoverflow.com/users/20332244)** (2022-10-26): Hi, don't bother i figured it out !! Big thanks @Driftr95 !! This truly helps
