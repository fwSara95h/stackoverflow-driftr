---
title: "How to detect and scrape a specific language version of a multilingual publication, if available?"
site: stackoverflow
question_id: 79578485
url: https://stackoverflow.com/q/79578485
asked: 2025-04-17T04:42:23Z
asked_by: "Mann Jain"
asked_by_url: https://stackoverflow.com/users/30295387
last_edited: 2025-04-17T20:43:47Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup, python-requests, data-science]
score: 0
views_at_snapshot: 139
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b8ecc3f3a00681c8433c7ea999303cdc97dcd04b6bf07d75a93fee41d19a0639
---

# How to detect and scrape a specific language version of a multilingual publication, if available?

Asked by [Mann Jain](https://stackoverflow.com/users/30295387) on Stack Overflow, <https://stackoverflow.com/q/79578485>, 2025-04-17, last edited 2025-04-17 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I wrote a python script for scraping data from WHO website, I wanted to retrieve Title, author name, date, pdf link and child page link from parent page (i applied some filters on parent page)
I am getting the data in CSV perfectly fine in every column but for many entries the language is getting changed to arabic or some other language even though the same thing is available in english on the website. Even the link to the pdf is redirecting to the pdf in different language even if english version is there. 

The webpage offers same information in different languages, I feel my script while sending request is fetching data in different language.

So my question is: How can I modify my script so that it gets all the data in english only?
I ***dont want to filter*** otherwise I'll lost my data. 

I want to make sure that if data is of another language, the script should find the english version of it on the webpage, because obviously it is present there.

I am attaching code below:  

```
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from http.client import RemoteDisconnected

BASE_URL = "https://iris.who.int"
PAGE_COUNT = 51  # Total pages
RPP = 100  # Results per page

# List of user-agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; rv:90.0) Gecko/20100101 Firefox/90.0",
]

session = requests.Session()

def get_with_retries(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS)
            }
            res = session.get(url, headers=headers, timeout=20)
            if res.status_code == 429:
                wait = 30 + random.randint(10, 30)
                print(f"⚠️  Rate limit hit. Waiting {wait}s...")
                time.sleep(wait)
                continue
            res.raise_for_status()
            return res
        except RemoteDisconnected:
            wait = 10 + attempt * 10
            print(f"[!] RemoteDisconnected — retrying in {wait}s...")
            time.sleep(wait)
        except requests.exceptions.RequestException as e:
            print(f"[!] Attempt {attempt + 1}/{max_retries} failed for {url}: {e}")
            time.sleep(10 * (attempt + 1))  # exponential backoff
    return None

def extract_details(item):
    # Check if language attribute is English
    lang = item.get("lang", "en")
    if lang != "en":
        return None  # Skip non-English

    title_tag = item.find("h4", class_="artifact-title")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    author_tag = item.find("span", class_="author")
    if author_tag and author_tag.get("lang") and author_tag["lang"] != "en":
        return None  # Skip if author explicitly marked non-English
    author = author_tag.get_text(strip=True) if author_tag else "N/A"

    date_tag = item.find("span", class_="govdoc-date")
    dates = date_tag.get_text(strip=True) if date_tag else "N/A"

    href = item.find("a", href=True)
    child_url = BASE_URL + href["href"] if href else "N/A"

    return title, author, dates, child_url

def extract_pdf_link(child_url):
    response = get_with_retries(child_url)
    if not response:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Prefer links that are clearly English
    pdf_links = soup.find_all("a", href=lambda x: x and ".pdf" in x)

    for link in pdf_links:
        href = link['href']
        text = link.get_text(strip=True).lower()
        if "english" in text or "en" in href:
            return BASE_URL + href

    # fallback if no clear English link
    if pdf_links:
        return BASE_URL + pdf_links[0]['href']

    return None

# Main scraping loop
data = []

for page_num in range(PAGE_COUNT):
    print(f"\n🔍 Scraping page {page_num + 1}/{PAGE_COUNT}...")
    url = f"https://iris.who.int/discover?filtertype=dateIssued&filter_relational_operator=equals&filter=2025&rpp={RPP}&page={page_num}"
    res = get_with_retries(url)
    if not res:
        print(f"[!] Skipping page {page_num + 1} due to repeated failures.")
        continue

    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select(".ds-artifact-item")

    for item in items:
        result = extract_details(item)
        if not result:
            continue  # Skip non-English

        title, author, dates, child_url = result
        pdf_link = extract_pdf_link(child_url) if child_url != "N/A" else "N/A"

        if pdf_link is None:
            continue  # Skip if no valid PDF found

        row = {
            "Title": title,
            "Author": author,
            "Dates": dates,
            "PDF_Link": pdf_link,
            "Child_Page": child_url
        }
        data.append(row)
        print(f"✅ Added: {title[:60]}...")

        time.sleep(random.uniform(2, 5))  # Random polite pause between items

    time.sleep(random.uniform(4, 8))  # Random pause between pages

# Save to file
df = pd.DataFrame(data)
df.to_csv("who_data_english_only.csv", index=False, encoding="utf-8-sig")
print(f"\n✅ Done! {len(df)} entries saved to who_data_english_only.csv")
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jsotola](https://stackoverflow.com/users/6901081)** (2025-04-17): you described the problem, but you did not ask a question ... please edit your post ... add a focused, answerable question to your post
- **[furas](https://stackoverflow.com/users/1832058)** (2025-04-17): next time you have to put starting `\`\`\`` in separated line to get highlighted code.
- **[furas](https://stackoverflow.com/users/1832058)** (2025-04-17): maybe you have to send header [Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language)
