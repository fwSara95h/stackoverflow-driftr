---
title: "How do I webscrape tables onto two different Sheets on the Excel Spreadsheet?"
site: stackoverflow
question_id: 75915842
url: https://stackoverflow.com/q/75915842
asked: 2023-04-03T03:29:39Z
asked_by: "NNBananas"
asked_by_url: https://stackoverflow.com/users/19672894
last_edited: never
tags: [python, excel, web-scraping, beautifulsoup, playwright-python]
score: 0
views_at_snapshot: 34
answer_count: 1
accepted_answer_id: 75916413
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 78f6f3a6a9bab0ef1879913d9ead686807923a53968bed3be2c17064d6c8f4e3
---

# How do I webscrape tables onto two different Sheets on the Excel Spreadsheet?

Asked by [NNBananas](https://stackoverflow.com/users/19672894) on Stack Overflow, <https://stackoverflow.com/q/75915842>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

This is my code that webscrapes the table from these two links. It doesn't crash.
"https://racing.hkjc.com/racing/information/English/Jockey/JockeyRanking.aspx" 
"https://racing.hkjc.com/racing/information/English/Trainers/TrainerRanking.aspx"

However, when I run it, the two tables seem to overlap each other and print on the same sheet rather than different sheets. Is there a way to fix this?

```
import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrape_ranking(url, sheet_name):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        soup = BeautifulSoup(page.content(), "html.parser")
        table = soup.select_one(".table_bd")

        if table is None:
            print("Table not found.")
        else:
            df = pd.read_html(str(table))[0]
            df.to_excel("hkjc.xlsx", sheet_name=sheet_name, index=True)

# Scrape TrainerRanking page
url_trainer = "https://racing.hkjc.com/racing/information/English/Trainers/TrainerRanking.aspx"
scrape_ranking(url_trainer, "TrainerRanking")

# Scrape JockeyRanking page
url_jockey = "https://racing.hkjc.com/racing/information/English/Jockey/JockeyRanking.aspx"
scrape_ranking(url_jockey, "JockeyRanking")

print("done")

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-04-03): Is that same sheet `JockeyRanking`? Do the dfs really get combined or does only the last one remain?
