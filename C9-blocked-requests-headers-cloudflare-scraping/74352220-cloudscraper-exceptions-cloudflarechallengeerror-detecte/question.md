---
title: "cloudscraper.exceptions.CloudflareChallengeError: Detected a Cloudflare version 2 Captcha challenge"
site: stackoverflow
question_id: 74352220
url: https://stackoverflow.com/q/74352220
asked: 2022-11-07T19:53:42Z
asked_by: "Lun"
asked_by_url: https://stackoverflow.com/users/16424940
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-requests]
score: -1
views_at_snapshot: 7969
answer_count: 1
accepted_answer_id: 74357110
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ff2698407c05340138ef7f73cdcb64f966c0fe3d92a1f394ae6d82aa07b602b
---

# cloudscraper.exceptions.CloudflareChallengeError: Detected a Cloudflare version 2 Captcha challenge

Asked by [Lun](https://stackoverflow.com/users/16424940) on Stack Overflow, <https://stackoverflow.com/q/74352220>, 2022-11-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

### Main.py ###

    import cloudscraper
    
    scraper = cloudscraper.create_scraper()
    cs_recent_page = scraper.get('https://coinsniper.net/new').text

### Error ###
`cloudscraper.exceptions.CloudflareChallengeError: Detected a Cloudflare version 2 Captcha challenge, This feature is not available in the opensource (free) version.`

I'm trying to access this site in order to scrape data off of it, but it uses cloudfare protection, so I found this solution but keep getting this error, is there another way to access this site?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[αԋɱҽԃ αмєяιcαη](https://stackoverflow.com/users/7658985)** (2022-11-07): Bypassing CloudFlare require a deep knowledge of reversing JS in order to mimic the Requests, Otherwise you've to use a headless browser such as Playwright/Selenium or whatever framework to collect the hCaptcha sitekey and send it to service like 2Captcha or Anti-Captcha and then inject the response and continue. Both of that require different techniques. otherwise if you can't do that, then you can subscribe for solver such as cloudscraper
