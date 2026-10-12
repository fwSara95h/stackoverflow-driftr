# Code from my Stack Overflow answer https://stackoverflow.com/a/74570172 (posted 2022-11-25), extracted verbatim; may need the question's context to run.
xSoup = BeautifulSoup(xmlStr, 'lxml') ## do NOT use 'xml' parser here unless you want to lose namespaces

enumTags = ['st:name', 'stu:studentscreening']
for d in [c for c in xSoup.descendants if c.name]:
    for name in enumTags:
        for i, t in enumerate(d.find_all(name, recursive=False)):
            t.name = f'{t.name}{i}'
