# Code from my Stack Overflow answer https://stackoverflow.com/a/73929247 (posted 2022-10-02), extracted verbatim; may need the question's context to run.
# from bs4 import BeautifulSoup 
for website in df_actionname['Weblink']:
  detailpage = requests.get(website)
  pageSoup = BeautifulSoup(detailpage.content, 'html.parser')
  print(f'scraped "{pageSoup.title.text}" from {website}')
