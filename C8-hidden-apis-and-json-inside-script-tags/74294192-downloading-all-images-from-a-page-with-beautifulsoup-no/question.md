---
title: "Downloading all Images from a page with beautifulSoup not working"
site: stackoverflow
question_id: 74294192
url: https://stackoverflow.com/q/74294192
asked: 2022-11-02T18:38:10Z
asked_by: "Jonathan Devereux"
asked_by_url: https://stackoverflow.com/users/7471514
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 309
answer_count: 1
accepted_answer_id: 74332271
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9b494fd790af79f8f0edc087d098ec4d08fb5456b580d23dbd21daabbfc44999
---

# Downloading all Images from a page with beautifulSoup not working

Asked by [Jonathan Devereux](https://stackoverflow.com/users/7471514) on Stack Overflow, <https://stackoverflow.com/q/74294192>, 2022-11-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to download the show images from [this][1] page with beautifulsoup.  

When I run the below code the only image that downloads is the spinning loading icon.  

When I check the requests tab on the page I can see requests for all the other images on the page so assume they should be downloaded as well. I am not sure why they would not download as they are contained within img tags in the html on the page?

    import re
    import requests
    from bs4 import BeautifulSoup
    site = 'https://www.tvnz.co.nz/categories/sci-fi-and-fantasy'
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    urls = [img['src'] for img in image_tags]
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if not filename:
             print("Regular expression didn't match with the url: {}".format(url))
             continue
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
    print("Download complete, downloaded images can be found in current directory!")

  [1]: https://www.tvnz.co.nz/categories/sci-fi-and-fantasy

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Greg](https://stackoverflow.com/users/13628163)** (2022-11-02): It looks like the page is loaded using JavaScript. If you run `print(response.text)` you'll notice the HTML does not contain the tv shows. You'll need something like selenium
- **[Jonathan Devereux](https://stackoverflow.com/users/7471514)** (2022-11-02): noted, thanks will look into Selenium. Would it be possible to just post a request to get the same image back? using the python requests library?
