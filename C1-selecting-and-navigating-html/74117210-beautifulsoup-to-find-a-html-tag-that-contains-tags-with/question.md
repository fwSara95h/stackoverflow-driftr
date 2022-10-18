---
title: "BeautifulSoup to find a HTML tag that contains tags with specific class"
site: stackoverflow
question_id: 74117210
url: https://stackoverflow.com/q/74117210
asked: 2022-10-18T20:38:50Z
asked_by: "Tomasz Maciążek"
asked_by_url: https://stackoverflow.com/users/15698050
last_edited: 2022-10-18T21:04:46Z
last_editor: "Wiktor Stribiżew"
last_editor_url: https://stackoverflow.com/users/3832970
tags: [python, beautifulsoup, findall]
score: 2
views_at_snapshot: 83
answer_count: 4
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: af3e0139e142382a2cdac3ad07aaf7300bb0f8fd49a38618fe5eabe1f010a180
---

# BeautifulSoup to find a HTML tag that contains tags with specific class

Asked by [Tomasz Maciążek](https://stackoverflow.com/users/15698050) on Stack Overflow, <https://stackoverflow.com/q/74117210>, 2022-10-18, last edited 2022-10-18 by [Wiktor Stribiżew](https://stackoverflow.com/users/3832970). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

How to find all tags that include tags with certain class?
The data is:

    <tr>
    <td class="TDo1" width=17%>Tournament</td>
    <td class="TDo2" width=8%>Date</td>
    <td class="TDo2" width=6%>Pts.</td>
    <td class="TDo2" width=34%>Pos. Player (team)</td>
    <td class="TDo5" width=35%>Pos. Opponent (team)</td>
    </tr>
    
    <tr>
    <td class=TDq1><a href="p.pl?t=410">GpWl(op)&nbsp;4.01/02</a></td>
    <td class=TDq2><a href="p.pl?t=410&r=4">17.02.02</a></td>
    <td class=TDq3>34/75</td>
    <td class=TDq5>39. John Deep</td>
    <td class=TDq9>68. <a href="p.pl?ply=1229">Mark Deep</a></td>
    </tr>
    
    <tr>
    <td class=TDp1><a href="p.pl?t=410">GpWl(op)&nbsp;4.01/02</a></td>
    <td class=TDp2><a href="p.pl?t=410&r=4">17.02.02</a></td>
    <td class=TDp3>34/75</td>
    <td class=TDp6>39. John Deep</td>
    <td class=TDp8>7. <a href="p.pl?ply=10">Darius Star</a></td>
    </tr>

I am trying

    for mtable in bs.find_all('tr', text=re.compile(r'class=TD?3')):
    print(mtable)

but this returns zero results.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Robert](https://stackoverflow.com/users/1431720)** (2022-10-18): `text()` is what's between the `<td ...>` and the `</td>`. You want `@class` I think... if this is XPath syntax
