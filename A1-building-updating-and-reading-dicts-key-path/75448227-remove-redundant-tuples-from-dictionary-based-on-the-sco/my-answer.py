# Code from my Stack Overflow answer https://stackoverflow.com/a/75451173 (posted 2023-02-14), extracted verbatim; may need the question's context to run.
def getAllPairs(obj):
    if isinstance(obj, tuple) and len(obj)==2: return [obj]
    allPairs = []
    if isinstance(obj, dict): obj = obj.values()
    if hasattr(obj, '__iter__') and not isinstance(obj, str):
        for i in obj: allPairs += getAllPairs(i)
    return allPairs

def onlyBest(obj, bestRef:dict):
    if isinstance(obj, list):
      # if all(isinstance(i, tuple) and len(i)==2 for i in obj):
        return [i for i in obj if not i[1] < bestRef.get(i[0],i[1])]
    if isinstance(obj, dict):
        return {k: onlyBest(v,bestRef) for k, v in obj.items()}
    return obj
