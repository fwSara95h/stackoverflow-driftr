---
title: "I randomly get no output at <h1> and <Li> when scraping with beautifulsoup"
site: stackoverflow
question_id: 74136536
url: https://stackoverflow.com/q/74136536
asked: 2022-10-20T08:17:21Z
asked_by: "flexyflash"
asked_by_url: https://stackoverflow.com/users/20110941
last_edited: 2022-10-20T08:19:39Z
last_editor: "baduker"
last_editor_url: https://stackoverflow.com/users/6106791
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 61
answer_count: 1
accepted_answer_id: 74146125
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 764d818f64fb53e3e6987729139f192c091190e4a88d37b30e76ce871f1265b2
---

# I randomly get no output at <h1> and <Li> when scraping with beautifulsoup

Asked by [flexyflash](https://stackoverflow.com/users/20110941) on Stack Overflow, <https://stackoverflow.com/q/74136536>, 2022-10-20, last edited 2022-10-20 by [baduker](https://stackoverflow.com/users/6106791). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

    from urllib import response
    from bs4 import BeautifulSoup
    import requests
    import csv
    
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    # }
    
    csv_file = open("scifi_audible.csv", "w")
    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["title ", "link ", "rating ", "reviews "])
    
    url = "https://www.audible.de/"
    
    audiobooklinks = []
    
    for x in range(1, 2):
        source = requests.get(f"https://www.audible.de/search?node=16245852031&page={x}")
        soup = BeautifulSoup(source.content, "lxml")
    
        audiobooks = soup.find_all("h3", class_ = "bc-heading")
        for item in audiobooks:
            for link in item.find_all("a", href=True):
                audiobooklinks.append(url + link["href"])
    
    
    #testlink = 'https://www.audible.de/pd/Mortarion-The-Pale-King-Hoerbuch/B0BCQXVJML'
    
    for link in audiobooklinks:
        r = requests.get(link) #headers=headers)
    
        soup = BeautifulSoup(r.content, "lxml")
        
        try:
            title = soup.find("h1", class_= "bc-heading").text.strip()
        except:
            title = "no output possible"
    
        try:
            rating = soup.find("span", attrs={"aria-hidden":"true", "class":"bc-text"}).text.strip()
        except:
            rating = "no rating"
    
        try:
            raw_reviews = soup.find("li", class_= "bc-list-item ratingsLabel").text.strip()
        except:
            raw_reviews = "no raw_reviews"
    
        try:
            reviews = raw_reviews.split("(")[-1].split()[0].replace(".", "")
        except:
            reviews = "no reviews"
    
        print(title, link, rating, reviews)
    
        csv_writer.writerow([title, link, rating, reviews])
        
    csv_file.close()


Most of the time it works. Randomly it is printed i.e. like this:

"no output possible https://www.audible.de//pd/Mortarion-The-Pale-King-Hoerbuch/B0BCQXVJML no rating no"


What do I have to change to always get the h1 and li?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-10-20): Is that url behind a login?
- **[flexyflash](https://stackoverflow.com/users/20110941)** (2022-10-20): No, the html can be accessed without a login
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-10-20): I’m voting to close this question because, code works fine, behavior is not reproducible and question may need some more details to clarify.
- **me** (2022-10-20): @HedgeHog - I am able to reproduce the behavior - they did say it doesn't happen *most* of the time
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-10-20): @Driftr95 Noticed the *it doesn't happen most of the time* in my opinion it still needs more details. Feel free to light us up with additional information.
- **me** (2022-10-20): @HedgeHog It's usually a 503 error - I've suggested a solution for it, though I  don't have any explanation for the 200-OK-but-empty-content scenario...
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-10-21): @Driftr95 - That would have been the information I would have expected from the question, thank you very much for that. On what basis does your figure of 2% refer? It would be interesting because even with the 1000 requests I used for testing (delayed and non-delayed), not one ran into this error.
- **me** (2022-10-21): @HedgeHog I also ran 1k requests [50x20] - 17 got 503 and 2 had 200 ok but empty content. I wonder if the location or user's internet conditions can have anything to do with it?
- **me** (2022-10-21): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/248956/discussion-between-driftr95-and-hedgehog).
