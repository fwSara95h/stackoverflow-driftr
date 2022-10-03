---
title: "Can you search groups of text using for x in python?"
site: stackoverflow
question_id: 73938415
answer_id: 73939165
url: https://stackoverflow.com/a/73939165
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-03T18:00:14Z
last_edited: 2022-10-03T23:40:35Z
revisions: 3
revision_history: https://stackoverflow.com/posts/73939165/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b45da76c01f2fb10f088fe73d4c8736b59000026ef617cfc6689f6506f52936c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73939165>, 2022-10-03, last edited 2022-10-03; score 0. Text as retrieved 2026-10-12.

Assuming the variable names in the compressed text always have only one letter, which is always at the beginning of the name, and that whitespaces can be ignored, you can use a function like:

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

then you can just loop through like `for x in vnSplit(Text):...`

Here are some sample outputs from the function: 

    ("S V1XV2E") ---> ['S', 'V1', 'X', 'V2', 'E']
    ("SV2Exyz") ---> ['S', 'V2', 'E', 'x', 'y', 'z']
    ("abc324k_1") ---> ['a', 'b', 'c324', 'k_1']

[Printed using `for ct in cTexts: print(f'("{ct}") ---> {vnSplit(ct)}')`]

EDIT: if you want to go by a dictionary instead of the single-letter format, you could do something like:

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
It's called the same way, but dependent on `startVar()` and the [output][1] is in a different format (easily changed by editing the `return`); but with this, the compression **must** adhere to the dictionary


  [1]: https://i.sstatic.net/Xy1ad.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rambo](https://stackoverflow.com/users/20151512)** (2022-10-03): Interesting... is there a way to allow for more than one letter per variable name in this function?
- **me** (2022-10-03): @Rambo then I might approach it in a different way - maybe with a reference list of possible variable "prefixes" to check through instead of the simpler `isalpha`, but the pattern can't be *too* confusing - like if both 'e', 'x' and 'ex' are possible prefixes, should 'ex2' return ['e', 'x2'] or ['ex2']? so, I wouldn't know what to do with overlapping patterns, but otherwise it's doable
- **[Rambo](https://stackoverflow.com/users/20151512)** (2022-10-03): I see what you're getting at, do you think I could integrate a dictionary in the place of `isalpha`, and if so may I ask how?
- **me** (2022-10-03): @Rambo I've added in an edit. The process is a bit different from the previous, but I think it can actually handle similar compressions such both "e" and "ex" **as long as** the longer/longest one ["ex"] comes first in the dictionary
