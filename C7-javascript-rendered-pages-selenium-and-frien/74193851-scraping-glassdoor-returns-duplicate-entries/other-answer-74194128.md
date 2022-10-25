---
title: "Scraping Glassdoor returns duplicate entries"
site: stackoverflow
question_id: 74193851
answer_id: 74194128
url: https://stackoverflow.com/a/74194128
author: "Asad Ikram"
author_url: https://stackoverflow.com/users/20181742
posted: 2022-10-25T12:31:45Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 892fc705cc8f839720bd31918d21adb85447973dd76ca1a6fc7318281bd911f0
role: another answer on the same question, kept as context; not my work
---

# Answer by [Asad Ikram](https://stackoverflow.com/users/20181742) — 2022-10-25

Posted on Stack Overflow, <https://stackoverflow.com/a/74194128>, 2022-10-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You're going way too fast. You need to put some waits. 

I see you have put Implicit Waits. Trying putting Explicit Waits instead. 

Something like this:

 (put your own conditions. you can try invisibility element too. like if something is invisible and then visible to ensure you are on next page now)
if not then increase your time.sleep()

    WebDriverWait(driver, 40).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="wrapper"]/section/div/div/div[2]/button[2]')))

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Zoya Aqib](https://stackoverflow.com/users/15606732)** (2022-10-25): Tried that and it didn't work. I just went to the Glassdoor website and discovered that page 7 and onwards, it literally starts duplicating the search results from page 1. No idea why.
- **[Asad Ikram](https://stackoverflow.com/users/20181742)** (2022-10-26): Is it for specific user? If you change your user-agent and Ip and go to page 8 will it keep showing duplicate records?
- **[Zoya Aqib](https://stackoverflow.com/users/15606732)** (2022-10-26): I tried Incognito mode, VPN, another computer, with and without logging in....everything. Still the same. Really strange
- **[Asad Ikram](https://stackoverflow.com/users/20181742)** (2022-10-27): Can be restriction on their frond-end then
- **[Asad Ikram](https://stackoverflow.com/users/20181742)** (2022-10-27): I've a way around for it which I can't share here. Try reaching me on Linked-in
