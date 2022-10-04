---
title: "Elements able to be found using XPATH but not using CSS Selector. Am I searching using the correct value?"
site: stackoverflow
question_id: 73942961
answer_id: 73943472
url: https://stackoverflow.com/a/73943472
author: "AbiSaran"
author_url: https://stackoverflow.com/users/7671727
posted: 2022-10-04T05:32:43Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 04150984057d1531189086b60890b7a036b68430635899024428cab6e43d1929
role: another answer on the same question, kept as context; not my work
---

# Answer by [AbiSaran](https://stackoverflow.com/users/7671727) — 2022-10-04

Posted on Stack Overflow, <https://stackoverflow.com/a/73943472>, 2022-10-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You have mentioned the wrong locator type, it should be CSS_SELECTOR and also put a dot '.' in front of element's property, because it is a 'class':

    text_data = WebDriverWait(driver,10).until(EC.visibility_of_all_element_located((By.CSS_SELECTOR,'.Card___StyledLi4-ulg8ho-7.jmevwM')

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Xaldin](https://stackoverflow.com/users/20154862)** (2022-10-04): Ah!! Thank you! I’m still new to this. I’ll be sure to never forget this though
