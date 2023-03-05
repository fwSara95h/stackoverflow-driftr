---
title: "Obtaining HREF with Python BeautifulSoup (BS4) with no apparent tags"
site: stackoverflow
question_id: 75645404
url: https://stackoverflow.com/q/75645404
asked: 2023-03-05T21:17:50Z
asked_by: "walksonair"
asked_by_url: https://stackoverflow.com/users/15696430
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 45
answer_count: 1
accepted_answer_id: 75645927
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bf492e65aee70e37668a2597ee23720c10fcc80c5782f422e920462cbeb2abdc
---

# Obtaining HREF with Python BeautifulSoup (BS4) with no apparent tags

Asked by [walksonair](https://stackoverflow.com/users/15696430) on Stack Overflow, <https://stackoverflow.com/q/75645404>, 2023-03-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to grab the URL from this HTML code subset. Basically, I found all `<item>` tags using `soup.find_all('item', class_="sale-item")` and would like to extract the URL from the first href. Can anyone assist?

    <item class="sale-item" style="margin:6px; padding: 0; text-decoration:none;" tabindex="0" title="">
    <style="text-decoration:none; display:block"="" height:100%;="" href="http://www.assus.com/12165456ALPHA.html">
    <header>
    <div class="smaht-header" style="width:100%; color:#000000; background-color:#EEEEEE;"><span style="color:#2a6293!important">ONLINE-ONLY</span></div>
    <div style="color:#2a6293; width:100%; float:left">
    ....code continues to </item>

A lot of the BS4 solutions assume the href is encapsulated in the `a` tag. I'm unsure how to proceed with this setup...thank you in advance!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[AJ222](https://stackoverflow.com/users/1800459)** (2023-03-05): Why not use a regex? for example https://regex101.com/r/8Ks47b/1
