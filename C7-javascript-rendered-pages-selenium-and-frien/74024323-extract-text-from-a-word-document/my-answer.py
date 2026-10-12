# Code from my Stack Overflow answer https://stackoverflow.com/a/74051264 (posted 2022-10-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# from bs4 import BeautifulSoup

def getParaColor(para):
  try:
    return BeautifulSoup(
        para.paragraph_format.element.xml, 'xml'
    ).find('color').get('w:val')
  except:
    return ''

# --- block 2 ---
# import re

def splitParas(paras):
  ptc = [(
      p.text, getParaColor(p), p.paragraph_format.element.xml
  ) for p in paras]
  curSectn = 'UNKNOWN'
  splitBlox = [{}]

  for pt, pc, px in ptc:
    # double-check for missing text
    xmlText = BeautifulSoup(px, 'xml').text
    xmlText = ' '.join([s for s in xmlText.split() if s != ''])
    if len(xmlText) > len(pt): pt = xmlText

    # initiate
    if not pt:
      if splitBlox[-1] != {}:
        splitBlox.append({})
      continue
    if pc == '20752E':
      curSectn = pt.strip()
      continue
    if splitBlox[-1] == {}:
      splitBlox[-1]['section'] = curSectn
      splitBlox[-1]['raw'] = [] 
      splitBlox[-1]['Name'] = []
      splitBlox[-1]['address_raw'] = []

    # collect
    splitBlox[-1]['raw'].append(pt)   
    if pc == 'D12229':
      splitBlox[-1]['Name'].append(pt)
    elif re.search("^Te.*:.*", pt):
      splitBlox[-1]['tel_raw'] = re.sub("^Te.*:", '', pt).strip()
    elif re.search("^Mob.*:.*", pt):
      splitBlox[-1]['mobile_raw'] = re.sub("^Mob.*:", '', pt).strip()
    elif pt.startswith('Email:') or re.search(".*[@].*[.].*", pt):
      splitBlox[-1]['Email'] = pt.replace('Email:', '').strip()
    else:
      splitBlox[-1]['address_raw'].append(pt)

  # some cleanup
  if splitBlox[-1] == {}: splitBlox = splitBlox[:-1]
  for i in range(len(splitBlox)):
    addrsParas = splitBlox[i]['address_raw'] # for later

    # join lists into strings
    splitBlox[i]['Name'] = ' '.join(splitBlox[i]['Name'])
    for k in ['raw', 'address_raw']:
      splitBlox[i][k] = '\n'.join(splitBlox[i][k])

    # search address for City, State and PostCode
    apLast = addrsParas[-1].split(',')[-1]
    maybeCity = [ap for ap in addrsParas if '–' in ap]
    if '–' not in apLast:
      splitBlox[i]['State'] = apLast.strip()
    if maybeCity:
      maybePIN = maybeCity[-1].split('–')[-1].split(',')[0]
      maybeCity = maybeCity[-1].split('–')[0].split(',')[-1]
      splitBlox[i]['City'] = maybeCity.strip()
      splitBlox[i]['PostCode'] = maybePIN.strip()

    # add mobile to tel
    if 'mobile_raw' in splitBlox[i]:
      if 'tel_raw' not in splitBlox[i]:
        splitBlox[i]['tel_raw'] = splitBlox[i]['mobile_raw']
      else:
        splitBlox[i]['tel_raw'] += (', ' + splitBlox[i]['mobile_raw'])
      del splitBlox[i]['mobile_raw']

    # split tel [as needed]
    if 'tel_raw' in splitBlox[i]:
      tel_i = [t.strip() for t in splitBlox[i]['tel_raw'].split(',')] 
      telNum = []

      for t in range(len(tel_i)):
        if '/' in tel_i[t]:
          tns = [t.strip() for t in tel_i[t].split('/')]
          tel1 = tns[0]
          telNum.append(tel1)
          for tn in tns[1:]:
            telNum.append(tel1[:-1*len(tn)]+tn)
        else:
          telNum.append(tel_i[t])

      splitBlox[i]['Tel_1'] = telNum[0]
      splitBlox[i]['Tel'] = telNum[0] if len(telNum) == 1 else telNum

  return splitBlox

# --- block 3 ---
#import docx
#import pandas 

content = docx.Document('HE Distributors.docx')
# pandas.DataFrame(splitParas(content.paragraphs)) # <--all Columns
pandas.DataFrame(splitParas(content.paragraphs))[[
    'section', 'Name', 'address_raw', 'City', 
    'PostCode', 'State', 'Email', 'Tel_1', 'tel_raw'
]]
