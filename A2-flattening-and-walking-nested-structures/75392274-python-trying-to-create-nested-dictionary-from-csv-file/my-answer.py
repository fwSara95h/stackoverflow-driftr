# Code from my Stack Overflow answer https://stackoverflow.com/a/75424722 (posted 2023-02-12), extracted verbatim; may need the question's context to run.
def load_csv(filename, sep=','):
    with open(filename, 'r') as csvfile:
        csvlines = csvfile.read().strip().splitlines()
    csvRows = [[v.strip() for v in l.split(sep)] for l in csvlines]
    if not csvRows: return {}
    keys = csvRows[0][1:]
    return {r[0]: dict(zip(keys, r[1:])) for r in csvRows[1:] if r}
