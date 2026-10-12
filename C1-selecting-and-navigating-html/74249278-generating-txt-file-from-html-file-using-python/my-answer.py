# Code from my Stack Overflow answer https://stackoverflow.com/a/74257514 (posted 2022-10-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# when you want an attribute value or something else rather than just innerText
not_text = {'img': ['alt'], 'br': [f'"\n"']}

# for elements with indent
indentsRef = {'li': 4}

# "Block-level Elements" from https://www.w3schools.com/html/html_blocks.asp 
bTags = ['address', 'article', 'aside', 'blockquote', 'canvas', 'dd', 'div', 'dl', 'dt', 'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'li', 'main', 'nav', 'noscript', 'ol', 'p', 'pre', 'section', 'table', 'tfoot', 'ul', 'video']

def html_to_text(hNode, ble=bTags, indents=indentsRef, specialTags=not_text): 
    # returns (isBlockElement: bool, innerText: str)

    blePlus = ble + list(specialTags.keys()) 

    if hNode.name is None or (hNode.name not in blePlus and not hNode.find(blePlus)): 
        return (False, hNode.get_text(' ', strip=True)) 

    cnIndent = ' '*sum([
        indents[t.name] for t in (list(hNode.parents) + [hNode]) 
        if t.name in indents
    ])

    if hNode.name in specialTags: 
        attribs = []
        for attrib in specialTags[hNode.name]: 
            if attrib == '':
                attribs.append(hNode.get_text(' ', strip=True)) 
            elif attrib[0] == attrib[-1] == '"':
                attribs.append(attrib[1:-1]) 
            #  elif attrib == '>__': # can add more 
            else: attribs.append(hNode.get(attrib, ''))

        joiner = ' ' # ?customize for multi-attribute
        return (hNode.name in ble, joiner.join(attribs))

    if not hNode.find(blePlus): 
      nodeText = [
          (cnIndent + l) for l in hNode.get_text(' ', strip=True).split('\n')
      ]
      return (True, '\n'.join(nodeText))

    nodeText = [] 
    prevChild = None
    for c in hNode.children:
        c_h2t = html_to_text(c) 

        space_before = cnIndent 
        if prevChild and (not prevChild[0]) and c_h2t[0]: 
            space_before = '\n' + space_before
        space_after = '\n' if c_h2t[0] else ' '

        nodeText.append(space_before + c_h2t[1] + space_after)
        prevChild = c_h2t
    return (hNode.name in ble, ''.join(nodeText))

# --- block 2 ---
print(html_to_text(bodyHtml)[1])
