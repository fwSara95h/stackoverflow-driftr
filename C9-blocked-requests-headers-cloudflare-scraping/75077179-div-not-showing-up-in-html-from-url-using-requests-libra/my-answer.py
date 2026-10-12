# Code from my Stack Overflow answer https://stackoverflow.com/a/75104039 (posted 2023-01-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import requests

sess = requests.Session()
headers = {'user-agent': 'Mozilla/5.0'}
data = {'username': 'YOUR_EMAIL/USERNAME', 'password': 'YOUR_PASSWORD'}

loginResp = sess.post('https://untappd.com/login', headers=headers, data=data)
print(loginResp.status_code, loginResp.reason, 'from', loginResp.url) ## should print 200 OK...

response = sess.get(venue_url, headers = {'User-agent': 'Mozilla/5.0'})
## CAN CONTINUE AS BEFORE ##

# --- block 2 ---
# venue_url = 'https://untappd.com/v/glory-days-grill-of-ellicott-city/3329822'
gloryMenu = scrape_untappd_menu(venue_url, cookies=sess.cookies)
