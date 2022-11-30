---
title: "How to scrape multiple elements within a specific section of a website"
site: stackoverflow
question_id: 74632370
url: https://stackoverflow.com/q/74632370
asked: 2022-11-30T18:11:31Z
asked_by: "Zachariah"
asked_by_url: https://stackoverflow.com/users/7897708
last_edited: 2022-11-30T18:20:41Z
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 110
answer_count: 1
accepted_answer_id: 74635364
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4186f122491c46557965f98e2d923ba2c5152e977ac3c94a1e3a8cbf968a5570
---

# How to scrape multiple elements within a specific section of a website

Asked by [Zachariah](https://stackoverflow.com/users/7897708) on Stack Overflow, <https://stackoverflow.com/q/74632370>, 2022-11-30, last edited 2022-11-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Super new to python coming from a C# background.

Inside Microsoft's wiki page,   https://en.wikipedia.org/wiki/Microsoft,

I'm trying to scrape all the text inside the history section. 

I'm curious how to go about the situation using beautiful soup. I understand that beautiful soup doesn't have XPath support.

The first element to be scraped from the history section is:

    <div role="note" class="hatnote navigation-not-searchable">Main article: <a href="/wiki/History_of_Microsoft" title="History of Microsoft">History of Microsoft</a></div>


The Last element to be scraped will be:

    <p>On January 18, 2022, Microsoft announced the acquisition of American video game developer and <a href="/wiki/Holding_company" title="Holding company">holding company</a> <a href="/wiki/Activision_Blizzard" title="Activision Blizzard">Activision Blizzard</a> in an all-cash deal worth $68.7 billion.<sup id="cite_ref-:0_150-0" class="reference"><a href="#cite_note-:0-150">[150]</a></sup> Activision Blizzard is best known for producing franchises, including but not limited to <i><a href="/wiki/Warcraft" title="Warcraft">Warcraft</a></i>, <i><a href="/wiki/Diablo_(series)" title="Diablo (series)">Diablo</a></i>, <i><a href="/wiki/Call_of_Duty" title="Call of Duty">Call of Duty</a></i>, <i><a href="/wiki/StarCraft" title="StarCraft">StarCraft</a></i>, <i><a href="/wiki/Candy_Crush_Saga" title="Candy Crush Saga">Candy Crush Saga</a></i>, <i><a href="/wiki/Crash_Bandicoot" title="Crash Bandicoot">Crash Bandicoot</a></i>, <i><a href="/wiki/Spyro" title="Spyro">Spyro the Dragon</a></i>, <i><a href="/wiki/Skylanders" title="Skylanders">Skylanders</a></i>, and <i><a href="/wiki/Overwatch_(video_game)" title="Overwatch (video game)">Overwatch</a></i>.<sup id="cite_ref-151" class="reference"><a href="#cite_note-151">[151]</a></sup> Activision and Microsoft each released statements saying the acquisition was to benefit their businesses in the <a href="/wiki/Metaverse" title="Metaverse">metaverse</a>, many saw Microsoft's acquisition of video game studios as an attempt to compete against <a href="/wiki/Meta_Platforms" title="Meta Platforms">Meta Platforms</a>, with <a href="/wiki/TheStreet" title="TheStreet">TheStreet</a> referring to Microsoft wanting to become "the <a href="/wiki/The_Walt_Disney_Company" title="The Walt Disney Company">Disney</a> of the metaverse".<sup id="cite_ref-152" class="reference"><a href="#cite_note-152">[152]</a></sup><sup id="cite_ref-153" class="reference"><a href="#cite_note-153">[153]</a></sup> Microsoft has not released statements regarding Activision's recent legal controversies regarding employee abuse, but reports have alleged that Activision CEO <a href="/wiki/Bobby_Kotick" title="Bobby Kotick">Bobby Kotick</a>, a major target of the controversy, will leave the company after the acquisition is finalized.<sup id="cite_ref-154" class="reference"><a href="#cite_note-154">[154]</a></sup> The deal is expected to close in 2023 followed by a review from the <a href="/wiki/US_Federal_Trade_Commission" class="mw-redirect" title="US Federal Trade Commission">US Federal Trade Commission</a>.<sup id="cite_ref-155" class="reference"><a href="#cite_note-155">[155]</a></sup><sup id="cite_ref-:0_150-1" class="reference"><a href="#cite_note-:0-150">[150]</a></sup>
    </p>

How would I go about getting all the information inbetween those elements?




    from bs4 import BeautifulSoup
    import requests
    
    url = 'https://en.wikipedia.org/wiki/Microsoft'
      
    # call get method to request that page
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, "html.parser")
