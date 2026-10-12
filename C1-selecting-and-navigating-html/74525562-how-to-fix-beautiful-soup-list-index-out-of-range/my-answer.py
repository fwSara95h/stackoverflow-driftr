# Code from my Stack Overflow answer https://stackoverflow.com/a/74570856 (posted 2022-11-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def extractAttr(tag, sel, attr='', defVal=None):
    s = tag.select_one(sel)
    if s is None: return defVal
    if attr == '': 
        stxt = s.get_text(' ').strip()
        return stxt if stxt else defVal
    return s.get(attr, defVal)

# --- block 2 ---
selRef = [ # key, selector, attribute, default
    ('Title', '.jobTitle', '', '?'),
    ('Company', '.companyName', '', '?'),
    ('Location', '.companyLocation', '', '?'),
    ('Rating', '.ratingNumber', '', 'NaN'),
    ('Date', '.date', '', 'NaN'),
    ('Salary', '.salary-snippet-container', '', 'NaN'),
    ('Description', '.job-snippet', '', ''),
    ('Links', 'a[href]', 'href', None)
] # be careful to have exactly 4 items in each tuple

# --- block 3 ---
for job in jobs:
    result_html = job.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser') 
    jn += 1

    jDict = {k: extractAttr(soup, s, a, d) for k, s, a, d in selRef}
    dataframe = pd.concat([dataframe, pd.DataFrame([jDict])])
    print("Job number {0:4d} added - {1:s}".format(jn, jDict['Title']))
