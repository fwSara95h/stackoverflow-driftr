---
title: "I'm having issues with a python program for scraping TripAdvisor Reviews"
site: stackoverflow
question_id: 76540171
url: https://stackoverflow.com/q/76540171
asked: 2023-06-23T12:33:28Z
asked_by: "Leif Moore"
asked_by_url: https://stackoverflow.com/users/22120006
last_edited: never
tags: [python, selenium-webdriver, web-scraping, beautifulsoup, tripadvisor]
score: 0
views_at_snapshot: 660
answer_count: 1
accepted_answer_id: 76543548
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3f40455290010966d6432b57aeb46a350bd2859ec0a8439e458bd6ae1dcef8e0
---

# I'm having issues with a python program for scraping TripAdvisor Reviews

Asked by [Leif Moore](https://stackoverflow.com/users/22120006) on Stack Overflow, <https://stackoverflow.com/q/76540171>, 2023-06-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

The following python program is for scraping a selection of review data from all reviews on our trip advisor page. It isn't working and I'm unable to trouble shoot it. It doesn't iterate through the pages, so stops after the first page of reviews. The files it outputs are empty. Here is the code: 
```
import time
import json
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Define the base URL of the TripAdvisor page
base_url = "https://www.tripadvisor.co.uk/Attraction_Review-g186225-d213774-Reviews-Scudamore_s_Punting_Company-Cambridge_Cambridgeshire_England.html"

# Set the checkpoint file name
checkpoint_file = "checkpoint.txt"

# Check if the checkpoint file exists
if os.path.exists(checkpoint_file):
    # Read the checkpoint file to get the last page scraped
    with open(checkpoint_file, "r") as f:
        last_page = int(f.read().strip())
else:
    last_page = 0

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

# Launch Selenium with the configured options
driver = webdriver.Chrome(options=chrome_options)  # Replace with the path to your Chrome WebDriver

# Send a GET request to the base URL
try:
    driver.get(base_url)
    time.sleep(10)  # Wait for the page to load

    # Find and click the "Accept Cookies" button using JavaScript injection
    driver.execute_script('document.getElementById("onetrust-accept-btn-handler").click();')
    time.sleep(5)  # Wait for the cookies to be accepted

    # Get the page source after accepting cookies
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Find the total number of pages
    page_count_element = soup.find("a", class_="pageNum last")
    if page_count_element:
        page_count = int(page_count_element.text.strip())
    else:
        page_count = 1  # Set a default value if the element is not found

    # Adjust the page count based on the last page scraped
    page_count -= last_page

    # Create a list to store the extracted review data
    review_data = []

    # Iterate over each page
    for page in range(last_page + 1, last_page + page_count + 1):
        # Construct the URL for the current page
        url = f"{base_url[:-5]}-or{page * 10}-{base_url[-5:]}"

        # Send a GET request to the URL
        driver.get(url)
        time.sleep(10)  # Wait for the page to load

        # Get the page source
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Find all the review elements on the current page
        review_elements = soup.select("#tab-data-qa-reviews-0 > div > div.LbPSX > div > div")

        # Iterate over each review element and extract relevant information
        for review in review_elements:
            try:
                # Extract the reviewer's name
                reviewer_name_elem = review.select_one(".ZVAUHZqh > span > a")
                reviewer_name = reviewer_name_elem.text.strip() if reviewer_name_elem else ""

                # Extract the rating
                rating_elem = review.select_one(".nf9vGX55")
                rating = float(rating_elem["title"].split()[0]) / 10 if rating_elem else 0.0

                # Extract the title
                title_elem = review.select_one("a._1r_My98y > span")
                title = title_elem.text.strip() if title_elem else ""

                # Extract the review text
                review_text_elem = review.select_one("div._1o6B68z4 > div")
                review_text = review_text_elem.text.strip() if review_text_elem else ""

                # Extract the review date
                review_date_elem = review.select_one("div._1OuugO9R")
                review_date = review_date_elem.text.strip() if review_date_elem else ""

                # Create a dictionary to store the review data
                review_info = {
                    "Reviewer Name": reviewer_name,
                    "Rating": rating,
                    "Title": title,
                    "Review Text": review_text,
                    "Review Date": review_date
                }

                # Add the review data to the list
                review_data.append(review_info)

            except Exception as e:
                print("An error occurred while extracting review data:", str(e))

    # Save the checkpoint for the last page scraped
    with open(checkpoint_file, "w") as f:
        f.write(str(last_page + page_count))

    # Close the Selenium driver
    driver.quit()

    # Save the review data to a JSON file
    with open("reviews.json", "w", encoding="utf-8") as json_file:
        json.dump(review_data, json_file, ensure_ascii=False, indent=4)

    # Save the review data to a CSV file
    with open("reviews.csv", "w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["Reviewer Name", "Rating", "Title", "Review Text", "Review Date"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(review_data)

    # Save the review text to a TXT file
    with open("reviews.txt", "w", encoding="utf-8") as txt_file:
        for review in review_data:
            txt_file.write(review["Review Text"] + "\n")

    print("Scraping completed successfully!")
except Exception as e:
    print("An error occurred during scraping:", str(e))
    driver.quit()

```


I've tried using requests but wasn't happy with the results. I've gone over the selectors trying html, css and xpath selectors to grab the data I want to scrape. I've changed output types. I've tried throttling the requests so it doesn't trigger anti-scraping security on TripAdvisor. I've tried a fair few things. Happy to discuss.

Over all I'm hoping the program will scrape all of the review fields I've defined into a file. there are over 1000 reviews and the program I created would populate the json with the review fields I specified for the first pages reviews however the fields have no data in them. I'm very open to suggestions at this point.
