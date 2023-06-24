---
title: "Remove tag containing a certain text"
site: stackoverflow
question_id: 76545651
url: https://stackoverflow.com/q/76545651
asked: 2023-06-24T10:40:39Z
asked_by: "Floppy88"
asked_by_url: https://stackoverflow.com/users/1077533
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 43
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 776d83c27a5d584aa5d29644e05f94721380d6635fa28e0e2277e25c4b3bd85e
---

# Remove tag containing a certain text

Asked by [Floppy88](https://stackoverflow.com/users/1077533) on Stack Overflow, <https://stackoverflow.com/q/76545651>, 2023-06-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this HTML code:

    <p>
    	<strong>
    		Read our full
    		<a href="">
    			review
    		</a>
    	</strong>
    </p>

I would like to remove all 'p' tags containing 'Read our full' string using BeautifulSoup. I tried the following code, but it doesn't work

    for x in soup.find_all("p", text=re.compile('Read our full')): 
        x.decompose()
