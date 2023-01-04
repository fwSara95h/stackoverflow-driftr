---
title: "How to solve \"Move target out of bounds\" Selenium error?"
site: stackoverflow
question_id: 75011359
answer_id: 75011800
url: https://stackoverflow.com/a/75011800
author: "Andrew Ryan"
author_url: https://stackoverflow.com/users/7451892
posted: 2023-01-04T21:59:17Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 49e793666b400aeccd9c7b2731d95882387434c12e6f0e7d70dcf39a40056538
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrew Ryan](https://stackoverflow.com/users/7451892) — 2023-01-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75011800>, 2023-01-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

So it seems that the button that you are trying to click is not visible on the screen. You could try this:

    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[contains(text(),'Load More Listings')]"))

To click the button.
