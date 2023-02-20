---
title: "Imaged returned as base64 encoded string when scraping news article"
site: stackoverflow
question_id: 75512759
url: https://stackoverflow.com/q/75512759
asked: 2023-02-20T18:07:05Z
asked_by: "Cian Sullivan"
asked_by_url: https://stackoverflow.com/users/17474072
last_edited: 2023-07-27T09:50:23Z
last_editor: "Brian Tompsett - 汤莱恩"
last_editor_url: https://stackoverflow.com/users/4370109
tags: [python, beautifulsoup, base64]
score: 0
views_at_snapshot: 174
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f5d87b4bd8d8a578912f1eedae2d6dbd5187448d2b8c6c78a10c6bf438c1897b
---

# Imaged returned as base64 encoded string when scraping news article

Asked by [Cian Sullivan](https://stackoverflow.com/users/17474072) on Stack Overflow, <https://stackoverflow.com/q/75512759>, 2023-02-20, last edited 2023-07-27 by [Brian Tompsett - 汤莱恩](https://stackoverflow.com/users/4370109). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am new to scraping data and I am trying to extract the following image from a news article:

    <img alt="Preparing for the NBA's Victor Wembanyama revolution" class="" data-mptype="image" src="https://a.espncdn.com/photo/2023/0218/r1133272_1296x518_5-2.jpg">

Here the image tag seems to show up as a real link to a photo which I can see on my browser. However, when I try to extract this data using BeautifulSoup I am returned a base64 encoded string: 
> ("data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)"

 I have not been able to figure out how to do anything with this string as I can't display it on my web page like I want to.

Any help would be greatly appreciated. 

Here is the script I have wrote to extract the data from the web page.

```py
def scrape_news(request):
    team = request.GET.get('team')
    hide_names = request.GET.get('hide_names') == 'true'


    # Set the URL of the ESPN.com page that contains the team's news
    url = f'https://www.espn.com/nba/team/_/name/{team}'

    # Send a GET request to the URL and parse the response with BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the news articles on the page
    news_articles = soup.find_all('article', {'class': 'contentItem'})

    # Create a list to store the news articles
    articles_list = []

    # Loop through each news article and extract the relevant information
    for article in news_articles:
        team_heading = soup.find('title').text.split('-')[0].strip()

        latest_article = article.find('a', class_='contentItem__content')
        
        # Check if latest_article is not None
        if latest_article is not None:
            headline = latest_article.find('h2', class_='contentItem__title').text.strip()
            link = latest_article['href']
            img = latest_article['src']

            # check image
            print(img) # prints encoded string


            # Create a dictionary for the current article
            article_dict = {
                'team_heading': team_heading,
                'headline': headline,
                'link': link,
                'hide_names': hide_names
            }

            # Add the article dictionary to the list
            articles_list.append(article_dict)

    # Render the template with the news articles
    return render(request, 'scrape_news.html', {'articles_list': articles_list})
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[JonSG](https://stackoverflow.com/users/218663)** (2023-02-20): That base64 image looks like it is a placeholder/default that gets updated via javascript
- **[Mark Setchell](https://stackoverflow.com/users/2836621)** (2023-02-20): Do you mean you want to put the base64 image into your `scrape_news.html` template? If so, you can add an `<img>` element with that base64 string as its `src`.
