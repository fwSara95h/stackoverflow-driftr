---
title: "Downloading PDFs from CAG"
site: stackoverflow
question_id: 73985919
url: https://stackoverflow.com/q/73985919
asked: 2022-10-07T10:40:05Z
asked_by: "NoobCoderPy"
asked_by_url: https://stackoverflow.com/users/20147620
last_edited: 2022-10-07T10:45:22Z
last_editor: "Filburt"
last_editor_url: https://stackoverflow.com/users/205233
tags: [python, pdf, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 61
answer_count: 1
accepted_answer_id: 73986919
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 671225ec28f5da3bc2da1344ccb7a3511f8401e8ce104603b3a6f419d36c35b0
---

# Downloading PDFs from CAG

Asked by [NoobCoderPy](https://stackoverflow.com/users/20147620) on Stack Overflow, <https://stackoverflow.com/q/73985919>, 2022-10-07, last edited 2022-10-07 by [Filburt](https://stackoverflow.com/users/205233). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to download multiple PDFs from CAG website (link <https://cag.gov.in/en/state-accounts-report?defuat_state_id=64>). I am using the following code-

```python
url='https://cag.gov.in/en/state-accounts-report?defuat_state_id=64'

response=requests.get(url)

response

soup=BeautifulSoup(response.text,'html.parser')

soup

for link in soup.select("a[href$='.pdf']"):
   
    print(link)

for link in soup.select("a[href$='.pdf']"):    
    
    filename = os.path.join(folder_location,link['href'].split('/')[-1])  

     
    with open(filename, 'wb') as f:

      f.write(requests.get(urljoin(url,link['href'])).content)
```

This is giving me all the PDFs from the whole page, I wish to download the PDF under the tab 'Monthly Key Indicators' only. Please suggest the necessary changes in the code to do that.
