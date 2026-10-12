# Code from my Stack Overflow answer https://stackoverflow.com/a/74237830 (posted 2022-10-28), extracted verbatim; may need the question's context to run.
with open('cat.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        imagesname = ' '.join(row)
        r = requests.get(imagesname)

        soup = bs(r.content, 'html.parser') 
        tables = soup.find_all('img', class_='pick')

        inParsed = urllib.parse.urlparse(imagesname) # break down url
        rootUrl = f'{inParsed.scheme}://{inParsed.netloc}' # to get root

        for image in tables:
            imageUrl = urllib.parse.urljoin(rootUrl, imageUrl.get('src')) # add root to src
            saveImgAs = [u for u in imageUrl.split('/') if u][-1] # get name from link

            with open(saveImgAs, "wb") as f:
                f.write(requests.get(imageUrl).content) # download
                f.close()

            print(saveImgAs, image)
