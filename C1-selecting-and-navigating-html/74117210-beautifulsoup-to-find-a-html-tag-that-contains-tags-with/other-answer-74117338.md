---
title: "BeautifulSoup to find a HTML tag that contains tags with specific class"
site: stackoverflow
question_id: 74117210
answer_id: 74117338
url: https://stackoverflow.com/a/74117338
author: "Rahul K P"
author_url: https://stackoverflow.com/users/4407666
posted: 2022-10-18T20:52:06Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1f4851970c83484bebe376b149a38d173b7d97cb2026e516ee925ba1423a0b55
role: another answer on the same question, kept as context; not my work
---

# Answer by [Rahul K P](https://stackoverflow.com/users/4407666) — 2022-10-18

Posted on Stack Overflow, <https://stackoverflow.com/a/74117338>, 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You need to find matching with `td`. Like this,

    In [1]: bs.find_all('td', {"class": re.compile(r'TD\w\d')})
    Out[1]: 
    [<td class="TDo1" width="17%">Tournament</td>,
     <td class="TDo2" width="8%">Date</td>,
     <td class="TDo2" width="6%">Pts.</td>,
     <td class="TDo2" width="34%">Pos. Player (team)</td>,
     <td class="TDo5" width="35%">Pos. Opponent (team)</td>,
     <td class="TDq1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>,
     <td class="TDq2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>,
     <td class="TDq3">34/75</td>,
     <td class="TDq5">39. John Deep</td>,
     <td class="TDq9">68. <a href="p.pl?ply=1229">Mark Deep</a></td>,
     <td class="TDp1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>,
     <td class="TDp2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>,
     <td class="TDp3">34/75</td>,
     <td class="TDp6">39. John Deep</td>,
     <td class="TDp8">7. <a href="p.pl?ply=10">Darius Star</a></td>]
