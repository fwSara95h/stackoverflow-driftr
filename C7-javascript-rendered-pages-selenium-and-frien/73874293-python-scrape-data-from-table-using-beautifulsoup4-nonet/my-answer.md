---
title: "Python - Scrape Data from Table using BeautifulSoup4: 'NoneType' object has no attribute 'find'"
site: stackoverflow
question_id: 73874293
answer_id: 73874480
url: https://stackoverflow.com/a/73874480
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-27T22:44:24Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73874480/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: df85dbbe1df50771fea8d90ed7ac7058b50d106f6b677ac9a70fd58213e380ac
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73874480>, 2022-09-27; score 0. Text as retrieved 2026-10-12.

The error is raised at `table = soup.find...`, but the problem is actually that the site is blocking `requests.get` to protect itself, so your code hasn't scraped or even accessed the site at all. 

It works with [selenium](https://www.scrapingbee.com/blog/selenium-python/) for me (possibly because it's a bit better at mimicking human behavior.)

    #from selenium import webdriver
    
    def linkSoup(l):  
        # I downloaded and saved 'chromedriver.exe' to the same folder as this .py file
        driverD = webdriver.Chrome('chromedriver.exe')
        driverD.get(l)
        lSoup = BeautifulSoup(driverD.page_source, 'html.parser')
        driverD.close()
        del driverD
        return lSoup 
    
    
    soup = linkSoup('https://inmotion.dhl/en/formula-1/fastest-pit-stop-award')
    
    table = soup.find("table", class_="f1-award-table")
    table_body = table.find('tbody')
    
    rows = table_body.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        print(cols)

The results look [like this][1].


  [1]: https://i.sstatic.net/Ga0kY.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[LawrenceTN](https://stackoverflow.com/users/9078486)** (2022-09-28): I appreciate the response. I had a feeling it had something to do with security and me not being able to access it. I'm super new to Python and API's in general so this is exciting stuff. Other than that issue, it seems like my logic/code was correct I believe? I just needed to find a way to bypass the block.
- **me** (2022-09-28): @LawrenceTN yes, the bs4 parts are fine, you just have to gain access first
