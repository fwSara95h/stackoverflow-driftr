---
title: "Scraping what's inside the links"
site: stackoverflow
question_id: 74420235
answer_id: 74497640
url: https://stackoverflow.com/a/74497640
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-19T04:55:25Z
last_edited: 2022-11-19T05:02:19Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74497640/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [crawler output, linkToSoup, queue crawler (saveScrawlSess), recursive crawler, saveScrawlSess]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: edeb88e17a8e772232d29e478874761a763a8fef058218c15df75e910c23b96a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74497640>, 2022-11-19, last edited 2022-11-19; score 0. Text as retrieved 2026-10-12.

> scrape the website, and what is inside the links at the same time

Assuming that you mean you want to scrape all the pages that the links on the site lead to, I have [this recursive crawler](https://pastebin.com/AeN4BFv5) which should be able to do it. Just calling `linkTreeMapper('https://www.bleepingcomputer.com/', None, 1)` gave an output [like this](https://pastebin.com/r6zjJVLM); the fuction was actually meant to go further, like `linkTreeMapper('https://www.bleepingcomputer.com/', pageLimit=2)` would return
```json
{
    "url": "https://www.bleepingcomputer.com/",
    "atDepth": 0,
    "pageTitle": "BleepingComputer | Cybersecurity, Technology News and Support",
    "pageBodyText": "News Featured Latest US govt: Iranian hackers br...n in with Twitter Not a member yet? Register Now",
    "pageUrls": [
        {
            "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
            "atDepth": 1,
            "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
            "pageUrls": [
                {
                    "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                    "atDepth": 2,
                    "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
                    "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
                    "pageUrls": [
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                            "atDepth": 3,
                            "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        },
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                            "atDepth": 3,
                            "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        }
                    ]
                },
                {
                    "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                    "atDepth": 2,
                    "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                    "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
                    "pageUrls": [
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                            "atDepth": 3,
                            "errorMessage": "Message: timeout: Timed out receiving message from renderer: -0.009\n  (Session info: chrome=107.0.5304.88)\n"
                        },
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                            "atDepth": 3,
                            "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        }
                    ]
                }
            ]
        },
        {
            "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
            "atDepth": 1,
            "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
            "pageUrls": [
                {
                    "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                    "atDepth": 2,
                    "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
                    "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
                    "pageUrls": [
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                            "atDepth": 3,
                            "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        },
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                            "atDepth": 3,
                            "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...SUBMIT advertisement advertisement advertisement"
                        }
                    ]
                },
                {
                    "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                    "atDepth": 2,
                    "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                    "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT",
                    "pageUrls": [
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/",
                            "atDepth": 3,
                            "pageTitle": "US govt: Iranian hackers breached federal agency using Log4Shell exploit",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        },
                        {
                            "url": "https://www.bleepingcomputer.com/news/security/google-to-roll-out-privacy-sandbox-on-android-13-starting-early-2023/",
                            "atDepth": 3,
                            "pageTitle": "Google to roll out Privacy Sandbox on Android 13 starting early 2023",
                            "pageBodyText": "News Featured Latest US govt: Iranian hackers br...what content is prohibited. Submitting... SUBMIT"
                        }
                    ]
                }
            ]
        }
    ]
}
```
(I set `pageLimit=2` so that the output would be small enough to view here)

---

However, using recursion can be dangerous in cases like these, and as you can see, it's harder to eliminate repeated scrawling of the same page; so, it might be better to use [this queue-based scrawler](https://pastebin.com/TBtYja5D)
```python
## FIRST COPY [OR DOWNLOAD&IMPORT] REQUIREMENTS FROM https://pastebin.com/TBtYja5D ##
setGlobals(varDict={
    'starterUrl': 'https://www.bleepingcomputer.com/', 
    'pageLimit': None, 'maxScrapes': 55, 'scrapeCt': 0, 'curUrlId': 0
}, clearLog=True)
nextUrl = get_next_fromScrawlQ()
while nextUrl: nextUrl = logScrape(scrapeUrl(nextUrl))
saveScrawlSess('qScrawl_bleepingComp.csv', 'vScrawl_bleepC.json')
```
and "qScrawl_bleepingComp.csv" would look like 

|url|refUrlId|status|urlId|pageTitle|pageText|pageUrlCt|newToQueue|
|---|---|---|---|---|---|---|---|
|https://www\.bleepingcomputer\.com/|\[starter\]|scraped|1|BleepingComputer &#124; Cybersecurity, Technology News and Support|News Featured Latest Exploit rele\.\.\.er Not a member yet? Register Now|237\.0|129\.0|
|https://www\.facebook\.com/BleepingComputer|1|?scraped|2|BleepingComputer &#124; New York NY|NaN|0\.0|0\.0|
|https://twitter\.com/BleepinComputer|1|scraped|3|NaN|JavaScript is not available\. We’v\.\.\.ret — let’s give it another shot\.|6\.0|6\.0|
|https://www\.youtube\.com/user/BleepingComputer|1|?scraped|4|YouTube|BleepingComputer - YouTube|0\.0|0\.0|
|https://www\.bleepingcomputer\.com/news/security/exploit-released-for-actively-abused-proxynotshell-exchange-bug/|1|scraped|5|Exploit released for actively abused ProxyNotShell Exchange bug|News Featured Latest Exploit rele\.\.\. prohibited\. Submitting\.\.\. SUBMIT|148\.0|26\.0|

(Only the first five rows [of 1.6k+] are above, and the last 2 columns have not been included - [see uploaded csv for full output](https://docs.google.com/spreadsheets/d/1ybRW-cL3qXGMatzjVr_M8_6nZ5uZ6CjJ28vRKAidNHE/edit?usp=sharing).)

The "pageUrlIds" columns has a list of numbers, each of which should correspond to a row according to the "urlId" column; so, if you wanted to, you could use that to form a nested dictionary like the output of the recursive crawler.

---

> Is this possible for just BeautifulSoup and the Requests library?

For some sites, it might be - both of my crawlers use a `linkToSoup` function [to fetch and parse the html of each page], and I have several versions of it; the simple `requests` version didn't work for bleepingcomputer, so I used [cloudscraper](https://pypi.org/project/cloudscraper/). However, I'm not skilled with setting headers for requests [beyond the the very basics], so someone else may have be able to figure out the perfect set of parameters...
