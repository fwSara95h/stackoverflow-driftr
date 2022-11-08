---
title: "cloudscraper.exceptions.CloudflareChallengeError: Detected a Cloudflare version 2 Captcha challenge"
site: stackoverflow
question_id: 74352220
answer_id: 74357110
url: https://stackoverflow.com/a/74357110
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-08T07:34:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74357110/revisions
accepted: true
score: 1
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [linkToSoup_selenium, prettify_htmlText]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c04501b377e26eb70b2ebae7d431c3c5eb6c14bac4aaaee9d85a9ef607bf8022
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74357110>, 2022-11-08; **accepted**; score 1. Text as retrieved 2026-10-12.

You could use [ScrapingAnt](https://scrapingant.com/) instead of cloudscraper - it's pretty useful unless you need to scrape a very large number of pages (the free tier only allows 10k requests per month). If you register, they give you a token that you can paste into the code below:
```python
import requests
import urllib.parse
from bs4 import BeautifulSoup

sa_key = 'YOUR_API_TOKEN' # paste here
sa_api = 'https://api.scrapingant.com/v2/general'
qParams = {'url': 'https://coinsniper.net/new', 'x-api-key': sa_key}
reqUrl = f'{sa_api}?{urllib.parse.urlencode(qParams)}'  

r = requests.get(reqUrl)
# print(r.text) # --> html
soup = BeautifulSoup(r.content, 'html.parser')
```
I printed with my own function `print(`[`prettify_htmlText`](https://gist.github.com/Driftr95/89df5f5814339af7cbdd5a60cc3468a3)`(soup))` (I sometimes find it more readable than just `print(soup.text)`) to get the output
```markdown
New Listings
- CoinSniper
Limited Presale
Token Revolutionising the $850b Carbon Credits Industry
Read More
ad
BNB Price: $342.32
Projects Listed: 39,062
Total Votes: 114,961,735
Watchlists: 1,589,556
Total KYCs: 227
Total Audits: 245
Supported Chains: 8
Register / Login
26K
50K
Submit Coin
Account
Watchlist - Login - Register
Cryptocurrencies
Today's best - All time Best - New listings - By Marketcap - Presales
CoinSniper
Submit coin - Update Coin - Contact Us
Services
Advertising - Audit partners - KYC verification - AMA hosting
Follow us on twitter!
Join our telegram group!
Best Coins Today - All Time Best - New Listings - By Marketcap - Presales
Your banner here? Contact us!
Buy now Buy now Buy now       Buy now Buy now Buy now       Buy now
New listings
Today's best - All time best - New listings - By marketcap - Presales
Promoted
Your coin here? Contact us!
| # Coin                            | Votes        | #  | Name                            | Badges    | Chain | Market Cap | Price            | Change 24h | Launch      | Votes   |
| --------------------------------- | ------------ | -- | ------------------------------- | --------- | ----- | ---------- | ---------------- | ---------- | ----------- | ------- |
| 1 BIG Big Eyes                    | 803,087 VOTE | 1  | BIG Big Eyes                    | KYC Audit | ETH   | Presale    | -                | -          | In 3 months | 803,087 |
| 2 D2T Dash 2 Trade                | 756,164 VOTE | 2  | D2T Dash 2 Trade                | KYC Audit | ETH   | Presale    | -                | -          | In 22 days  | 756,164 |
| 3 IMPT IMPT.io                    | 753,262 VOTE | 3  | IMPT IMPT.io                    | KYC Audit | ETH   | Presale    | -                | -          | In 3 months | 753,262 |
| 4 RIA Calvaria: Duels of Eternity | 752,429 VOTE | 4  | RIA Calvaria: Duels of Eternity | KYC Audit | ETH   | Presale    | -                | -          | In 2 months | 752,429 |
| 5 METRO Metropoly                 | 656,951 VOTE | 5  | METRO Metropoly                 | Audit     | ETH   | Presale    | -                | -          | In 1 month  | 656,951 |
| 6 DOGET Dogeliens                 | 408,400 VOTE | 6  | DOGET Dogeliens                 | Audit     | BSC   | Presale    | -                | -          | In 4 months | 408,400 |
| 7 BABYBTC BabyBitcoin             | 335,483 VOTE | 7  | BABYBTC BabyBitcoin             | KYC Audit | BSC   | Presale    | -                | -          | In 1 month  | 335,483 |
| 8 TFT Toon Finance                | 293,482 VOTE | 8  | TFT Toon Finance                |           | ETH   | Presale    | -                | -          | In 1 month  | 293,482 |
| 9 GGT GameGuru                    | 130,041 VOTE | 9  | GGT GameGuru                    | KYC Audit | BSC   | $ 769,182  | $ 0. (0x2) 8096  | 21.8 %     | 1 month ago | 130,041 |
| 10 NITRO NITRO                    | 10,777 VOTE  | 10 | NITRO NITRO                     | KYC Audit | BSC   | Presale    | -                | -          | In 11 days  | 10,777  |
| 11 BERGERDOGE Berger Dog Coin     | 917 VOTE     | 11 | BERGERDOGE Berger Dog Coin      |           | BSC   | -          | $ 0. (0x12) 5663 | 23.9 %     | 3 days ago  | 917     |
Coins
Chain
ALL
ALL - BSC - ETH - MATIC - TRX - FTM - KCC - DOGECHAIN - OTHER
Platform
ALL
ALL - CMC - CG - CMC & CG
KYC
ALL
ALL - YES - NO
Audit
ALL
ALL - YES - NO
Reset Filters
| # Coin                           | Votes 24h | Votes | #  | Name                          | Chain | Market Cap      | Price            | Change 24h | Launch       | Votes | Votes 24h | Submitted      |
| -------------------------------- | --------- | ----- | -- | ----------------------------- | ----- | --------------- | ---------------- | ---------- | ------------ | ----- | --------- | -------------- |
| 1 NOVA NovaChain                 | 0 VOTE    | 0     | 1  | NOVA NovaChain                | BSC   | -               | -                | -          | Today        | 0     | 0         | 51 minutes ago |
| 2 JUNP4EVER Jump forever         | 0 VOTE    | 0     | 2  | JUNP4EVER Jump forever        | MATIC | -               | -                | -          | 1 day ago    | 0     | 0         | 1 hour ago     |
| 3 LITE THE LITE                  | 0 VOTE    | 0     | 3  | LITE THE LITE                 | BSC   | -               | $ 0. (0x5) 2744  | 10.73 %    | 2 days ago   | 0     | 0         | 1 hour ago     |
| 4 FAMUS likefamus                | 2 VOTE    | 2     | 4  | FAMUS likefamus               | BSC   | $ 3,917,503     | $ 0. (0x3) 3917  | 12.97 %    | 7 days ago   | 2     | 2         | 2 hours ago    |
| 5 MCT🌛 Moon Community Token      | 1 VOTE    | 1     | 5  | MCT🌛 Moon Community Token     | BSC   | Presale         | -                | -          | In 1 day     | 1     | 1         | 2 hours ago    |
| 6 CHADZ ChadZone                 | 0 VOTE    | 0     | 6  | CHADZ ChadZone                | ETH   | -               | $ 0. (0x5) 9257  | 100 %      | Today        | 0     | 0         | 3 hours ago    |
| 7 FLAPPY Flappy Bird Token       | 1 VOTE    | 1     | 7  | FLAPPY Flappy Bird Token      | BSC   | Presale         | -                | -          | In 11 days   | 1     | 1         | 3 hours ago    |
| 8 SANTAFLOKI Santa Floki         | 0 VOTE    | 0     | 8  | SANTAFLOKI Santa Floki        | ETH   | $ 27,194        | $ 0. (0x7) 2774  | 1126 %     | Today        | 0     | 0         | 4 hours ago    |
| 9 ASA Andermattswissalps         | 0 VOTE    | 0     | 9  | ASA Andermattswissalps        | OTHER | -               | -                | -          | In 11 days   | 0     | 0         | 4 hours ago    |
| 10 CHAD Chad Doge                | 15 VOTE   | 15    | 10 | CHAD Chad Doge                | ETH   | $ 7,276         | $ 0. (0x5) 7275  | 123 %      | Today        | 15    | 15        | 5 hours ago    |
| 11 BGT Bull Game ToKens          | 0 VOTE    | 0     | 11 | BGT Bull Game ToKens          | BSC   | -               | $ 0. (0x2) 4467  | 93.17 %    | 2 days ago   | 0     | 0         | 6 hours ago    |
| 12 BRAZIL Brazil Inu             | 3 VOTE    | 3     | 12 | BRAZIL Brazil Inu             | ETH   | $ 109,698       | $ 0. (0x3) 1096  | 0.2 %      | 4 days ago   | 3     | 3         | 7 hours ago    |
| 13 APLACE AbitPlace              | 0 VOTE    | 0     | 13 | APLACE AbitPlace              | OTHER | -               | -                | -          | 1 day ago    | 0     | 0         | 7 hours ago    |
| 14 WCRT World Cup Raffle Token   | 3 VOTE    | 3     | 14 | WCRT World Cup Raffle Token   | BSC   | -               | $ 0. (0x2) 2877  | -          | 1 day ago    | 3     | 3         | 8 hours ago    |
| 15 TWITTERBIRD TwitterBird       | 0 VOTE    | 0     | 15 | TWITTERBIRD TwitterBird       | BSC   | -               | $ 0. (0x6) 7861  | -          | 2 days ago   | 0     | 0         | 9 hours ago    |
| 16 BURN BurnChain                | 1 VOTE    | 1     | 16 | BURN BurnChain                | BSC   | -               | -                | -          | In 8 days    | 1     | 1         | 10 hours ago   |
| 17 BANAL Baby Anal Dust          | 4 VOTE    | 4     | 17 | BANAL Baby Anal Dust          | BSC   | -               | $ 0. (0x1) 1981  | -          | 1 day ago    | 4     | 4         | 11 hours ago   |
| 18 GRINCHGROW GrinchGrow         | 0 VOTE    | 0     | 18 | GRINCHGROW GrinchGrow         | BSC   | -               | $ 0. (0x11) 2048 | -          | 1 day ago    | 0     | 0         | 12 hours ago   |
| 19 BNBC BNBChampionship          | 0 VOTE    | 0     | 19 | BNBC BNBChampionship          | BSC   | -               | -                | -          | Tomorrow     | 0     | 0         | 12 hours ago   |
| 20 NFTYI NFTY                    | 0 VOTE    | 0     | 20 | NFTYI NFTY                    | BSC   | Presale         | -                | -          | In 21 days   | 0     | 0         | 13 hours ago   |
| 21 LAPAD Let's ANNOUNCE PAD      | 27 VOTE   | 27    | 21 | LAPAD Let's ANNOUNCE PAD      | BSC   | -               | -                | -          | In 1 year    | 27    | 27        | 13 hours ago   |
| 22 BETS BSC BETS                 | 0 VOTE    | 0     | 22 | BETS BSC BETS                 | BSC   | -               | -                | -          | Today        | 0     | 0         | 13 hours ago   |
| 23 ALEXJONES Alex Jones Token    | 1 VOTE    | 1     | 23 | ALEXJONES Alex Jones Token    | BSC   | -               | $ 0. (0x9) 1320  | -          | 1 day ago    | 1     | 1         | 13 hours ago   |
| 24 CELF Christmas Elf Bsc        | 132 VOTE  | 132   | 24 | CELF Christmas Elf Bsc        | BSC   | -               | $ 0. (0x6) 7276  | 41.69 %    | 1 day ago    | 132   | 132       | 13 hours ago   |
| 25 ADIS ADIS                     | 0 VOTE    | 0     | 25 | ADIS ADIS                     | BSC   | -               | $ 0. (0x3) 3319  | -          | 1 day ago    | 0     | 0         | 13 hours ago   |
| 26 CI CLEAN IT                   | 1 VOTE    | 1     | 26 | CI CLEAN IT                   | BSC   | -               | $ 0. (0x9) 9722  | -          | 1 day ago    | 1     | 1         | 14 hours ago   |
| 27 ETHERGY Ethergy Web           | 0 VOTE    | 0     | 27 | ETHERGY Ethergy Web           | ETH   | -               | -                | -          | Tomorrow     | 0     | 0         | 14 hours ago   |
| 28 TWITTERCAT Twitter Cat        | 2 VOTE    | 2     | 28 | TWITTERCAT Twitter Cat        | BSC   | -               | $ 0. (0x5) 8161  | -          | 1 day ago    | 2     | 2         | 15 hours ago   |
| 29 DOGESH DOGESH INU             | 169 VOTE  | 169   | 29 | DOGESH DOGESH INU             | BSC   | Presale         | -                | -          | In 1 month   | 169   | 169       | 15 hours ago   |
| 30 CYBER Cyberpunk City Token    | 0 VOTE    | 0     | 30 | CYBER Cyberpunk City Token    | BSC   | -               | $ 0. (0x8) 2892  | -          | 1 day ago    | 0     | 0         | 16 hours ago   |
| 31 AVT AVATAR                    | 0 VOTE    | 0     | 31 | AVT AVATAR                    | BSC   | -               | $ 0. (0x4) 2416  | 12.86 %    | 4 days ago   | 0     | 0         | 17 hours ago   |
| 32 TWITTY Twitty Inu             | 0 VOTE    | 0     | 32 | TWITTY Twitty Inu             | BSC   | -               | $ 0. (0x10) 6187 | 3.54 %     | 5 days ago   | 0     | 0         | 18 hours ago   |
| 33 ANGRYBIRDS AngryBirds         | 0 VOTE    | 0     | 33 | ANGRYBIRDS AngryBirds         | BSC   | -               | $ 0. (0x12) 1311 | -          | 2 days ago   | 0     | 0         | 21 hours ago   |
| 34 ZEPX ZEPCOIN                  | 0 VOTE    | 0     | 34 | ZEPX ZEPCOIN                  | BSC   | -               | -                | -          | 5 months ago | 0     | 0         | 21 hours ago   |
| 35 BUTTS ButtCoin                | 0 VOTE    | 0     | 35 | BUTTS ButtCoin                | OTHER | -               | -                | -          | 5 months ago | 0     | 0         | 1 day ago      |
| 36 PALT PalancaToken             | 0 VOTE    | 1     | 36 | PALT PalancaToken             | BSC   | $ 1,080,976,328 | $ 0. (0x7) 1080  | 126.38 %   | 11 days ago  | 1     | 0         | 1 day ago      |
| 37 MST Monster Protocol          | 0 VOTE    | 0     | 37 | MST Monster Protocol          | BSC   | Presale         | -                | -          | In 6 days    | 0     | 0         | 1 day ago      |
| 38 EZDOGE EZ Doge                | 0 VOTE    | 5     | 38 | EZDOGE EZ Doge                | BSC   | $ 93,668        | $ 0. (0x2) 1873  | 42.64 %    | 1 day ago    | 5     | 0         | 1 day ago      |
| 39 DAPPS DAPP Play Store         | 0 VOTE    | 0     | 39 | DAPPS DAPP Play Store         | MATIC | -               | -                | -          | 3 days ago   | 0     | 0         | 1 day ago      |
| 40 FNDEX Free Nation DEX         | 0 VOTE    | 0     | 40 | FNDEX Free Nation DEX         | MATIC | $ 310,023       | $ 0. (0x1) 1476  | 0 %        | 1 month ago  | 0     | 0         | 1 day ago      |
| 41 MTV MuuTV                     | 0 VOTE    | 0     | 41 | MTV MuuTV                     | BSC   | -               | $ 0. (0x6) 5276  | 4.05 %     | 1 day ago    | 0     | 0         | 1 day ago      |
| 42 RHLLOR Token of Fire (RHLLOR) | 1 VOTE    | 1     | 42 | RHLLOR Token of Fire (RHLLOR) | ETH   | $ 227,989       | $ 0. (0x4) 1908  | 21.07 %    | 1 year ago   | 1     | 1         | 1 day ago      |
| 43 POWGE PowgeCoin               | 0 VOTE    | 0     | 43 | POWGE PowgeCoin               | OTHER | -               | -                | -          | 1 month ago  | 0     | 0         | 1 day ago      |
| 44 HBA HeroesBattleArena         | 0 VOTE    | 0     | 44 | HBA HeroesBattleArena         | MATIC | -               | -                | -          | In 28 days   | 0     | 0         | 1 day ago      |
| 45 QATARLAEEB QatarLaeeb         | 0 VOTE    | 0     | 45 | QATARLAEEB QatarLaeeb         | BSC   | -               | $ 0. (0x13) 9833 | 100 %      | 2 days ago   | 0     | 0         | 1 day ago      |
| 46 WAM WAM Token                 | 0 VOTE    | 0     | 46 | WAM WAM Token                 | BSC   | -               | $ 0. (0x8) 2129  | -          | 2 days ago   | 0     | 0         | 1 day ago      |
| 47 KST Koinswap                  | 0 VOTE    | 1     | 47 | KST Koinswap                  | BSC   | $ 9,582,253     | $ 0. (0x3) 4813  | 1.38 %     | 2 months ago | 1     | 0         | 1 day ago      |
| 48 FGC FrogChain                 | 0 VOTE    | 0     | 48 | FGC FrogChain                 | BSC   | -               | $ 0. (0x14) 2223 | 100 %      | In 1 year    | 0     | 0         | 1 day ago      |
| 49 EDOGE eDOGE                   | 0 VOTE    | 0     | 49 | EDOGE eDOGE                   | BSC   | -               | -                | -          | In 1 day     | 0     | 0         | 1 day ago      |
| 50 QS Qatar soccer               | 0 VOTE    | 0     | 50 | QS Qatar soccer               | ETH   | $ 4,893         | $ 0. (0x3) 4893  | 44.29 %    | 3 days ago   | 0     | 0         | 1 day ago      |
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - … - 479 - 480
Your Favorite Coin Missing?
Can't find your coin? List your favorite coin now!
Get your
community to vote for your coin and gain exposure.
Submit Coin
View Top Coins
Click the button below to view the Top Listed coins!
These coins had
at least 500 community votes.
View Top Coins
Find the best new cryptocurrency projects
Did ever you wonder where people find the best new cryptocurrency projects, coins and tokens like Doge
and Shiba Inu? They use
websites like coinsniper.net . Cryptocurrency projects are listed here before
CoinMarketCap,
CoinGecko and major exchanges. Find the best crypto moonshots on our website.
However: before investing always do your
own research (DYOR)! Listing on coinsniper.net does NOT mean we endorse the project,
they could be scams.
Be careful with your investments.
How does CoinSniper work?
New cryptocurrency projects can be listed Applying Here. Once applied, they
instantly become visible
on the New Listings Page. New listings require 500 votes to be officially listed in
our top list.
After that, anyone can see and vote for the project.
Get your community to vote on your project, because votes matter! Our ranking is simple: the highest
votes is #1 on our website.
The project will get exposure with all our visitors!
Note on voting: Unique votes only count once for the "All Time" page, but can count every 24
hours on the "Today" page.
All Time Rankings - Daily Ranking - New Listings - Submit Coin - Update Request - Contact Us - Services - Advertise - © 2022 coinsniper.net - Cookie Statement - Terms & Conditions - Privacy Policy
Disclaimer
CoinSniper gives user the opportunity to post information about crypto projects.Please note that CoinSniper does not verify the user generated content on this website. CoinSniper does not provide any financial advice, act as financial services provider or broker, or in any other way aid in the formation of any transactions in cryptocurrency or otherwise.
Also note that, the cryptocurrency listed on this website could potentially be scams, i.e. designed to induce you to invest financial resources that may be lost forever and not be recoverable once investments are made. You are responsible to Do Your Own Research (DYOR) regarding any information listed on this website.
WARNING: Scam Telegram Channels
The ONLY real Telegram channel for CoinSniper / ScamSniper is @coinsnipernet .
Any other channel using the CoinSniper / ScamSniper logo and brand name are a SCAM!
Okay, I understand
```

<hr><hr>

If the 10k requests cap is too limiting for you, you should consider selenium - I have [this function](https://gist.github.com/Driftr95/cbae6710c134df708f44ade8503f6638) which can simplify its use a bit, but you still have to install it and download the driver.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jagar](https://stackoverflow.com/users/12053756)** (2022-11-09): Just tested it, and it is extremely slow, (~ 1 min for a simple website), and also for some websites it gives `{"detail":"Our browser was detected by target site. Try again later or contact us support@scrapingant.com"}` are you just using selenium there?
- **me** (2022-11-09): @Jagar sorry to hear, *this* site wasn't that slow for me with scrapingAnt, but yes, with some sites it's quite slow; and yes, I use selenium pretty much whenever I can, but some environments don't allow selenium installation,  and that's where I use scrapingAnt...
