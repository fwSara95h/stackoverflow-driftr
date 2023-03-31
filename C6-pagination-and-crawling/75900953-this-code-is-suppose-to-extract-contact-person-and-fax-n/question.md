---
title: "This code is suppose to extract contact person and fax number looks okay but does not work"
site: stackoverflow
question_id: 75900953
url: https://stackoverflow.com/q/75900953
asked: 2023-03-31T16:54:16Z
asked_by: "Life Unexplained"
asked_by_url: https://stackoverflow.com/users/19809700
last_edited: 2023-03-31T17:24:21Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, web-scraping, beautifulsoup, bots]
score: 0
views_at_snapshot: 50
answer_count: 2
accepted_answer_id: none
closed: 2023-03-31T20:58:23Z (Not suitable for this site)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: af68eb13fc818f685a613331326f56cb093d8b4bf3f1ed4c6d9764e3179c820d
---

# This code is suppose to extract contact person and fax number looks okay but does not work

Asked by [Life Unexplained](https://stackoverflow.com/users/19809700) on Stack Overflow, <https://stackoverflow.com/q/75900953>, 2023-03-31, last edited 2023-03-31 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

The result is this (but there are results on the site)
> ```py
> Contact Person: None
> Fax Number: None
> Contact Person: None.
> ```


```py
import requests
from bs4 import BeautifulSoup


def get_contact_person_and_fax_number(url):
    # Send GET request to link url
    link_response = requests.get(url)

    # Parse HTML content with BeautifulSoup
    link_soup = BeautifulSoup(link_response.content, "html.parser")

    # Find the contact person and fax number
    contact_person = None
    fax_number = None
    contact_div = link_soup.find("div", {"class": "info-gen-box clearfix"})
    if contact_div:
        contact_person = contact_div.find("div", {"class": "info-gen-box clearfix"})
        if contact_person:
            contact_person = contact_person.text.strip()
        fax_number = contact_div.find("div", {"class": "info-fax info-mar"})
        if fax_number:
            fax_number = fax_number.text.strip()

    return (contact_person, fax_number)


# Prompt user for NAICS code
naics_code = input("Enter NAICS code: ")

# Loop through all search result pages
for page_num in range(1, 81):
    # Send GET request to search page
    page_url = f"https://www.usaopps.com/government_contractors/search.htm?naics={naics_code}&page={page_num}"
    page_response = requests.get(page_url)

    # Parse HTML content with BeautifulSoup
    page_soup = BeautifulSoup(page_response.content, "html.parser")

    # Find all search results on current page
    results = page_soup.select(".lr-title")
    links = page_soup.find_all('div', {'class': 'lr-title'})

    # Loop through each search result link and extract contact person and fax number if available
    for link in links:
        # Extract link url
        url = link.find('a').get('href')

        if not url.startswith('http'):
            url = f"https://www.usaopps.com{url}"

        # Get contact person and fax number for this link
        contact_person, fax_number = get_contact_person_and_fax_number(url)

        # Print results
        print(f"Contact Person: {contact_person}")
        print(f"Fax Number: {fax_number}")
```
