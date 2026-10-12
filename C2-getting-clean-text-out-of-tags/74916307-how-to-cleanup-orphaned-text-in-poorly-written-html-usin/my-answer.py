# Code from my Stack Overflow answer https://stackoverflow.com/a/74935343 (posted 2022-12-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from bs4 import BeautifulSoup

## just a function I use often to reduce whitespace ##
def miniStr(obj, lineSep=' ', wordSep=' '):
    return lineSep.join(wordSep.join(
        w for w in l.split() if w) for l in str(obj).splitlines() if l.strip())


## the solution ##
def containStrings(inpObj, asHtmlStr=True, tCont='div'): 
    ### initiate [main] container - "fixed" html will be added to this ###
    cDiv = BeautifulSoup('<div></div>', "html.parser").div 

    ### format inputs ###
    tCont = str(tCont) if str(tCont).isalpha() else 'div' # can only contain letters
    if not isinstance(inpObj, type(cDiv)): 
        # parses html strings twice [first time to correct errors - like open tags] 
        inpObj = BeautifulSoup(
            f'<div>{BeautifulSoup(inpObj, "html.parser")}</div>', "html.parser").div

    ### loop through input and fill up cDiv ###
    for c in inpObj.children:
        if isinstance(c, str): 
            c = BeautifulSoup(f'<{tCont}>{c}</{tCont}>', "html.parser").find(tCont)
        cDiv.append(BeautifulSoup(c.prettify(), "html.parser").find(c.name))

    return cDiv.prettify()[6:-7] if asHtmlStr else cDiv

# --- block 2 ---
# the inputs [before processing]
print('\n\n'.join(f'<!--from line{i+1}-->\n'+'\n'.join(
    [miniStr(c, '') for c in BeautifulSoup(l,'html.parser').children]
) for i, l in enumerate(linesList)))

# --- block 3 ---
# the outputs [after processing]
print('\n\n'.join(f'<!--from line{i+1}-->\n'+'\n'.join(
    [miniStr(c, '') for c in containStrings(l, False).children]
) for i, l in enumerate(linesList)))
