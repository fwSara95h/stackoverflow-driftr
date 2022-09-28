---
title: "How do I use BeautifulSoup to extract all the news article urls from this webpage - https://indianexpress.com/article/technology/"
site: stackoverflow
question_id: 73874461
answer_id: 73887971
url: https://stackoverflow.com/a/73887971
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T21:28:35Z
last_edited: 2022-10-02T19:55:53Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73887971/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 348d5d752faeeabc7ec508dd3d59d4cb1836f27c0414ce404d54750687bda826
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73887971>, 2022-09-28, last edited 2022-10-02; score 0. Text as retrieved 2026-10-12.

You can filter the links so that only the ones containing `article/` remain. (Python's [list comprehension][1] is my favorite syntax for filtering.) 

A possible solution:

    from bs4 import BeautifulSoup
    page = requests.get('https://indianexpress.com/section/technology/')
    bSoup = BeautifulSoup(page.content, 'html.parser')
    links_list = bSoup.find_all('a')
    
    #filter links for articles:
    article_links_all = [
        l.get('href') for l  in links_list 
        if 'href' in l.attrs and 'article/' in l.attrs['href']
    ]
    
    # get rid of duplicates:
    article_links = list(set(article_links_all))
    
    for link in article_links:
        print(link)
Then the output will be:

    https://indianexpress.com/article/technology/mobile-tabs/older-apple-ipads-to-get-stage-manager-support-with-ipados-16-1-beta-8177892/
    https://indianexpress.com/article/sports/sport-others/in-gujarat-the-national-games-garba-and-the-start-of-election-fever-8179176/
    https://indianexpress.com/article/lifestyle/health/covid-may-increase-heart-ailments-if-it-becomes-endemic-expert-8179186/
    https://indianexpress.com/article/lifestyle/health/patient-administer-self-cpr-heart-attack-cardiac-arrest-cardiopulmonary-resuscitation-8178675/
    https://indianexpress.com/article/technology/tech-news-technology/google-search-new-features-multisearch-food-shopping-google-maps-8179203/
    https://indianexpress.com/article/technology/tech-news-technology/erbium-is-a-malware-that-steals-credit-card-details-passwords-and-hacks-crypto-wallets-8177544/
    https://indianexpress.com/article/opinion/columns/what-the-rajasthan-political-crisis-highlights-congress-effectively-has-no-high-command-8176760/
    https://indianexpress.com/article/cities/thiruvananthapuram/home-ministry-lists-murders-and-attacks-by-pfi-cadres-in-ban-notification-8178553/
    https://indianexpress.com/article/technology/tech-news-technology/tech-indepth-understanding-nvidia-dlss-and-dlss-3-8178684/
    https://indianexpress.com/article/horoscope/horoscope-today-26-september-2022-check-astrological-prediction-for-scorpio-sagittarius-cancer-aries-and-other-signs-8162319/
    https://indianexpress.com/article/what-is/what-is-the-protection-of-children-from-sexual-offences-act-2012/
    https://indianexpress.com/article/technology/tech-news-technology/apple-ditches-iphone-production-increase-after-demand-falters-8177169/
    https://indianexpress.com/article/technology/science/ancient-armoured-bristly-worm-wufengella-phylum-evolution-lophophore-8178150/
    https://indianexpress.com/article/technology/tech-news-technology/intel-and-samsung-display-showcase-slidable-pc-during-intels-innovation-keynote-8177212/
    https://indianexpress.com/article/technology/tech-reviews/realme-9i-5g-review-8159696/
    https://indianexpress.com/article/sports/cricket/watch-suresh-raina-takes-a-stunner-against-australia-legends-in-road-safety-world-series-semi-8179194/
    https://indianexpress.com/article/technology/techook/amazon-flipkart-sales-best-budget-tws-earbuds-to-buy-under-rs-3000-8177816/
    https://indianexpress.com/article/entertainment/bollywood/ranbir-kapoor-trade-decodes-the-stars-box-office-journey-the-good-the-bad-the-blockbuster-8176244/
    https://indianexpress.com/article/opinion/editorials/after-the-ban-the-political-challenge-posed-by-pfi-still-needs-tackling-8179138/
    https://indianexpress.com/article/india/code-of-ethics-for-digital-news-websites-6758543/
    https://indianexpress.com/article/sports/cricket/chahar-arshdeep-send-back-half-sa-side-in-15-balls-as-india-secure-victory-in-first-t20i-8179221/
    https://indianexpress.com/article/technology/tech-news-technology/amazons-big-september-2022-echo-event-tonight-heres-what-to-expect-8177264/
    https://indianexpress.com/article/technology/mobile-tabs/nothing-phone-1-gets-another-camera-centric-update-8178907/
    https://indianexpress.com/article/technology/techook/nova-to-niagara-the-top-android-launchers-to-try-out-on-your-smartphone-8175729/
    https://indianexpress.com/article/technology/science/italian-space-agency-releases-liciacube-images-of-dart-crash-8177728/
    https://indianexpress.com/article/explained/pfi-terrorist-organisation-mha-ban-explained-8177409/
    https://indianexpress.com/article/cities/delhi/delhi-ncr-news-live-updates-rains-aap-arvind-kejriwal-bjp-8173016/
    https://indianexpress.com/article/technology/tech-reviews/oppo-enco-buds-2-review-8153028/
    https://indianexpress.com/article/technology/tech-news-technology/intel-announces-13th-gen-intel-core-processor-heres-everything-you-need-to-know-8177290/
    https://indianexpress.com/article/sports/cricket/ind-vs-sa-1st-t20-surya-woke-up-after-he-got-hit-8179164/
    https://indianexpress.com/article/technology/tech-reviews/vivo-v25-pro-review-8177339/
    https://indianexpress.com/article/trending/trending-in-india/rhinoceros-walks-on-nepal-road-unmindful-of-people-touching-it-8178819/
    https://indianexpress.com/article/technology/gaming/netflix-launches-game-handles-for-its-games-all-you-need-to-know-8178368/
    https://indianexpress.com/article/india/senior-advocate-r-venkataramani-is-new-attorney-general-of-india-8179072/
    https://indianexpress.com/article/cities/delhi/delhi-yamuna-flowing-warning-level-heavy-rain-basin-states-8173217/
    https://indianexpress.com/article/technology/tech-news-technology/amazons-september-2022-product-launch-event-announcements-8179069/
    https://indianexpress.com/article/technology/tech-reviews/samsung-galaxy-watch-5-pro-review-8151008/
    https://indianexpress.com/article/entertainment/movie-review/blonde-movie-review-ana-de-armas-imarilyn-monroe-biopic-netflix-8175733/
    https://indianexpress.com/article/business/economy/rupee-value-us-dollar-falls-low-news-8173192/
    https://indianexpress.com/article/technology/gadgets/sony-india-festive-sale-deals-discounts-on-audio-headphones-tws-speakers-tvs-8178107/
    https://indianexpress.com/article/trending/trending-in-india/women-perform-garba-inside-mumbai-local-train-8178884/
    https://indianexpress.com/article/india/jaishankar-sullivan-discuss-bilateral-ties-indo-pacific-8179191/
    https://indianexpress.com/article/technology/tech-news-technology/dating-apps-thrive-in-china-but-not-just-for-romance-8177218/
    https://indianexpress.com/article/technology/science/nasa-spacex-crew-5-launch-dragon-endurance-falcon-9-8178453/
    https://indianexpress.com/article/cities/ahmedabad/two-firs-lodged-over-clashes-between-nsui-abvp-members-8179172/
    https://indianexpress.com/article/technology/science/how-about-them-apples-research-orchards-chart-a-fruits-future-8178701/
    https://indianexpress.com/article/cities/baroda/borsad-municipality-president-loses-no-confidence-motion-as-bjp-members-defy-party-whip-8179197/
    https://indianexpress.com/article/technology/tech-reviews/viewsonic-xg2431-gaming-monitor-review-8140688/


  [1]: https://www.w3schools.com/python/python_lists_comprehension.asp

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Community](https://stackoverflow.com/users/-1)** (2022-10-02): Your answer could be improved with additional supporting information. Please [edit] to add further details, such as citations or documentation, so that others can confirm that your answer is correct. You can find more information on how to write good answers [in the help center](/help/how-to-answer).
