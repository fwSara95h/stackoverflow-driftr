---
title: "beautifulsoup for google search result"
site: stackoverflow
question_id: 76547451
url: https://stackoverflow.com/q/76547451
asked: 2023-06-24T18:20:19Z
asked_by: "Saravanan Ragavan"
asked_by_url: https://stackoverflow.com/users/15837741
last_edited: 2023-07-08T17:56:14Z
tags: [python, beautifulsoup]
score: 1
views_at_snapshot: 1703
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a725d4530cb1e3abab075c4f33fe22d903213f6357b734edf6f2c1afc644a663
---

# beautifulsoup for google search result

Asked by [Saravanan Ragavan](https://stackoverflow.com/users/15837741) on Stack Overflow, <https://stackoverflow.com/q/76547451>, 2023-06-24, last edited 2023-07-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am new to beautifulsoap and python. I want to scrape google search result by using beautifulsoap. 

Expecting this: 
1) Title, Link, Description of Search Results for first three result only
2) Below code I mentioned keyword in python file itself. How to make it dynamic(when run the file, it should ask me for keyword)

Below is the code I tried. However, I am stuck with the results


    # Import the beautifulsoup
    # and request libraries of python.
    import requests
    import bs4
    
    # Make two strings with default google search URL
    # 'https://google.com/search?q=' and
    # our customized search keyword.
    # Concatenate them
    text= "Up Daily News"
    url = 'https://google.com/search?q=' + text
    
    # Fetch the URL data using requests.get(url),
    # store it in a variable, request_result.
    request_result=requests.get( url )
    
    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
    						"html.parser")
    #print(soup)
    # soup.find.all( h3 ) to grab 
    # all major headings of our search result,
    heading_object=soup.find_all( 'h3' )
      
    # Iterate through the object 
    # and print it as a string.
    for info in heading_object:
        print(info.getText())
        print("------")

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[diviquery](https://stackoverflow.com/users/7776212)** (2023-06-24): What do you mean by keyword? Is it the value of the text variable in your code?
- **[Sanmeet](https://stackoverflow.com/users/15088809)** (2023-06-24): You could argument parser libraries out there or maybe use sys
