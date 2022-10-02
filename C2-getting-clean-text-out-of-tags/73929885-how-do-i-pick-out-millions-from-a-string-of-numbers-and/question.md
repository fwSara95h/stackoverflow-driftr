---
title: "How do I pick out millions from a string of numbers and commas?"
site: stackoverflow
question_id: 73929885
url: https://stackoverflow.com/q/73929885
asked: 2022-10-02T22:53:09Z
asked_by: "Michael"
asked_by_url: https://stackoverflow.com/users/20145764
last_edited: 2022-10-02T23:19:45Z
last_editor: "Stephen C"
last_editor_url: https://stackoverflow.com/users/139985
tags: [python, string, beautifulsoup, filter]
score: 2
views_at_snapshot: 158
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6e31a8b4943270eac820a0490c27fdd6d0e4d5461970ac7cb11e062594982f0
---

# How do I pick out millions from a string of numbers and commas?

Asked by [Michael](https://stackoverflow.com/users/20145764) on Stack Overflow, <https://stackoverflow.com/q/73929885>, 2022-10-02, last edited 2022-10-02 by [Stephen C](https://stackoverflow.com/users/139985). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I was using beautifulsoup to do some web scraping on Yahoo Finance for fun. The goal is to take the html file, find the financial data and place it into an array. I've managed to get the output to this format

Total Revenue42,965,39136,483,93920,139,65822,588,85825,067,279

How would I split the numbers into millions? For example we know 42,965,39136,483,939 is actually 42,965,391 and 36,483,939 but how do we code for this? I've tried using regex without success. 

    with open('Nucor Yahoo HTML.html','r') as html:
	content = html.read()
	soup = BeautifulSoup(content, 'lxml')
	tables = soup.find_all(class_ = 'rw-expnded')
	for table in tables:
		pattern = re.compile(r'\d\d\d?,[0-9]{3},[0-9]{3}')
		matches = pattern.finditer(table.text)
		for match in matches:
			print(match)
		print(table.text)

the html file is here:https://finance.yahoo.com/quote/NUE/financials?p=NUE

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[infinitezero](https://stackoverflow.com/users/5436259)** (2022-10-02): Can you not get it in a better format to begin with?
