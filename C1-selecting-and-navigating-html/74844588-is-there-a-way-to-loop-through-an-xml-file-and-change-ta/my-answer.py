# Code from my Stack Overflow answer https://stackoverflow.com/a/74845261 (posted 2022-12-19), extracted verbatim; may need the question's context to run.
tagListPairs = [(['stu:studentscreening'], ['sti:name'])]
for parentTags, enumTags in tagListPairs:
    for p in soup.find_all(parentTags):
        for name in enumTags:
            for i, t in enumerate(p.find_all(name)):
                t.name = f'{t.name}{i}'
