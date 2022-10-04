---
title: "I want to scrape all the text like heading, bullets paragraph from article acept some <p> tags from start of the article and from end of the article"
site: stackoverflow
question_id: 73948314
url: https://stackoverflow.com/q/73948314
asked: 2022-10-04T13:03:53Z
asked_by: "Info Rewind"
asked_by_url: https://stackoverflow.com/users/20147022
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-newspaper, newspaper3k]
score: 0
views_at_snapshot: 340
answer_count: 1
accepted_answer_id: 73952457
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 534329f834be83a1faecf8e434a5e638c2c450d5581648e63407e8f29fbb16e0
---

# I want to scrape all the text like heading, bullets paragraph from article acept some <p> tags from start of the article and from end of the article

Asked by [Info Rewind](https://stackoverflow.com/users/20147022) on Stack Overflow, <https://stackoverflow.com/q/73948314>, 2022-10-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape the Article for this site

https://www.traveloffpath.com/covid-19-travel-insurance-everything-you-need-to-know/
and https://www.traveloffpath.com/what-to-do-if-your-flight-is-delayed-or-canceled/?swcfpc=1
I am stuck in the "p" tag because I don't want "p" tags from the start of the article and from the end of the article as I don't want "p" Share the article"p" and "p" last updated "p" and some "p" tag from the bottom text that is not included in the article. 



<!-- language: lang-python -->

    Articletext = soup.find(class_="article")
    for items in soup.find_all(class_="article"):
        Gather = '\n'.join([item.text for item in items.find_all(["h6","h5","h4","h3","h2","h1","p","li"])])
        filtered = Gather.split("↓ Join the community ↓")
        Content = filtered[0].split("Email")
        while True :
            try:
                Content = filtered[0].split("Email")
                
            except :
                Content = Content[1].split("ago")
            else :
                break
        # try:
        #     Content = filtered[0].split("Email")
        # except:
        #     Content = filtered[0].split("ago")
        # Content = re.split('ago | Read More:',Gather) 
        print("Content: ", Content[1])

<!-- end snippet -->

[enter image description here][1]


  [1]: https://i.sstatic.net/zqPtU.png

> Blockquote

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[psykx](https://stackoverflow.com/users/1898063)** (2022-10-04): Use a DOM parser to parse the dom and then inspect it. Don't reinvent the wheel.
- **[furas](https://stackoverflow.com/users/1832058)** (2022-10-04): you can always get list with all `<p>` and later slice this list `[1:-1]` to get without first and without last.
- **me** (2022-10-04): By *'some "p" tag from the bottom text that is not included in the article'* do you mean the list of links for recommended further reading and the *"This article originally appeared...."* bit?
- **[Info Rewind](https://stackoverflow.com/users/20147022)** (2022-10-04): I have found the answer myself, for the link above I mentioned. #===  Articletext = soup.find(class_="article") #===  for items in soup.find_all(class_="article"): #===     Gather = '\n'.join([item.text for item in items.find_all(["h6","h5","h4","h3","h2","h1","p","li"])]) #===     filtered = Gather.split("↓ Join the community ↓") #===     Content = filtered[0].split("Email") #===     word = "ago" #===     if word in Content[1]: #===         Content = Content[1].split("ago") #===      print("Content: ", Content[1])
