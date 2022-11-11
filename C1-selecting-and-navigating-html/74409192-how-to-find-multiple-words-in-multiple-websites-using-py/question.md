---
title: "How to find multiple words in multiple websites using Python?"
site: stackoverflow
question_id: 74409192
url: https://stackoverflow.com/q/74409192
asked: 2022-11-11T23:30:43Z
asked_by: "nihility24"
asked_by_url: https://stackoverflow.com/users/19563980
last_edited: 2022-11-11T23:35:52Z
tags: [python, web-scraping, beautifulsoup, text-mining]
score: 0
views_at_snapshot: 392
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 408e49aaf5eff7504032abf19088cbef7f3333bfe81f70ab9759fa22ec0aec40
---

# How to find multiple words in multiple websites using Python?

Asked by [nihility24](https://stackoverflow.com/users/19563980) on Stack Overflow, <https://stackoverflow.com/q/74409192>, 2022-11-11, last edited 2022-11-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of 100+ companies and I want to know if they have specific products, certifications. I have used the code below to count the number **1 specific word** in multiple websites (found the code from kind-hearted strangers in stackoverflow). (A) But, how can I edit the query the_word to include multiple words? 

(B) Also, what about partial words,such as I want a line with the word "certification" but, it can be also there as '...we certified...' or, '...received certificate...'. I guess the easy hack is to use all possible words and search them. In SQL, there are wildcard letters, such as LIKE certi% . Is there any similar ideas? 

THANKS IN ADVANCE !!!

```
#Counts and gives the lines in websites
import requests
from bs4 import BeautifulSoup

url_list = ["http://www.a-w-s.co.uk/","http://www.albanywindows.co.uk","http://www.aimwindows.co.uk"]

#the_word = input()
the_word = 'UKCA','CA

total_words = []
for url in url_list:
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content.lower(), 'lxml')
    words = soup.find_all(text=lambda text: text and the_word.lower() in text)
    count = len(words)
    words_list = [ ele.strip() for ele in words ]
    for word in words:
        total_words.append(word.strip())

    print('\nUrl: {}\ncontains {} of word: {}'.format(url, count, the_word))
    print(words_list)

#print(total_words)
total_count = len(total_words) ```


Works for 1 word but, when I tried,  
the_word= 'UKCA', 'CA', 'PS24' 
the_word= ['UKCA', 'CA', 'PS24']
the_word= ('UKCA', 'CA', 'PS24') 

Error... How to fix this!
