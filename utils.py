import roman
import re

from num2words import num2words

mapping_normalization = [
  #[ u'\xa0 ', u' ' ],
#  [ u'«\xa0', u'«' ],
#  [ u'\xa0»', u'»' ],
  #[ u'\xa0' , u' ' ],
  [ u'M.\u00a0'   , u'Monsieur ' ],
  [ u'M. '   , u'Monsieur ' ],
  [ u'Mme\u00a0'  , u'Madame ' ],
  [ u'Mme '  , u'Madame ' ],
  [ u'Mlle\u00a0' , u'Mademoiselle ' ],
  [ u'Mlle ' , u'Mademoiselle ' ],
  [ u'Mlles\u00a0', u'Mademoiselles ' ],
  [ u'Mlles ', u'Mademoiselles ' ],
  [ u'%', u'pourcent' ],
]

superscript_chars_mapping = {
  '0': u'\u2070',
  '1': u'\u00b9',
  '2': u'\u00b2',
  '3': u'\u00b3',
  '4': u'\u2074',
  '5': u'\u2075',
  '6': u'\u2076',
  '7': u'\u2077',
  '8': u'\u2078',
  '9': u'\u2079',

  '0 ': u'\u2070 ',
  '1 ': u'\u00b9 ',
  '2 ': u'\u00b2 ',
  '3 ': u'\u00b3 ',
  '4 ': u'\u2074 ',
  '5 ': u'\u2075 ',
  '6 ': u'\u2076 ',
  '7 ': u'\u2077 ',
  '8 ': u'\u2078 ',
  '9 ': u'\u2079 ',

  'o': 'uméro',
  '°': 'uméro',
  'os': 'uméros',
  '°s': 'uméros',
  '° s': 'uméros',
  u'°\u00a0s': 'uméros',
  'o s': 'uméros',
  u'o\u00a0s': 'uméros',
  's': 's',
  'ter': 'ter',
  'gr': 'onseigneur',

  ' ': ' ',

  # Those should be in sync with ORDINAL_REGEX
  'e': 'ieme',
  'è': 'ieme ',
  'e,': 'ieme,',
  'èm': 'ieme ',
  'e ': 'ieme ',
  'e –': 'ieme –',
  'r': 'ier',
  'er': 'ier',
  'er ': 'ier ',
  'er.': 'ier.',
  'er,': 'ier,',
  'ER': 'ier',
  'Er': 'ier',
  'er –': 'ier –',
  're': 'iere',
  'ère': 'iere',
  'ère': 'iere',
  'ème': 'ieme',
  'éme': 'ieme',
  'ème ': 'ieme',
  'eme': 'ieme',
}

ORDINAL_REGEX = re.compile("(\d+)([ieme|ier|iere]+)")

subscript_chars_mapping = {
  '0': u'\u2080',
  '1': u'\u2081',
  '2': u'\u2082',
  '3': u'\u2083',
  '4': u'\u2084',
  '5': u'\u2085',
  '6': u'\u2086',
  '7': u'\u2087',
  '8': u'\u2088',
  '9': u'\u2089',

  '0 ': u'\u2080 ',
  '1 ': u'\u2081 ',
  '2 ': u'\u2082 ',
  '3 ': u'\u2083 ',
  '4 ': u'\u2084 ',
  '5 ': u'\u2085 ',
  '6 ': u'\u2086 ',
  '7 ': u'\u2087 ',
  '8 ': u'\u2088 ',
  '9 ': u'\u2089 ',

  'e': u'\u2091',
  ' ': '',
}

WORD_REGEX = re.compile("[^\w\d\'\-]+")
def splitIntoWords(text):
    return WORD_REGEX.split(text)

NUMS_REGEX = re.compile("(\d+,?\u00A0?\d+)|(\d+\w+)|(\d)*")
def getNumbers(text):
    return NUMS_REGEX.split(text)

def getRomanNumbers(ch):
  ROMAN_CHARS = "XVI"
  ro  = ''
  ros = 0
  for i in range(len(ch)):
    c = ch[i]
    if c in ROMAN_CHARS:
      #print('len(ro)="{}" c="{}" ch[i-1]="{}" ro="{}" ch="{}"'.format(len(ro), c, ch[i-1], ro, ch))
      if len(ro) == 0 and not ch[i-1].isalpha():
        ro  = c
        ros = i
      else:
        if len(ro) > 0 and ch[i-1] in ROMAN_CHARS:
          ro += c
    else:
      if len(ro) > 0:
        if not c.isalpha():
          #print('getRomanNumbers', ch, ro)
          yield ch[ros-1], ch[i], ro
        ro  = ''
        ros = i

  if len(ro) > 0:
    #print('getRomanNumbers final', ch, "|||", ro)
    yield ch[ros-1], '', ro

def filter_numbers(inp):
  finalinp = ''

  #print('filter_numbers', 'inp=', inp)

  for e in getNumbers(inp):
    if not e:
      continue

    newinp = e
    #print('filter_numbers', 'e=', e)

    try:
      ee = ''.join(e.split())
      if int(e) > 0:
        #print('filter_numbers', 'INT:BEFORE', 'ee=', ee, 'newinp=', newinp)
        newinp = num2words(int(ee), lang='fr')
        #print('filter_numbers', 'INT:AFTER', 'ee=', ee, 'newinp=', newinp)
    except ValueError:
      try:
        ee = ''.join(e.replace(',', '.').split())
        if float(ee):
          #print('filter_numbers', 'FLOAT:BEFORE', 'ee=', ee, 'newinp=', newinp)
          newinp = num2words(float(ee), lang='fr')
          #print('filter_numbers', 'FLOAT:AFTER', 'ee=', ee, 'newinp=', newinp)
      except ValueError:
        matches = ORDINAL_REGEX.match(e)
        #print('filter_numbers', 'ORDINAL', 'e=', e, matches)
        if matches:
          newinp = num2words(int(matches.group(1)), ordinal=True, lang='fr')

    finalinp += newinp

    #print('filter_numbers', 'e=', e, 'newinp=', newinp, 'finalinp=', finalinp)

  return finalinp

def maybe_normalize(value):
  for norm in mapping_normalization:
    value = value.replace(norm[0], norm[1])

  for ro_before, ro_after, ro in getRomanNumbers(value):
    #print('maybe_normalize', 'ro=', ro)
    try:
      value = value.replace(ro_before + ro + ro_after, ro_before + str(roman.fromRoman(ro)) + ro_after)
    except roman.InvalidRomanNumeralError as ex:
      print(ex)
      pass

  return value

def maybe_translate(element, mapping):
  value = maybe_normalize(element.nodeValue)

  bsp  = value.count(' ')
  nbsp = value.count('\u00a0')
  if value in mapping:
    return mapping[value]
  else:
    nvalue = value.strip()
    if nbsp > 0:
      if nbsp == 1 and value.find('\u00a0') == len(value) - 1:
        if nvalue in mapping:
          return mapping[nvalue] + u'\u00a0'
      if nbsp == 1 and value.find('\u00a0') == len(value) - 2 and value.find(' ') == len(value) - 1:
        if nvalue in mapping:
          return mapping[nvalue] + u'\u00a0'
    if bsp > 0:
      if bsp == 1 and value.find(' ') == len(value) - 1:
        if nvalue in mapping:
          return mapping[nvalue] + u' '

  if element.nodeValue.strip().isnumeric() and str(int(element.nodeValue.strip())) == element.nodeValue.strip():
    pass
  else:
    print("NOT TRANSLATED: '{}' => '{}'".format(element.nodeValue, value))
    for c in value:
      print("value: '{}' == {}".format(c, ord(c)))
  return value

def recursive_text(root, finaltext=""):
  if root.nodeName == 'br':
    return ' '
  else:
    for c in root.childNodes:
      if c.nodeType == c.TEXT_NODE:
        if root.nodeName == 'exposant':
          finaltext += maybe_translate(c, superscript_chars_mapping)
        elif root.nodeName == 'indice':
          finaltext += maybe_translate(c, subscript_chars_mapping)
        else:
          finaltext += maybe_normalize(c.nodeValue)
      if c.nodeType == c.ELEMENT_NODE:
        finaltext += recursive_text(c)
  return finaltext
