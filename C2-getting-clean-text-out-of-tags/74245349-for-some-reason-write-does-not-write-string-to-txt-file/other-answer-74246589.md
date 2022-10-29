---
title: "For some reason .write() does not write string to .txt file anymore"
site: stackoverflow
question_id: 74245349
answer_id: 74246589
url: https://stackoverflow.com/a/74246589
author: "d r"
author_url: https://stackoverflow.com/users/19023353
posted: 2022-10-29T15:35:15Z
last_edited: 2022-10-29T15:46:38Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5c894e55403b0dc26733a6a46112c785e37ce06fb9bc2c0ad4e01c67ba4d1265
role: another answer on the same question, kept as context; not my work
---

# Answer by [d r](https://stackoverflow.com/users/19023353) — 2022-10-29

Posted on Stack Overflow, <https://stackoverflow.com/a/74246589>, 2022-10-29, last edited 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is your slitely changed script with marked (*****************) changes:
~~~python
def get_subpages(url):
    # gets all subpage links from a website that start with the given url
    from urllib.request import urlopen, Request
    from bs4 import BeautifulSoup
    links = [url]
    
    # ******************* added sublinks_list variable   ******************
    sublinks_list = []
    
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
                sublinks = soup.findAll('a')

                for sublink in sublinks:
                
                    #templinks.append(sublink.get('href'))  ***************** changed the line with next row *****************
                    templinks.append(sublink['href'])
                    
                # clean off accidental 'None' values
                templinks = list(filter(lambda item: item is not None, templinks))

                for templink in templinks:
                    # make sure we have still the correct website and don't accidentally crawl instagram etc.
                    # also avoid duplicates
                    
                    #if templink.find(url) == 0 and templink not in links:  ******************* changed the line with next row *****************
                    if templink not in sublinks_list:
                    
                        #links.append(templink)      ******************* changed the line with next row *****************
                        sublinks_list.append(templink)
                        
                        all_urls.write(templink + '\n')     # ******************* added this line  *****************

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

lnks = get_subpages('https://www.jhanley.com/blog/pyscript-creating-installable-offline-applications/')  #  # ******************* url used for testing  *****************

~~~
It works and there is over 180 links in the file. Please test it yourself. There are still some missfits and questionable sintax so you should test your code thoroughly again - but the part with writing links into a file works.    

Regards...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[curies](https://stackoverflow.com/users/20364643)** (2022-10-29): Thank you so much for this contribution! Yes this works! Sadly the script has lost quite some functionality. This now only grabs the links on the webpage you enter as input. As the newly found websites are not returned as input anymore this does not achieve my goal with the script. With an input like ``https://www.jhanley.com`` I wanna find all websites that start like this, and not external links like ``techradar.com/``. You got rid of that part when reworking the if condition and don't feed into the loop back anymore. Tried your other minor changes, which didn't get my script running sadly.
- **[d r](https://stackoverflow.com/users/19023353)** (2022-10-29): I'm sorry, but I don't get it completely. For https://www.jhanley.com the content of the file is:  https://www.jhanley.com/ #site-content https://www.jhanley.com/main / /blog/ https://contact.jhanley.com https://www.jhanley.com/main/ http://www.wordpress.org https://andersnoren.se #
- **[d r](https://stackoverflow.com/users/19023353)** (2022-10-29): It looks OK. to me - like something you can refine a bit and get what you need.
- **[d r](https://stackoverflow.com/users/19023353)** (2022-10-29): And there is a lot of links starting with '/' like '/blog/' in jhanley.com which are abreviated href for main url plus that link - it is in fact https://jhanley.com/blog/. Such links should be treated just like that - main url plus '/blog/'. Regards...
