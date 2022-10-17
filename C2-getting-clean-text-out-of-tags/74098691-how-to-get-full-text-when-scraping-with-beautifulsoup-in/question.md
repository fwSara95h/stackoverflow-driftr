---
title: "How to get full text when scraping with beautifulsoup in Python?"
site: stackoverflow
question_id: 74098691
url: https://stackoverflow.com/q/74098691
asked: 2022-10-17T14:14:45Z
asked_by: "Want Help"
asked_by_url: https://stackoverflow.com/users/16580625
last_edited: 2022-10-17T14:15:18Z
tags: [python, pandas, beautifulsoup]
score: -2
views_at_snapshot: 52
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 25619a086d6e4a8a16522ee00fdb4de24baaeee31e8ab990f2a0e168c22213ec
---

# How to get full text when scraping with beautifulsoup in Python?

Asked by [Want Help](https://stackoverflow.com/users/16580625) on Stack Overflow, <https://stackoverflow.com/q/74098691>, 2022-10-17, last edited 2022-10-17. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape website - product description... but the problem is that I am not getting full description of product, but just part of it (this is the output):

                                                   about
    0  [\n, [Descrizione], \n, [], [Allenamento per p...

And here's my code:

    def perform_search(kodovi):
        i = 0
        c = 0
        for x in kodovi:
            k = requests.get(searchlink).text
            soup=BeautifulSoup(k,'html.parser')
        
            productlist = soup.find_all("ul",{"class":"products-grid"})
    
            for product in productlist:
                link = product.find("a",{"class":"product-image"}).get('href')
                productlinks.append(link)
                print("Done")
    
    
    def scraping_data(productlinks,r):
        for link in productlinks:
            f = requests.get(link,headers=headers).text
            hun=BeautifulSoup(f,'html.parser')
    
    #Here I get description of product
            try:
                about=hun.find("div",{"class":"std"})
            except:
                about=None
                print("nothing found")
    
            try:
                name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
            except:
                name=None
    
            whisky = {"about":about}
    
            data.append(whisky)
            r=r+1
            print("completed",r)
    
        df = pd.DataFrame(data)
    
        print(df)


So actually the final question is how can I get full product description if it's structured like this:

    <div class="std">
    <h2>Descrizione</h2>
    <p></p><p>A LOT OF TEXT WITH PRODUCT DESCRIPTION......</p>
    </div>
