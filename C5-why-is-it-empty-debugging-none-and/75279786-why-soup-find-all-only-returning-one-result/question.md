---
title: "Why soup. find_all() only returning one result"
site: stackoverflow
question_id: 75279786
url: https://stackoverflow.com/q/75279786
asked: 2023-01-30T02:24:35Z
asked_by: "Franklin Ekwem"
asked_by_url: https://stackoverflow.com/users/21030554
last_edited: 2023-01-31T08:30:55Z
last_editor: "Adriaan"
last_editor_url: https://stackoverflow.com/users/5211833
tags: [python, list, beautifulsoup, element]
score: -3
views_at_snapshot: 110
answer_count: 1
accepted_answer_id: 75296465
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b552ac422eae65ec97ee0fe4a4f304f3a2fb435b226abc3af92b0671df85a901
---

# Why soup. find_all() only returning one result

Asked by [Franklin Ekwem](https://stackoverflow.com/users/21030554) on Stack Overflow, <https://stackoverflow.com/q/75279786>, 2023-01-30, last edited 2023-01-31 by [Adriaan](https://stackoverflow.com/users/5211833). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm scraping some information and below is my code
```
from bs4 import BeautifulSoup
import requests

url = "https://www.privateproperty.com.ng/property-for-sale"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_="similar-listings-item sponsored-listing")

for result in results:
    Title = result.find('div', class_= "similar-listings-info").text.replace('\n','')
    location = result.find( class_= "listings-location").text.replace('\n','')
    Price = result.find('div', class_= "similar-listings-price").text.replace('\n','')
    

info = (Title, location, Price)
print(info)
```
Why does this line 
```
results = soup.find_all('div', class_="similar-listings-item sponsored-listing") 
```
return only the 1st element?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-01-30): `Soup.find_all()` returns a list.  If you want a list-of-lists, you'll have to process those results and build it yourself.
- **[Franklin Ekwem](https://stackoverflow.com/users/21030554)** (2023-01-30): Thank you John, please how can I do that?
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-01-30): It sounds like you're asking me to write your program for you...
- **[Franklin Ekwem](https://stackoverflow.com/users/21030554)** (2023-01-30): Yes John Gordon, please could you help me with better language that enable me get the list of lists of the above function.
- **me** (2023-01-30): what's the html you're working with, and what output do you want to extract from it? the question is quite vague, but maybe you want to do something like [this](https://pastebin.com/ZnZ7xM6u) with [list comprehension](https://www.programiz.com/python-programming/list-comprehension)
