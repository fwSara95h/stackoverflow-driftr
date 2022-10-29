---
title: "For some reason .write() does not write string to .txt file anymore"
site: stackoverflow
question_id: 74245349
url: https://stackoverflow.com/q/74245349
asked: 2022-10-29T12:39:25Z
asked_by: "curies"
asked_by_url: https://stackoverflow.com/users/20364643
last_edited: 2022-10-29T12:40:23Z
tags: [python, text, beautifulsoup]
score: 1
views_at_snapshot: 675
answer_count: 3
accepted_answer_id: 74245682
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f87b818465123198659a8af9498c3275098f5e8a5ecb84eef0d085bfe4d8d113
---

# For some reason .write() does not write string to .txt file anymore

Asked by [curies](https://stackoverflow.com/users/20364643) on Stack Overflow, <https://stackoverflow.com/q/74245349>, 2022-10-29, last edited 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So I started with python some days ago and now tried to make a function that gives me all subpages of websites. I know it may not be the most elegant function but I had been pretty proud to see it working. But for some reason unknown to me, my function does not work anymore. I could've sworn I haven't changed that function since it worked the last time. But after hours of attempts to debug I am slowly doubting myself. Can you maybe take a look why my function does not output to a .txt file anymore? I just get handed an empty text file. Though if I delete it atleast creates a new (empty) one.

I tried to move the save strings part out of the try block, which didn't. work. I also tried ``all_urls.flush()`` to maybe save everything. I restarted the PC in the hopes that something in the background accessed the file and made me unable to write on it. I also renamed the file it supposed to save as, so as to generate something truly fresh. Still the same problem. I also controlled that the ``link`` from the loop gets given as a string, so that shouldn't be a problem. I also tried: 

```
print(link, file=all_urls, end='\n')
```
as a replacement to

```
all_urls.write(link)
all_urls.write('\n')
```
with no result.

My full function:

```
def get_subpages(url):
    # gets all subpage links from a website that start with the given url
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup
    links = [url]
    tested_links = []
    to_test_links = links
    # open a .txt file to save results into
    all_urls = open('all_urls.txt', 'w')
    problematic_pages = open('problematic_pages.txt', 'w')
    while len(to_test_links)>0:
        for link in to_test_links:
            print('the link we are testing right now:', link)
            # add the current link to the tested list
            tested_links.append(link)
            try:
                print(type(link))
                all_urls.write(link)
                all_urls.write('\n')
                # Save it to the -txt file and make an abstract
                # get the link ready to be accessed
                req = Request(link)
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, features="html.parser")
                # empty previous temporary links
                templinks = []
                # move the links on the subpage link to templinks
                for sublink in soup.findAll('a'):
                    templinks.append(sublink.get('href'))
                # clean off accidental 'None' values
                templinks = list(filter(lambda item: item is not None, templinks))

                for templink in templinks:
                    # make sure we have still the correct website and don't accidentally crawl instagram etc.
                    # also avoid duplicates
                    if templink.find(url) == 0 and templink not in links:
                        links.append(templink)

                #and lastly refresh the to_test_links list with the newly found links before going back into the loop
                to_test_links = (list(set(links) ^ set(tested_links)))
            except:
                # Save it to the ERROR -txt file and make an abstract
                problematic_pages.write(link)
                problematic_pages.write('\n')
                print('ERROR: All links on', link, 'not retrieved. If need be check for new subpages manually.')
    all_urls.close()
    problematic_pages.close()
    return links
```
