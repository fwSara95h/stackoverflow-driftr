---
title: "Trying to request information from \"IDEALISTA webpage\" in PYTHON with \"requests\" and I get <Response [403]>"
site: stackoverflow
question_id: 74173137
answer_id: 74185990
url: https://stackoverflow.com/a/74185990
author: "d r"
author_url: https://stackoverflow.com/users/19023353
posted: 2022-10-24T19:37:07Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2a79e9b360da3570d26304344a02e86b2156c3def7b14f021f5e48cca56b518c
role: another answer on the same question, kept as context; not my work
---

# Answer by [d r](https://stackoverflow.com/users/19023353) — 2022-10-24

Posted on Stack Overflow, <https://stackoverflow.com/a/74185990>, 2022-10-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You should ALWAYS check the robots.txt file if you want to scrape a page. Read this: ( https://dan-suciu.medium.com/the-complete-manual-to-legal-ethical-web-scraping-in-2021-3eeae278b334 )    
 In the case of your 2nd url it seems like the scraping is not allowed - it is blocked. Try the url  https://www.idealista.com/robots.txt and see the  text, google translates it as:    
**Misuse has been detected Access has been blocked
Having trouble accessing the site? Contact support
ID: fc1d890d-6ed6-8959-cd68-de965251f89b
IP: xx.xx.xx.xx
All the best,
The idealist team**    

Regards...
