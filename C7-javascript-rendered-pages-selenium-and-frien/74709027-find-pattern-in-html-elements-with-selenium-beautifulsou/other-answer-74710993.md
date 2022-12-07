---
title: "Find pattern in HTML elements with Selenium/BeautifulSoup"
site: stackoverflow
question_id: 74709027
answer_id: 74710993
url: https://stackoverflow.com/a/74710993
author: "AbiSaran"
author_url: https://stackoverflow.com/users/7671727
posted: 2022-12-07T02:11:16Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 048afab9af02b2fe7ee695a428aee1bf992c50f9bdd78bf6c13a66909bdf3627
role: another answer on the same question, kept as context; not my work
---

# Answer by [AbiSaran](https://stackoverflow.com/users/7671727) — 2022-12-07

Posted on Stack Overflow, <https://stackoverflow.com/a/74710993>, 2022-12-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can try this:

Here I am writing only the starting section of the XPath - ie, how to handle the dynamic value 'id="heat-85940"', pls fill in the remaining XPath, because you didn't post the URL and full HTML source.

    driver.find_element(By.XPATH, ".//*[starts-with(@id,'heat-')]...<remaining XPath until the element>")

or

    driver.find_element(By.XPATH, ".//*[starts-with(@id,'heat-8594')]...<remaining XPath until the element>")
