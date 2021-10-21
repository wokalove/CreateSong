import re
import requests
from bs4 import BeautifulSoup 

URL = 'https://www.liutaiomottola.com/formulae/freqtab.htm'
content = requests.get(URL)

			
text = ''' Note Name	Octave	Frequency (Hz)	Wavelength (M)*	Comment  kurła typowo or not'''
regexAvoid = '(?<!\b(?:and| or|not))\b(?!(?:and|or|not)\b)'
regexMatch = '\bNote Name\b|\bOctave\b|\bFrequency (Hz)\b|\bWavelength (M)*	Comment\b'

# text = BeautifulSoup(content.text, 'html.parser')
pattern = re.compile(r'td')
matches = pattern.finditer(text)

for match in matches:
    print(match)

