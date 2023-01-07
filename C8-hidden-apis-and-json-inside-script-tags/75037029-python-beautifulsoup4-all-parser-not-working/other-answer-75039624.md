---
title: "Python Beautifulsoup4 all parser not working?"
site: stackoverflow
question_id: 75037029
answer_id: 75039624
url: https://stackoverflow.com/a/75039624
author: "Vincent Lagache"
author_url: https://stackoverflow.com/users/20929778
posted: 2023-01-07T10:34:37Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2392fe895c1fbb429a13044c9e0f5f4b7ff4e0ebf93bf62a656470a905a6a341
role: another answer on the same question, kept as context; not my work
---

# Answer by [Vincent Lagache](https://stackoverflow.com/users/20929778) — 2023-01-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75039624>, 2023-01-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I don't know what exactly is your goal in scraping, but have you tried 

```python
soup = BeautifulSoup(page.content, 'html.parser')
```

After that, your code works perfectly for me and returns good urls at the end of the script

```console
https://www.aliexpress.com/item/1005004643645808.html?algo_pvid=36f2290b-a7f6-4a43-8d4e-cb427a255b22&algo_exp_id=36f2290b-a7f6-4a43-8d4e-cb427a255b22-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000030390398106%22%7D&pdp_npi=2%40dis%21EUR%213.8%211.79%21%21%21%21%21%402100b20d16730874440116525d06ef%2112000030390398106%21sea&curPageLogUid=TO7uEnR4RcFE
https://ae01.alicdn.com/kf/Sba697dac347c425bbbc16a0f71d8a534W/Mini-Tracking-Device-Tracking-Air-Tag-Key-Child-Finder-Pet-Tracker-Location-Smart-Bluetooth-Tracker-Car.jpg_220x220xz.jpg
```
