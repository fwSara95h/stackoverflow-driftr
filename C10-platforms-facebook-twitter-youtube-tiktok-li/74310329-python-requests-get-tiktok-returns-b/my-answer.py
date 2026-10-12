# Code from my Stack Overflow answer https://stackoverflow.com/a/74333736 (posted 2022-11-06), extracted verbatim; may need the question's context to run.
api_url = "https://api.scrapingant.com/v2/general"
page_url = "https://www.tiktok.com/@thatlittlepuff/video/7160116843611475246"
myKey_sa = YOUR_API_TOKEN # register on https://scrapingant.com/ and paste here

page = requests.get(f'{api_url}?url={page_url}&x-api-key={myKey_sa}')

print(page.content)
