# Code from my Stack Overflow answer https://stackoverflow.com/a/74018989 (posted 2022-10-10), extracted verbatim; may need the question's context to run.
matchedStr = [s for s in list_of_str if s in dirname]
if matchedStr:
    os.rename(f,"SET_STR")
else: pass # REDUNDANT
