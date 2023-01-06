---
title: "Python Beautifulsoup4 all parser not working?"
site: stackoverflow
question_id: 75037029
url: https://stackoverflow.com/q/75037029
asked: 2023-01-06T23:32:25Z
asked_by: "OFENROHR100"
asked_by_url: https://stackoverflow.com/users/15020314
last_edited: never
tags: [python, web-scraping, beautifulsoup, request]
score: 0
views_at_snapshot: 371
answer_count: 2
accepted_answer_id: 75038864
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f8ac11ff5c68df22fb58713d455f7ded7dfad6a592a67d2a840cf8e9a77d4fed
---

# Python Beautifulsoup4 all parser not working?

Asked by [OFENROHR100](https://stackoverflow.com/users/15020314) on Stack Overflow, <https://stackoverflow.com/q/75037029>, 2023-01-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

so I want to scrape a website but the current problem Iam facing is that whenever I try to print out the element Iam scrapping it just returns an empty list. I know that the problem is that the parser can't find the class in the hmtl code. I tried all the parsers which are supported with Beautifoulsoup4 => 'lxmL' and 'hmtl5lib' but it still doesn't work. I even tried downgrading the version from 4.11.0 => 4.9.3, still doesn't work. Any ideas?

    import requests
    import random
    from bs4 import BeautifulSoup
    
    products = {
        1: "Hoodies",
        2: "Sunglasses",
        3: "Couple-T-shirts",
        4: "Wall-Stickers",
        5: "Rugs",
        6: "Dog-Bed",
        7: "Claw-Cutter",
        8: "Fur-Remover",
        9: "Led-Keyboard",
        10: "Wireless-Chargers",
        11: "Powerbank",
        12: "Game-Controller",
        13: "Portable-Speakers",
        14: "Scalp-Massager",
        15: "Blackhead-Remover",
        16: "Lash-Products",
        17: "Makeup-Kit",
        18: "Air-Tag-Tracker",
        19: "Air-Purifiers",
        20: "Pixelart",
        21: "Yoga-Mats",
        22: "Face-Masks",
        23: "Fitness-Watches",
        24: "Resistance-Bands",
        25: "Air-Purifiers",
        26: "Cell-Phone-Mounts",
        27: "Wireless-Security-Cameras",
        28: "Massage-Tools",
        29: "Air-Purifiers",
        30: "Eyeliner-Pencil",
        31: "Water-Filters",
        32: "Slow-Feeder-Dog-Bowls",
        33: "Video-Doorbells",
        34: "Solar-Outdoor-Lights",
        35: "Phone-Grip",
        36: "Slow-Feeder-Dog-Bowls",
        37: "Pajamas",
        38: "Skin-Care-Oil",
        39: "Flasks",
        40: "Monitor-Holders",
        41: "Watches",
        42: "Rings",
        43: "Monitor-Holders",
        44: "Nail-Polish",
        45: "Rice-Cooker",
    }
    
    i = random.randint(1, 45)
    
    url = f'https://www.aliexpress.com/af/{products[i]}.html?spm=a2g0o.productlist.10000020initiative_id=SB_20230106091400&dida=y&origin=n'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    soup.prettify()
    product = soup.find_all('a', {'class': 'manhattan--container--1lP57Ag cards--gallery--2o6yJVt'})
    productimage = soup.find_all('img', {'class': 'manhattan--img--36QXbtQ product-img'})
    productprice = soup.find_all('div', {'class': 'manhattan--price-sale--1CCSZfK'})
    productrating = soup.find_all('span', {'class': 'manhattan--evaluation--3cSMntr'})
    
    print(soup)
    
    productlinkstring = product[0]['href']
    productlinkstring = 'https://www' + productlinkstring[4:]
    productimagelinkstring = productimage[0]['src']
    productimagelinkstring = 'https://' + productimagelinkstring[2:]
    productpricestring = productprice[0].text
    productratingsting = productrating[0].text
    
    producttitle = products[i]
    producttitlestring = producttitle.replace('-', ' ')
    
    productsstring = products[i]
    productsstringright = productsstring.replace('-', '+')
    endpoint = f'https://api.datamuse.com/words?ml={productsstringright}&max=18'
    
    response = requests.get(endpoint)
    
    data = response.json()
    
    print(productlinkstring)
    print(productimagelinkstring)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Carcigenicate](https://stackoverflow.com/users/3000206)** (2023-01-06): That likely means the content you're look for is populated by JavaScript, so it doesn't exist when you parse it. If that's the case, you'd need to use a tool like Selenium to run the JavaScript to generate the content. You can check if that's the case by checking the `Source` tab instead of the `Elements` tab in the dev tools. If it's only in the latter, that's your problem.
- **[OFENROHR100](https://stackoverflow.com/users/15020314)** (2023-01-06): It probably isn't. It worked some hours ago with a html parser in a different code but on the same site. (Sorry, I don't have a save of that code). But I will try Selenium then.
- **[OFENROHR100](https://stackoverflow.com/users/15020314)** (2023-01-06): @Carcigenicate No, it is not only in the latter option.
- **[CryptoFool](https://stackoverflow.com/users/7631480)** (2023-01-06): I ran the beginning of your code and saved the incoming HTML to a file and checked it out.  I don't see any 'class' attributes in the HTML that would match your queries.  In fact, the string`"manhattan--"` does not appear anywhere in the HTML.  I had the same thought as @Carcigenicate...that the elements you're expecting to find are not in the starting HTML of the page but are rather added to the DOM dynamically via Javascript.  I could very well have done something wrong.  In any case, if you aren't dumping and looking at the incoming HTML, that's the first place to look for issues.
- **[OFENROHR100](https://stackoverflow.com/users/15020314)** (2023-01-06): So I think the classes get changed depending on the size of the window. Maybe that is the problem.
