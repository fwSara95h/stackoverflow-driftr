---
title: "What is going on? (Attemp at scraping multiple pages)"
site: stackoverflow
question_id: 74411153
url: https://stackoverflow.com/q/74411153
asked: 2022-11-12T07:33:55Z
asked_by: "Jack9992"
asked_by_url: https://stackoverflow.com/users/20483330
last_edited: 2022-11-12T09:39:06Z
tags: [python, web-scraping, beautifulsoup, screen-scraping]
score: 1
views_at_snapshot: 125
answer_count: 2
accepted_answer_id: 74411346
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b5a69ee6db171c495391e08f2ab4dd6f8c2e15e1ea1e5e5775d1274ba42976d6
---

# What is going on? (Attemp at scraping multiple pages)

Asked by [Jack9992](https://stackoverflow.com/users/20483330) on Stack Overflow, <https://stackoverflow.com/q/74411153>, 2022-11-12, last edited 2022-11-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
url = "https://www.gumtree.com/search?search_category=all&q=ferrari"

while url:

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find_all("div", class_="h3-responsive")

    price = soup.find_all("strong", "h3-responsive")

    next_page = soup.select_one("li.pagination-page>a")

    for price,name in zip(name,price):
        print(name.text,price.text)

    if next_page:
        next_url = next_page.get("href")
        url = urljoin(url,next_url)
    else:
        url = None
```

Nothing is printing for some reason? I've had it running for 5 minutes and still nothing. I've had no error code either so I'm geuinely confused here? If anyone would like to fix this script please do so, if you didn't realize the script is supposed to scrape the name & price as well as every other page/s name and price.

If someone could please re-do the script, and make it also scrape all the other pages, because I have been having a hard time figuring out how to do this.

I've taken some suggestions in and done some editing but the script still won't work.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-12): Is this your script? Did you write it?
- **me** (2022-11-12): It's not printing anything because it's not finding anything, and it's not stopping because you've got an infinite loop going on currently which is attempting to scrape the same page over and over. Shift the `if next_page:` block to inside the while, add an `else: url=None` [after the `if` block], and change to `while url` instead of `while True` so if stops when it can't find a next page
- **[Jack9992](https://stackoverflow.com/users/20483330)** (2022-11-12): yes I wrote this. It won't scrap all of the other pages though.
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-12): The script below will work if your IP was not already blacklisted by Cloudfront, given you ran that infinite loop a few times. Let me know how it works for you (eventually use a VPN).
- **[Jack9992](https://stackoverflow.com/users/20483330)** (2022-11-12): I'm pretty sure the script works, but now my ip is blacklisted because I had that while loop running for over an hour. I'm such an idiot lmao, anyways. Thank you all so much guys! Big thanks to everyone!
- **[Jack9992](https://stackoverflow.com/users/20483330)** (2022-11-12): Hey @Driftr95 I tried the script on a new IP address and nothing prints again? Do you know the problem? Script is here: https://pastebin.com/V057zv3a
