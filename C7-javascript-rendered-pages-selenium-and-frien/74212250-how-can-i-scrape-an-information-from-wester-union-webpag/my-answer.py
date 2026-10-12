# Code from my Stack Overflow answer https://stackoverflow.com/a/74216513 (posted 2022-10-27), extracted verbatim; may need the question's context to run.
soup = linkToSoup_selenium(url, tmout='3')
# YOU MIGHT NEED TO ADJUST tmout - it sets the wait time for loading
# (3sec seems to be more that enough for me, but it can vary)

if soup is not None: 
    convSpan = soup.select_one('span#smoExchangeRate')
    if convSpan is not None:
        print(convSpan.get_text(strip=True))

# output:
# 1.00 BRL = 56.5617Argentine Peso(ARS)
