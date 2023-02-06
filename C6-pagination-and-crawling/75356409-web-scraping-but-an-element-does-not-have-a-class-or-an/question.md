---
title: "web scraping but an element does not have a class or an attribute"
site: stackoverflow
question_id: 75356409
url: https://stackoverflow.com/q/75356409
asked: 2023-02-06T00:17:05Z
asked_by: "noone"
asked_by_url: https://stackoverflow.com/users/21151581
last_edited: 2023-02-06T00:18:47Z
last_editor: "Michael M."
last_editor_url: https://stackoverflow.com/users/13376511
tags: [python, web-scraping, beautifulsoup]
score: -3
views_at_snapshot: 638
answer_count: 1
accepted_answer_id: 75368606
closed: 2023-02-07T00:23:26Z (Needs details or clarity)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6575d39f453bd8795d8248a334f26cf44cb96288f042481e9c5a09b32bda2fc2
---

# web scraping but an element does not have a class or an attribute

Asked by [noone](https://stackoverflow.com/users/21151581) on Stack Overflow, <https://stackoverflow.com/q/75356409>, 2023-02-06, last edited 2023-02-06 by [Michael M.](https://stackoverflow.com/users/13376511). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm new to web scraping and for my first project, I have to scrape a website that sells used cars. The main page of this website shows main details such as the name of the car, price, and km, but if I click on any of theses cars it takes me to a more detailed page where I can find other information such as the color, etc. For the main page everything is good, but on the detailed page when I inspect the page all the elements I need do not have a class or an attribute. I'm using python, BeautifulSoup. Does anyone have any solution?


```
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

# Define a list to store the information for each car
car_info = []

# Define the headers to use for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# Create a session to store the headers
session = requests.Session()
session.headers.update(headers)

# Loop through the pages with the car listings
for page_num in tqdm(range(1, 25)): # To get all cars, set the range to 266
    # Make a GET request to the URL for the current page
    url = f'https://www.automobile.tn/fr/occasion/{page_num}'
    page = session.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all the car listings on the page
    car_listings = soup.find_all("div", class_="occasion-item")

    # Loop through each car listing
    for listing in car_listings:
        # Extract the title and price of the car
        title = listing.find("h2").text.strip()
        price = listing.find("div", class_="price").text.strip()

        # Extract the KM and year of the car
        year = listing.select_one('li[class="year"]').text.strip()
        km = listing.select_one('li[class="road"]').text.strip()

        # Extract the boite information
        boite = listing.find("li", class_="boite").text.strip()

        # Find the link to the detailed page for the car
        detailed_page_link = "https://www.automobile.tn" + listing.select_one("a")["href"]

        # Make a GET request to the URL for the detailed page
        detailed_page = session.get(detailed_page_link)

        # Parse the HTML content of the detailed page
        detailed_soup = BeautifulSoup(detailed_page.content, "html.parser")

        # Extract the color, fuel, carrosserie, and puissance_fiscale information
        color = detailed_soup.find("div", class_="color").text.strip()
        fuel = detailed_soup.find("div", class_="fuel").text.strip()
        carrosserie = detailed_soup.find("div", class_="carrosserie").text.strip()
        puissance_fiscale = detailed_soup.find("div", class_="puissance_fiscale").text.strip()

        transmission = detailed_soup.find("div", class_="transmission").text.strip()

        # Add the information for the car to the list
        car_info.append((title, price, km, year, boite, color, fuel, carrosserie, puissance_fiscale))


df = pd.DataFrame(big_list, columns=['title', 'price', 'year', 'km', 'color', 'carrosserie', 'puissance_fiscale', 'boite', 'fuel', 'transmission'])
df.to_csv('various_cars.csv', index=False)
print(df)

```
this is my code everything works fine until the part of the color, fuel etc. This is the error i'm getting:
```
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_8568\2004631293.py in <module>
     51 
     52         # Extract the color, fuel, carrosserie, and puissance_fiscale information
---> 53         color = detailed_soup.select_one('div[itemprop="color"]').text.strip()
     54         fuel = detailed_soup.find("div", class_="fuel").text.strip()
     55         carrosserie = detailed_soup.find("div", class_="carrosserie").text.strip()

AttributeError: 'NoneType' object has no attribute 'text'
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Michael M.](https://stackoverflow.com/users/13376511)** (2023-02-06): Have you tried using a CSS selector?
- **[noone](https://stackoverflow.com/users/21151581)** (2023-02-06): yes but nothing seems to work..
- **[noone](https://stackoverflow.com/users/21151581)** (2023-02-06): # Extract the color, fuel, carrosserie, and puissance_fiscale information color = detailed_soup.select_one('div[itemprop="color"]').text.strip() fuel = detailed_soup.find("div", class_="fuel").text.strip() carrosserie = detailed_soup.find("div", class_="carrosserie").text.strip() puissance_fiscale = detailed_soup.find("div", class_="puissance_fiscale").text.strip() here's my trial with css selector
