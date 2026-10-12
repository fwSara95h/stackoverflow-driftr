# Code from my Stack Overflow answer https://stackoverflow.com/a/73928355 (posted 2022-10-02), extracted verbatim; may need the question's context to run.
def cleanPageTitle(origTitle, pageUrl):
    domain = tldextract.extract(pageUrl).domain
    cleaned = "".join([
            x for x in origTitle if (x.isalnum() or x in "._- ")
        ]).replace(domain, "")
    return cleaned
