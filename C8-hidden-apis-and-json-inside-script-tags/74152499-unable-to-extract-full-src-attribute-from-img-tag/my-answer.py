# Code from my Stack Overflow answer https://stackoverflow.com/a/74152500 (posted 2022-10-21), extracted verbatim; may need the question's context to run.
dimgTags = soup.find_all(lambda l: 'dimg_179' in str(l))

# get rid of parent tags
dimgTags = [d for d in dimgTags if not [t for t in dimgTags if d in t.parents]]
dimgTags = [d for d in dimgTags if d.name != 'img']

if dimgTags:
    dimgSrc = str(dimgTags[0]).split("var s='")[1].split("'")[0]
    display(HTML(f'<img src="{dimgSrc}">'))
