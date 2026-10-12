# Code from my Stack Overflow answer https://stackoverflow.com/a/74419123 (posted 2022-11-13), extracted verbatim; may need the question's context to run.
# from requests_html import HTMLSession

url = 'https://www.tapology.com/fightcenter/bouts/2093-ufc-76-the-dean-of-mean-keith-jardine-vs-chuck-the-iceman-liddell'
req = HTMLSession().get(url)
soup = BeautifulSoup(req.text, 'html.parser')

fightstats = soup.find_all('td')
fightresult = soup.find_all('div', class_='boutResultHolder')
print('\n\n\n'.join('\n'.join( # remove some whitespaces from text for better readability
    ' '.join(w for w in t.text.split() if w) for t in f if t.text.strip()
) for f in [fightresult, fightstats]))
