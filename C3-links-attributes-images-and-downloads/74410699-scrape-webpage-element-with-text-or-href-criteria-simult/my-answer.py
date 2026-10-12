# Code from my Stack Overflow answer https://stackoverflow.com/a/74417369 (posted 2022-11-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
auction_results = soup.select('tr:-soup-contains("3rd Incremental Auction"), tr:has(*[href*="base-residual"])')

# --- block 2 ---
inText, inAttr = "3rd Incremental Auction", "base-residual"
tag, attr = "tr", "href"
selector = f'{tag}:-soup-contains("{inText}"), tr:has(*[{attr}*="{inAttr}"])'
auction_results = soup.select(selector)

# --- block 3 ---
auction_results = soup.find_all(lambda t: t.name == tag and ((
    t.find(lambda c: c.get(attr) and inAttr in c.get(attr)) is not None
) or (t.text and inText in t.text)))

# --- block 4 ---
auction_results = [
    ar for ar in auction_results if not 
    [c for c in auction_results if ar in c.parents]
]

# --- block 5 ---
def checkPat(pat, main): # for convenience
    return True if re.search(pat, main, re.IGNORECASE | re.DOTALL) else False

def find_results(tag, textPat, attrPat, tagName='tr', attrName='href'):     
    if tag.name != tagName: return False  

    hasText = checkPat(textPat, tag.text) if tag.text else False
    hasAttr = tag.find(lambda t: t.get(attrName) and checkPat(
        attrPat, t.get(attrName))) is not None

    if hasText or hasAttr:
        if not tag.find(lambda t: find_results(t,textPat,attrPat,tagName,attrName)): 
            return True
    return False

# --- block 6 ---
# def checkPat... # as before

def find_auction_results(tag):  
    textPat = "3rd Incremental Auction" 
    attrPat = "base-residual"
    tagName, attrName = "tr", "href"

    if tag.name != tagName: return False # has to be tr

    hasText = checkPat(textPat, tag.text) if tag.text else False
    hasAttr = tag.find(lambda t: t.get(attrName) and checkPat(
        attrPat, t.get(attrName))) is not None

    if hasText or hasAttr:
        # if nested like [ tr -> tr -> a ] , will only allow inner tr
        if not tag.find(find_auction_results): return True
    return False
