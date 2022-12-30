---
title: "python beautifulsoup - parsing an HTML table row"
site: stackoverflow
question_id: 74959245
url: https://stackoverflow.com/q/74959245
asked: 2022-12-30T07:43:45Z
asked_by: "Meghan M."
asked_by_url: https://stackoverflow.com/users/9915864
last_edited: 2022-12-30T08:56:45Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 145
answer_count: 1
accepted_answer_id: 74961683
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c6d60d272032ee51887a99fd857c1a6682c82e1c45124e646299804508c0f296
---

# python beautifulsoup - parsing an HTML table row

Asked by [Meghan M.](https://stackoverflow.com/users/9915864) on Stack Overflow, <https://stackoverflow.com/q/74959245>, 2022-12-30, last edited 2022-12-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm using BeautifulSoup to parse a bunch of combined tables' rows, row by row, column by column in order to import it into Pandas. I can't use `to_html()` because one of the columns has a list of tag links in each cell. The data structure is the same in all the tables. 

I can't figure out the correct method to skip a `td.div` tag containing the attribute`{'class': ['stars']}`. My following code works but it doesn't seem correct. I can't just do a `if col.div: continue` because some of the required columns have extra `<div>` tags I need for later. 

```    
    def rebuild_row(self, row):
        new_row = []
        for col in row.find_all('td'):
            if col.img:
                continue
            if col.div and 'star' in str(col.div.attrs):
                continue
            if col.a:
                new_row.append(self.handle_links(col))
            else:
                if not col.text or not col.text.strip():
                    new_row.append(['NaN'])
                else:
                    new_text = self.clean_tag_text(col)
                    new_row.append(new_text)
        return new_row
```

I first tried `if 'stars' in col.div['class']:` but it choked on `key 'class'`. So then I tried to find the error:
```
            if col.div:
                if not hasattr(col.div, 'class'):
                    continue
                else:
                    print(f"{col.div['class']}")
```
but I get this output & error that I don't understand the why of because shouldn't the `not hasattr()` catch it?
```
['stars']
['stars']
Exception has occurred: KeyError
'class'
```


HTML row example:
```
<tr id="groupBook3144889">
<td width="5%"><a href="/book/show/40851529-the-7th-of-victorica"><img alt="The 7th of Victorica by Beau Schemery" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1531785241l/40851529._SY75_.jpg" title="The 7th of Victorica by Beau Schemery"/></a></td>
<td width="30%">
<a href="/book/show/40851529-the-7th-of-victorica">The 7th of Victorica (Gadgets and Shadows, #2)</a>
</td>
<td width="10%">
<a href="/author/show/6594115.Beau_Schemery">Schemery, Beau</a>
<span title="Goodreads Author!">*</span>
</td>
<td width="1%">
<div class="stars" data-rating="0" data-resource-id="40851529" data-restore-rating="null" data-submit-url="/review/rate/40851529?stars_click=false" data-user-id="0"><a class="star off" href="#" ref="" title="did not like it">1 of 5 stars</a><a class="star off" href="#" ref="" title="it was ok">2 of 5 stars</a><a class="star off" href="#" ref="" title="liked it">3 of 5 stars</a><a class="star off" href="#" ref="" title="really liked it">4 of 5 stars</a><a class="star off" href="#" ref="" title="it was amazing">5 of 5 stars</a></div>
</td>
<td width="1%">
<a class="actionLinkLite" href="/group/bookshelf/64285?shelf=read">read</a>, 
                    <a class="actionLinkLite" href="/group/bookshelf/64285?shelf=genre-action-adventure">genre-action-adve...</a>, 
                    <a class="actionLinkLite" href="/group/bookshelf/64285?shelf=genre-steampunk-dieselpunk">genre-steampunk-d...</a>, 
                    <a class="actionLinkLite" href="/group/bookshelf/64285?shelf=genre-young-adult">genre-young-adult</a>
</td>
<td width="1%">
                 
          </td>
<td width="1%">
                 
          </td>
<td width="1%">
<a href="/user/show/4872508-meghan"> Meghan</a>
</td>
<td width="1%">2022/12/25</td>
<td class="view" width="1%">
<a class="actionLink" href="/group/show_book/64285?group_book_id=3144889" style="white-space: nowrap">view activity »</a>
</td>
</tr>
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ScottC](https://stackoverflow.com/users/20174226)** (2022-12-30): Instead of `if not hasattr(col.div, 'class'):` you could possibly use `try-except` instead.
- **[Meghan M.](https://stackoverflow.com/users/9915864)** (2022-12-30): Thanks for reply. Since I'm self-taught in python, I don't use try-except that often. How would I apply it here? Like this? `try: if 'star' in col.div['class']: continue; except: pass` The result I got with that added some `col.div` to the new row resulting in an extra column. So I'm missing something?
- **[Meghan M.](https://stackoverflow.com/users/9915864)** (2022-12-30): I should mention that when I go for a direct `if col.div: continue`, it drops some of the more finicky columns resulting in an uneven number of columns per row.
- **[Meghan M.](https://stackoverflow.com/users/9915864)** (2022-12-30): This isn't my ideal solution but it works and is the simplest. I'm still not sure that checking `str(col.div.attrs)` is the right way to do it:   `for col in row.find_all('td'): if col.div and 'star' in str(col.div.attrs): continue;`
