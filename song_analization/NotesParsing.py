from bs4 import BeautifulSoup 
import requests 
import re

class NotesParsing:

    def get_html_template(self,url):
        r = requests.get(url)
        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")

        notes = []
        frequencies = []
        
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            notes.append(tds[0].text.strip() + tds[1].text.strip())
            frequencies.append(tds[2].text.strip())
        return notes, frequencies
            
        # self.saveOutputToFile(notes, frequencies)

    def get_parsed_data(self):
        url = 'https://www.liutaiomottola.com/formulae/freqtab.htm'

        notes, freq = self.get_html_template(url)
        
        notes = [x for x in notes if x]
        freq = [float(x) for x in freq if x]

        return notes, freq
        


# URL = 'https://www.liutaiomottola.com/formulae/freqtab.htm'
notes_parsing = NotesParsing()
notes_parsing.get_parsed_data()



