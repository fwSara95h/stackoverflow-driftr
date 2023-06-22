---
title: "how to extract the texts after the first h1 Tag?"
site: stackoverflow
question_id: 76530572
url: https://stackoverflow.com/q/76530572
asked: 2023-06-22T09:43:44Z
asked_by: "Mostafa Bouzari"
asked_by_url: https://stackoverflow.com/users/4575197
last_edited: 2025-01-21T15:03:30Z
last_editor: "VLAZ"
last_editor_url: https://stackoverflow.com/users/3689450
tags: [python, html, beautifulsoup, content-management-system]
score: 0
views_at_snapshot: 199
answer_count: 2
accepted_answer_id: 76532726
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 56373ca55ad660f8bed5671aca3b4ada25547ca4932630a385bc9dfb441a358b
---

# how to extract the texts after the first h1 Tag?

Asked by [Mostafa Bouzari](https://stackoverflow.com/users/4575197) on Stack Overflow, <https://stackoverflow.com/q/76530572>, 2023-06-22, last edited 2025-01-21 by [VLAZ](https://stackoverflow.com/users/3689450). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i'm trying to write a code to get and clean the text from 100 websites per day. i came across an issue with one website that has More than one h1 tag and when you scroll to the next h1 tag the URL on the website changes for example [this website][1]. 

what i have is basically this. 
   

    response=requests.get('https://economictimes.indiatimes.com/news/international/business/volkswagen-sets-5-7-revenue-growth-target-preaches-cost-discipline/articleshow/101168014.cms',headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})      
    soup = BeautifulSoup(response.content, 'html.parser')
     if len(soup.body.find_all('h1'))>2:    #to check if there is more than one tag      
        if i.endswith(".cms"):              #to check if the website has .cms ending (i have my doubts on this part)
          for elem in soup.next_siblings:
            if elem.name == 'h1':
               GET THE TEXT SOME HOW
              
            break

How can i get the text after first h1 tag? (please note that the text is in <div> tag and not in <p> tag. 

  [1]: https://economictimes.indiatimes.com/news/international/business/volkswagen-sets-5-7-revenue-growth-target-preaches-cost-discipline/articleshow/101168014.cms
