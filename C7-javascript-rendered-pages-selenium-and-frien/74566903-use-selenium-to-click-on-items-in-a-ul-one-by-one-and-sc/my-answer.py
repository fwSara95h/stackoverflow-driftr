# Code from my Stack Overflow answer https://stackoverflow.com/a/74573149 (posted 2022-11-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def extractAttr(elem, sel, attr, defVal=None):
    e = elem.find_elements(By.CSS_SELECTOR, sel)
    aVal = e[0].get_attribute(attr) if e else None
    return defVal if aVal is None else aVal

# --- block 2 ---
liSels = [ # selectors for the list items
    ('name', 'span[itemprop="name"]', 'innerText'),
    ('link', 'a[itemprop="url"][href]', 'href'),
    ('imgUrl', 'img[itemprop="photo"][src]', 'src')
]
pgSels = [ # selectors for the individual pages
    ('description', 'p.description', 'innerText'),
    ('moreInfo', 'li.large-margin-bottom > h3 + ul', 'innerText')
]

# --- block 3 ---
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 5)
rootUrl = 'https://www.crunchyroll.com'
cardSel = '#main_content > ul > li'

driver.get(f'{rootUrl}/comics/manga')
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cardSel)))

cards = [{
    k: extractAttr(c, s, a) for k, s, a in liSels
} for c in driver.find_elements(By.CSS_SELECTOR, cardSel)]
for i, c in enumerate(cards):
    driver.get(c['link'])
    for k, s, a in pgSels:
        cards[i][k] = extractAttr(driver, s, a)

# driver.quit()

# --- block 4 ---
[
 {'name': 'Genshin Impact', 'link': 'https://www.crunchyroll.com/comics/manga/genshin-impact/volumes', 'imgUrl': 'https://api-manga.crunchyroll.com/i/croll_manga/9e6d8c402f2916bd093fc7a1524265ca_1544713688_large.jpg', 'description': 'Aeons ago, the elder elemental gods granted civilization to the human race, but the world soon splintered as corruption and greed grew without check. Can the forces holding this world together be balanced against human desires, or is everything ultimately doomed to end in destruction? http://genshin.mihoyo.com/', 'moreInfo': 'Publisher: miHoYo Limited\nFirst Published:\nAuthor: miHoYo\nArtist: miHoYo\nCopyright: © 2017-2018 miHoYo Limited ALL RIGHTS RESERVED'} ,
 {'name': 'Inside Mari', 'link': 'https://www.crunchyroll.com/comics/manga/inside-mari/volumes', 'imgUrl': 'https://api-manga.crunchyroll.com/i/croll_manga/70d74c2842e6ebed097c8309889c67e8_1389837055_large.jpg', 'description': 'A young man is a shut-in, with nothing to do but kill time. The sole pleasure in his life is following home an angelic high school girl he sees every day in a convenience store. Today, like any other day, he follows her, but… Shuzo Oshimi, the creator of Drifting Net Café and Flowers of Evil, continues to open hidden doors of the heart in this monthly serialized story!', 'moreInfo': 'Publisher: Futabasha\nFirst Published:\nAuthor:\nArtist: Shuzo Oshimi\nCopyright: ©Shuzo Oshimi/FUTABASHA PUBLISHERS LTD.\nTranslator: Sheldon Drzka\nEditor: Emily Martha Sorensen\nLetterer: Carl Vanstiphout'} ,
 {'name': 'To Your Eternity', 'link': 'https://www.crunchyroll.com/comics/manga/to-your-eternity/volumes', 'imgUrl': 'https://api-manga.crunchyroll.com/i/croll_manga/c49832d6c4e25d693e6b88b0328e70a5_1519720335_large.jpg', 'description': 'A new manga from the creator of the acclaimed A Silent Voice, featuring intimate, emotional drama and an epic story spanning time and space, To Your Eternity is a totally unique and moving manga about death, life, reincarnation, and the nature of love. A lonely boy wandering the Arctic regions of North America meets a wolf, and the two become fast friends, depending on each other to survive the harsh environment. But the boy has a history, and the wolf is more than meets the eye as well …', 'moreInfo': 'Publisher: Kodansha\nFirst Published:\nAuthor:\nArtist:\nCopyright: Based on the manga "Fumetsu no Anata he" by Yoshitoki Oima originally serialized in the Weekly Shonen magazine published by KODANSHA LTD. To Your Eternity copyright © Yoshitoki Oima／KODANSHA LTD. English translation copyright © Yoshitoki Oima／KODANSHA LTD. All rights reserved.\nTranslator: Steven LeCroy\nEditor: Alexandra Swanson\nLetterer: Darren Smith'} ,
 {'name': 'Sun-Ken Rock', 'link': 'https://www.crunchyroll.com/comics/manga/sun-ken-rock/volumes', 'imgUrl': 'https://api-manga.crunchyroll.com/i/croll_manga/368cba1b39ae46b3435e6ac1d4f5987e_1391991276_large.jpg', 'description': 'Ken left Japan, pursuing the woman he loves to Korea. However, while she became a policewoman, Ken somehow wound up in a gang, even becoming their boss! The man who came from Japan now rises in Korea. It\'s Korean "Rock-Action" with a powerful punch!', 'moreInfo': 'Publisher: Shonen Gahosha\nFirst Published:\nAuthor:\nArtist: Boichi\nCopyright: ©BOICHI/Shonen-gahosha Co., Ltd.'} ,
 {'name': 'Fire Force', 'link': 'https://www.crunchyroll.com/comics/manga/fire-force/volumes', 'imgUrl': 'https://api-manga.crunchyroll.com/i/croll_manga/83fa13859c8baee6f20708b5d4bd5c35_1640071967_large.jpg', 'description': 'A new action fantasy set in a steampunk Tokyo from the creator of the smash-hit Soul Eater!The city of Tokyo is plagued by a deadly phenomenon: spontaneous human combustion! Luckily, a special team is there to quench the inferno: The Fire Force! The fire soldiers at Special Fire Cathedral 8 are about to get a unique addition. Enter Shinra, a boy who possesses the power to run at the speed of a rocket, leaving behind the famous “devil’s footprints” (and destroying his shoes in the process). ... more', 'moreInfo': 'Publisher: Kodansha\nFirst Published:\nAuthor: Atsushi Ohkubo\nArtist: Atsushi Ohkubo\nCopyright: Based on the manga "En\'en no Shōbōtai" by Atsushi Ohkubo originally serialized in the weekly Shonen Magazine published by KODANSHA LTD. Fire Force copyright © Atsushi Ohkubo／KODANSHA LTD. English translation copyright © Atsushi Ohkubo／KODANSHA LTD. All rights reserved.'} ,
]

# --- block 5 ---
# import pandas
pandas.DataFrame(cards).to_csv('crunchyCards.csv', index=False)
