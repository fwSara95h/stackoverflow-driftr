---
title: "Unable to find anchor tag for href link on goolge search page"
site: stackoverflow
question_id: 76800098
url: https://stackoverflow.com/q/76800098
asked: 2023-07-31T00:39:30Z
asked_by: "Cryptic "
asked_by_url: https://stackoverflow.com/users/8656115
last_edited: 2023-07-31T06:12:01Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 47
answer_count: 1
accepted_answer_id: 76803168
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 93b5eff943fd675754bbae22a194e925e7ea609b8070550d3eace41fd43ccdda
---

# Unable to find anchor tag for href link on goolge search page

Asked by [Cryptic ](https://stackoverflow.com/users/8656115) on Stack Overflow, <https://stackoverflow.com/q/76800098>, 2023-07-31, last edited 2023-07-31 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.


```
# Input data file
    df = pd.read_csv('BookSD.csv', usecols=[0], encoding = "ISO-8859-1")
    df.columns = ['model_name']

# Output file
    csv_file = open('sundown_scrape.csv', 'w')
    csv_writer = csv.writer(csv_file)
    df_result = pd.DataFram`your text`e(columns=['Model_name', 'Features', 'Specification'])

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like    Gecko)       Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}

    links = []
    model_list = ['SALT-200.4', 'SALT-2000.6'] 

    def get_google_search_links_sundown(query_model):
        href_pattern = re.compile(r'.*https://www.sundownaudio.com.*')
        for query in query_model:
            url = f"https://www.google.com/search?q={query}"
            #print(url)
            response = requests.get(url, headers=headers)
            #response.raise_for_status()
            #print(response)
            soup = BeautifulSoup(response.content, 'html5lib')
            #Find relevant HTML elements to extract data
            search_results = soup.find('a', href=href_pattern) ###### THIS LINE SEEMS TO BE A PROBLEM
        
            #for result in search_results:
            #   link = result.find("a")
            # If url (Search result) is received then extract the href link
            if search_results:
                href = search_results.get("href")
                if href.startswith("/url?q=https://www.sundownaudio.com/index.php/"):
                    href = href[7:]  # Removing the "/url?q=" part from the link
                    if "&sa" in href:  # Removing any additional parameters in the link
                        href = href.split("&sa")[0]
                    links.append(href)
            else:
                print ('No sundown link found in this a-tag')
        return links  # Need to pass list for all model in function

# Fetching search result for desired model query
    links_fn = get_google_search_links_sundown(model_list)

    str_links = ""
    print("Links found:")
    for link in links_fn:
        str_links += link
        print(str_links)
```


I am totally confused why my script is pulling a `href` link for SALT-200.4 but it does not work for "SALT-2000.6". 

I have tried the script to pass each individually and still getting the same results. I have tried different parser types, header in get requests without improvements. Href links for both should be fetched as the HTML result is showing same on  chrome inspection for `url = f"https://www.google.com/search?q={query}"`

Note that I am not able to search by div-class due to dynamic nature of google search results

Please suggest what am I doing wrong here. I would like to solve this problem using Beautifulsoup for my project.
