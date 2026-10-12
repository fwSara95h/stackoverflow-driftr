# Code from my Stack Overflow answer https://stackoverflow.com/a/73939165 (posted 2022-10-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def vnSplit(cText):
  #just in case:
  cText = str(cText) 
  if cText == '':
    return []
  #remove whitespace
  cText = ''.join(cText.split())

  varNames = []
  varName = cText[0]
  ctLen = len(cText)
  for i in range(1, ctLen):
    if cText[i].isalpha():
      varNames.append(varName)
      varName = '' 

    if i == ctLen - 1: #last char
        varNames.append(varName + cText[i])
    else: 
      varName = varName + cText[i]

  return varNames

# --- block 2 ---
def startVar(string, vDict):
  possVars = [v for v in vDict if string.startswith(v)]
  return possVars[0] if possVars else False

def vnExtract(cText, vDict): 
  cText = str(cText) #just in case

  #remove whitespace - but not on original
  ct = ''.join(cText.split())

  compressedVars = [] 
  extractedVars = []
  varName = ''
  varSuffix = ''
  while len(ct) > 0: 
    possVar = startVar(ct, vDict)
    if possVar:
      if varName != '': 
        compressedVars.append(varName + varSuffix)
        if varSuffix != '' and varSuffix[0].isalpha(): #OPTIONAL
          varSuffix = '_' + varSuffix #OPTIONAL
        extractedVars.append(vDict[varName] + varSuffix)
      varName = possVar
      varSuffix = ''
      ct = ct.replace(varName, '', 1)
    else:
      varSuffix = varSuffix + ct[0]
      ct = ct[1:]

    if ct == '' and varName in vDict:
      compressedVars.append(varName + varSuffix)
      if varSuffix != '' and varSuffix[0].isalpha(): #OPTIONAL
        varSuffix = '_' + varSuffix #OPTIONAL
      extractedVars.append(vDict[varName] + varSuffix)

  return {
      'compressed_text': cText,
      'compressed_vars': compressedVars,
      'extracted_vars': extractedVars
  }
