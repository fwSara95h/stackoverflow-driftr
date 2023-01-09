---
title: "Getting empty list after running scaping code in python to get reviews of users from play store of my app"
site: stackoverflow
question_id: 75054860
url: https://stackoverflow.com/q/75054860
asked: 2023-01-09T08:46:11Z
asked_by: "Tushar Patki"
asked_by_url: https://stackoverflow.com/users/19408055
last_edited: never
tags: [python, web-scraping, beautifulsoup, request]
score: -1
views_at_snapshot: 54
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9719d8854e3b819d81eae401edd3829030bc371cf6394a06da2cfec2c9af7b58
---

# Getting empty list after running scaping code in python to get reviews of users from play store of my app

Asked by [Tushar Patki](https://stackoverflow.com/users/19408055) on Stack Overflow, <https://stackoverflow.com/q/75054860>, 2023-01-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
import requests
from bs4 import BeautifulSoup

# Send a GET request to the web page
response = requests.get('https://play.google.com/store/apps/details?id=com.example.app&reviewSortOrder=4&reviewType=0')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the review divs
review_divs = soup.find_all('div', class_='single-review')

# Extract the review data from each review div
reviews = []
for review_div in review_divs:
    # Extract the review text
    review_text = review_div.find('span', class_='review-body').text
    # Extract the reviewer's name
    reviewer_name = review_div.find('span', class_='author-name').text
    # Extract the review rating
    review_rating = review_div.find('div', class_='tiny-star').get('aria-label').split(' ')[1]
    
    # Store the review data in a dictionary
    review = {
        'review_text': review_text,
        'reviewer_name': reviewer_name,
        'review_rating': review_rating
    }
    
    # Add the review dictionary to the list of reviews
    reviews.append(review)

print(reviews)

```


I wrote this code to scrap reviews of my app from Playstore in tabular format. However, I am only getting empty block after running this code, I am not able to identify where I am making error in this code to get.Results I am expecting are list of all of the reviews of my app users.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Samuel](https://stackoverflow.com/users/14923551)** (2023-01-09): Print your status, see what it returns `print(response.status_code)`
