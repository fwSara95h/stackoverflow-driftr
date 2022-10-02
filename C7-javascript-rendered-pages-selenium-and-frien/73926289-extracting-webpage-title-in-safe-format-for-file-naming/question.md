---
title: "Extracting Webpage Title in Safe Format for File Naming"
site: stackoverflow
question_id: 73926289
url: https://stackoverflow.com/q/73926289
asked: 2022-10-02T13:42:05Z
asked_by: "pglove"
asked_by_url: https://stackoverflow.com/users/1485503
last_edited: 2022-10-02T15:53:55Z
tags: [python, selenium, web-scraping, beautifulsoup, automation]
score: 1
views_at_snapshot: 219
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bb010a98bb2a6d04b95cefe726721814d079edee763280d6b2f6edacf1b2e1c1
---

# Extracting Webpage Title in Safe Format for File Naming

Asked by [pglove](https://stackoverflow.com/users/1485503) on Stack Overflow, <https://stackoverflow.com/q/73926289>, 2022-10-02, last edited 2022-10-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Using Python I'd like to scrape some information from a webpage and save the info to a .txt file named using the title of the page scraped.

Unfortunately many pages contain special characters that can't be used in file names, so ideally I want to extract the title you would get if you did file/save from a browser.

Is it possible to achieve this with BeautifulSoup or Selenium?

I can get the page title with soup, and then clean it, but if there is a more efficient way of getting the browser-cleaned title I'd love to know how.

EDIT:

So far I have achieved a workable result with the following code. I used YouTube as an example but really would prefer an all-purpose page-title retrieval in browser save format if possible. Probably doesn't exist, but there's always hope.

    import re
    import mechanize
    
    br = mechanize.Browser()
    br.open("https://www.youtube.com/watch?v=RvCBzhhydNk")
    
    title = re.sub('[^A-Za-z0-9]+', ' ', br.title().replace("YouTube", "")).strip()
    
    print(title)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[AbiSaran](https://stackoverflow.com/users/7671727)** (2022-10-02): Selenium does not have that feature, you have to get the title, then write simple logic to avoid the special characters or change the special characters to something else.
- **[Rivered](https://stackoverflow.com/users/9536233)** (2022-10-02): Having an example website and target would be very useful.
- **me** (2022-10-03): ...you could use something like [uipath](https://dev.tutorialspoint.com/uipath/uipath_studio_recording.htm#) to have it nearly save a page and get the name, but that would be an insanely convoluted and inefficient process just to get a name
