---
title: "Extract Data from <script> in html"
site: stackoverflow
question_id: 75046158
url: https://stackoverflow.com/q/75046158
asked: 2023-01-08T07:34:56Z
asked_by: "user19022072"
asked_by_url: (account no longer exists)
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 266
answer_count: 1
accepted_answer_id: 75050526
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d5cd9cdeb8f908c225f4aba8a4b05071907cd3f58028b7ec14f797fe350dfff5
---

# Extract Data from <script> in html

Asked by user19022072 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/75046158>, 2023-01-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to extract data from an HTML script without success.
I'm able to get all the text content of the script that has the data I'm looking for, all I have to do is extract the relevant data.

``` 
response = requests.get('https://www.yad2.co.il/item/ajyw4gne', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
more_data = soup.find_all("script")[13]

```
link : https://www.yad2.co.il/item/ajyw4gne

[![The data in the website][1]][1]
[![The data from the script][2]][2]


  [1]: https://i.sstatic.net/LTkm4.png
  [2]: https://i.sstatic.net/5emhV.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-01-08): That's Javascript code.  You code hack your way with regular expressions, or you can switch to Selenium and let the Chrome browser interpret the Javascript for you.
- **user19022072 (account no longer exists)** (2023-01-08): @Tim Roberts I know I can do it with Selenium but I'm sure there is another way without selenium
- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-01-08): Wishful thinking is not a good engineering strategy.  The numbers are not in the HTML you receive.  You have to execute the Javascript.  End of story.
- **user19022072 (account no longer exists)** (2023-01-09): @Tim Roberts look on the solution of Driftr95 this is what I looking for
