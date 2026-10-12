# Code from my Stack Overflow answer https://stackoverflow.com/a/75296465 (posted 2023-01-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> results = soup.find_all('div', class_="similar-listings-item sponsored-listing") 
>

# --- block 2 ---
results = soup.find_all('div', {'class': "similar-listings-item"}) ## OR
# results = soup.select('div.similar-listings-item')

# --- block 3 ---
infoList = []
for result in results:
    Title = result.find('div', class_= "similar-listings-info").text.replace('\n','')
    location = result.find( class_= "listings-location").text.replace('\n','')
    Price = result.find('div', class_= "similar-listings-price").text.replace('\n','')

    info = (Title, location, Price) # this is a tuple btw, so 
    # infoList.append(info) # --> list of tuples
    infoList.append([Title, location, Price]) # --> list of lists
    # print(info) # will print for every result
print(info) # will print ONLY the LAST result

# --- block 4 ---
def get_min_text(containerTag, elName, classAttr, defaultVal=None):
    el = containerTag.find(elName, class_=classAttr)
    if el is None: return defaultVal
    return ' '.join(el.get_text(' ').split()) # split+join minimizes whitespace

results = soup.find_all('div', {'class': "similar-listings-item"}) 
infoList = [[get_min_text(result, *c[:3]) for c in [
    ('div', 'similar-listings-info'), # Title
    ('p', 'listings-location'), # Location
    ('div', 'similar-listings-price') # Price
]] for result in results]
