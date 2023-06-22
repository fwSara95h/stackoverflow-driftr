---
title: "how to extract the texts after the first h1 Tag?"
site: stackoverflow
question_id: 76530572
answer_id: 76532726
url: https://stackoverflow.com/a/76532726
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-22T14:01:22Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76532726/revisions
accepted: true
score: 1
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e20347787e3a81eaf17c9027472c4e4d004cee055da057148b5744bc64e313e9
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76532726>, 2023-06-22; **accepted**; score 1. Text as retrieved 2026-10-12.

You had the right idea in trying to use [`.next_siblings`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#next-siblings-and-previous-siblings), but you should keep in mind that ***`soup.next_siblings`* is unlikely to generate anything** as the document itself is generally not expected to have any siblings.

---

The following code finds the first header and then [if it doesn't have any siblings], searches up the its parents to find the nearest one with siblings and then goes through the siblings but stops if another `h1` tag is reached.

```py
# list_of_urls = ['https://economictimes.indiatimes.com/...
# for url in list_of_urls:
    # response = requests.get(url,.....
    # soup = BeautifulSoup(response.content, 'html.parser')

    header1 = soup.find('h1')
    if not header1:
        print(f'[{response.status_code} {response.reason}] No headers at', url)
        continue
    
    if header1.next_sibling: hSibs = header1.next_siblings
    else:
        hParent = next((p for p in header1.parents if p.next_sibling), None)
        hSibs = hParent.next_siblings if hParent else []
    
    h1Sibs = []
    for ns in hSibs:
        if ns.name == 'h1' or (not isinstance(ns,str) and ns.find('h1')): break
        h1Sibs.append(ns)
    h1Sibs_text = '\n---\n'.join(ns.get_text(' ') for ns in h1Sibs)
```

for the site in your example, <kbd>`print(h1Sibs_text)`</kbd> should print

> ```lang-none
> SECTIONS Volkswagen sets 5-7% revenue growth target, preaches cost discipline Reuters Last Updated: Jun 21, 2023, 07:16 PM IST Rate Story Share Font Size Abc Small Abc Medium Abc Large Save Print Comment
> ---
> Synopsis The German carmaker has set "performance programmes" for each brand, allocating them capital and setting a specific return on sales target, but delegating responsibility to the brands for how those targets are reached, executives said in a press call on its Capital Markets Day. "If you look at how Volkswagen operated in the past, often we had a fixed cost growth and we wanted to outgrow that fixed cost," Chief Financial Officer Arno Antlitz said. Agencies Volkswagen sets 5-7% revenue growth target, preaches cost discipline Volkswagen  set new financial targets on Wednesday of 5-7% annual  revenue  growth by 2027 and 9-11% returns by 2030, aiming to stay disciplined on investment and focus on boosting margins in the face of growing competition for market share.  The German carmaker has set "performance programmes" for each brand, allocating them  capital  and setting a specific return on sales target, but delegating responsibility to the  brands  for how those targets are reached, executives said in a press call on its  Capital Markets Day .  "If you look at how Volkswagen operated in the past, often we had a fixed cost growth and we wanted to outgrow that fixed cost," Chief Financial Officer  Arno Antlitz  said.  "We are convinced in the transformation we need to change that strategy to our value over volume approach, be very disciplined on fixed cost, be very disciplined on investment and rather focus on value," he added.  In  China , where internal combustion engine sales still provide high revenues for the carmaker, it has slightly reduced its target for battery-electric vehicle sales in the next 1-2 years and is instead focused on protecting margins,  Antlitz  said.  The new revenue growth target is a marked jump from Volkswagen's performance in recent years, with revenue growing just 1.1-1.2% per year in the last two years, and 0.7% in 2018-2019 prior to the pandemic.  Under the new performance programmes, each brand will have a set target for operating result, returns, net cash flow, cash conversion rate, and investment ratio, Volkswagen said in a statement, adding it would tie management incentives to meeting targets.  The carmaker is planning separate capital markets days for each brand over the coming months to introduce those targets, sources close to the company told Reuters last Friday. Don’t miss out on ET Prime stories! Get your daily dose of business updates on WhatsApp.  click here! Thursday, 22 Jun, 2023 Experience Your Economic Times Newspaper, The Digital Way! Read Complete Print Edition  » Front Page Pure Politics ET Markets Smart Investing More Local Indices End at Record Peaks on HDFC, IT Gains India’s key stock benchmarks closed at record highs amid choppy trade on Wednesday, bucking the bearish mood in other Asian markets, as merger-bound HDFC Bank and HDFC, as well as software shares, paced the gains. Musk Meets Modi, Says Tesla to be in India Soon Tesla founder Elon Musk said he had a very good conversation with Prime Minister Narendra Modi and he is confident the company, the world’s largest electric carmaker, will be in India “as soon as humanly possible” and that it is likely to make a “significant investment” in the country. ZEE-Sony Deal on, Whether I’m CEO or Not Punit Goenka, CEO & MD of Zee Entertainment Enterprises, has said that the ZEE-Sony merger will go through whether or not he is the CEO of the merged company, as it benefits 96% of stakeholders. Read More News on volkswagen Capital Market Brands Capital Revenue antlitz arno antlitz capital markets day china (Catch all the  Business News ,  Breaking News  Events and  Latest News  Updates on  The Economic Times .) Download  The Economic Times News App  to get Daily Market Updates & Live Business News. ... more less ETPrime stories of the day Venture capital Peak XV and Sequoia’s trek ahead has plenty of tricky troughs 11 mins read Investing Despite the INR1 lakh a share feat, MRF skids on 10 critical points investors shouldn’t overlook. 7 mins read OTT More than just claps and confetti: How IPL has transformed the in-stadium cricket viewing experience 14 mins read Subscribe to  ETPrime Videos PM Modi, Joe Biden exchange gifts at White House PM signs on T-shirt of a boy as he welcomes Modi Details of PM Modi's gift to Joe Biden, Jill Biden Stock radar: Buy Grasim stock; target Rs 2080 Sensex loses over 50 pts, Nifty tests 18,850 Joe Biden, Jill Biden receive PM Modi at WH Here's what was there for PM at State Dinner Stock ideas by experts for June 22 Stocks in focus: Glenmark, LIC & more Richard Gere to Ruchira Kamboj on UN's Yoga event 1 2 3 Poll Are foreign rating agencies unfairly harsh on India? Yes No Can't say Vote Latest from ET Gritty Goenka says Sony-Zee merger is still on for larger audience Modi invites Micron to boost chip making in India Can Vedanta afford to repay debts amid profit pangs? Trending World News Nintendo Direct 2023 Pokemon Go Spotlight Hour Titanic tourist submersible Lionel Messi Britney Joy Venus Williams Boxing Summer solstice Jujutsu Kaisen Chapter 227 Wordle Today Quordle Today Mikayla Campinos Taylor Swift The Flash Box-office Plaza Wars Paxton Whitehead Summer Solstice 2023 Extraction 2 How to Watch Portugal vs Iceland Titanic Submarine
> ```


**Note that** you don't have to use `'\n---\n'` to join the siblings' text - you can use any string as separator.

---

Btw, for that specific site's articles, a much simpler way would be to target the header tag specifically by its class,

```py
    if url.startswith('https://economictimes.indiatimes.com/'): ## might need more
        h1Sibs = soup.select('*:has(>h1.artTitle)~*') 
        h1Sibs_text = '\n---\n'.join(ns.get_text(' ') for ns in h1Sibs)
```

<sup>NOTE: using [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property) with the *`*:has(>h1.artTitle)~*`* selector is similar to using `soup.find('h1',class_='artTitle').parent.next_siblings`, but is safer than chaining `find`,`parent`,`next_siblings` as it will simply return an empty list instead of raising any errors if `h1.artTitle` is not found.</sup>

If you are scraping many different links, but you know the sites for most of them, you might want to break if up into *`if...elif...`* blocks for each site (or even groups of sites) and only use something generic like my first snippet for unlisted sites in the `else` block. You might even consider using something [like this configurable parser](https://pastebin.com/ZnZ7xM6u) with sets of selectors for each site.
