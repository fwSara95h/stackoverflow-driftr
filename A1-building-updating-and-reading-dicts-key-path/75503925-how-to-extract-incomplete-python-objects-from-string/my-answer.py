# Code from my Stack Overflow answer https://stackoverflow.com/a/75511708 (posted 2023-02-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import ast

def eval_brokenLiteral(litStr:str, defaultVal=None, printError=True):
    try: return ast.literal_eval(litStr)
    except SyntaxError as se: evalError = se 
    # litStr = litStr[:getattr(evalError, 'offset', len(litStr))]

    bracketPairs = {'{': '}', '[': ']'}
    closers, curCloser = [], ''
    for c in ''.join(litStr.split()):
        if c not in bracketPairs: break
        curCloser = bracketPairs[c] + curCloser
        closers.append(curCloser)

    for closer in closers:
        subStr = litStr.strip() 
        while subStr[1:]:
            try: return ast.literal_eval(subStr + closer)
            except SyntaxError: subStr = subStr[:-1].strip()

    if printError: print(repr(evalError))
    return defaultVal

# --- block 2 ---
testCases = [
    "[{'a' : 1, 'b' : 2}, {'a' : 1'}]",
    '[[1, 2, 3], [11, 12, 21]',
    """[{'a': [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 'b': [{'a':"""
]
for ti, tc in enumerate(testCases, 1):
    print(f'Case {ti}: {repr(tc)}\n  -  ----> ', end='')
    op = eval_brokenLiteral(tc)
    print(f'Output ---> {repr(op)}' if op else '', '\n\n---\n')
