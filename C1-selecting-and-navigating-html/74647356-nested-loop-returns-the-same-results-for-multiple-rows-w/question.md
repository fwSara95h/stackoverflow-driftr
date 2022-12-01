---
title: "nested loop returns the same results for multiple rows while webscraping - beautiful soup"
site: stackoverflow
question_id: 74647356
url: https://stackoverflow.com/q/74647356
asked: 2022-12-01T19:42:24Z
asked_by: "user15564501"
asked_by_url: (account no longer exists)
last_edited: 2022-12-01T21:00:14Z
last_editor: "Andrej Kesely"
last_editor_url: https://stackoverflow.com/users/10035985
tags: [python, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 126
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4d6ef09103ecbc5917a5597b9a219a9dacfd83b15415a320e99945c043a29092
---

# nested loop returns the same results for multiple rows while webscraping - beautiful soup

Asked by user15564501 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/74647356>, 2022-12-01, last edited 2022-12-01 by [Andrej Kesely](https://stackoverflow.com/users/10035985). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape an apartment website and it's not looping. I get  different apartments but the rest of the information is the same. Yesterday it was pulling a different address.


```
url = "https://www.apartments.com/atlanta-ga/?bb=lnwszyjy-H4lu8uqH"
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('section', class_="placard-content")
properties = soup.find_all('li', class_="mortar-wrapper")
addresses = soup.find_all('a', class_="property-link")

for list in lists:
    price = list.find('p', class_="property-pricing").text
    beds = list.find('p', class_="property-beds").text
    for address in addresses:
        location = address.find('div', class_="property-address js-url").text
        for property in properties:
            name = property.find('span', class_="js-placardTitle title").text
            info = [name,location,beds,price]
            print(info)```


Here is the output I'm getting
```
['Broadstone Pullman', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['1660 Peachtree Midtown', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['Mira at Midtown Union', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['Alexan Summerhill', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['1824 Defoor', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['3005 Buckhead', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['AMLI Westside', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['Novel O4W', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['The Cliftwood', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']
['Ellington Midtown', '105 Rogers St NE, Atlanta, GA 30317', 'Studio - 2 Beds', '$1,630 - 2,825']```
