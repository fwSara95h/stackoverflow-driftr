# Code from my Stack Overflow answer https://stackoverflow.com/a/74693810 (posted 2022-12-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
title = soup.find('em', class_='gravel-text').text

imgLinks = []
for images in soup.find_all('div', class_='thumb-frame'):
    imgLinks.append(images.a['href']) 

j = [{'title':title, 'image':imgLinks}]
# dump j, write to and close jfile #

# --- block 2 ---
j = [{'title':soup.find('em', class_='gravel-text').text, 'image':[]}] 
for images in soup.find_all('div', class_='thumb-frame'):
    j['image'].append(images.a['href']) 

# dump j, write to and close jfile

# --- block 3 ---
url = "https://stock.adobe.com/search?k=interstellar%20movie"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")


with open('images.json', 'w') as jfile:
    json.dump([{'title': soup.find('em', class_='gravel-text').text, 'image': [
        image.a['href'] for image in soup.find_all('div', class_='thumb-frame')
    ]}], jfile)

# --- block 4 ---
url = "https://stock.adobe.com/search?k=interstellar%20movie"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")


title = soup.find('em', class_='gravel-text')
title = '! MISSING TITLE !' if title is None else title.text

imgLinks = [
    image.select_one('a[href]').get('href') for image in 
    soup.select('div[class="thumb-frame"]:has(a[href])')
]

with open('images.json', 'w') as jfile:
    json.dump([{'title':title, 'image':imgLinks}], jfile)
