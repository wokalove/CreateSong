from bs4 import BeautifulSoup 
import requests

class NotesParsing:

    def get_html_template(self):

        URL = 'https://www.liutaiomottola.com/formulae/freqtab.htm'
        # URL = 'https://pages.mtu.edu/~suits/notefreqs.html'
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, 'html.parser')

        rows = soup.find('table',{ "class" : "table-sm"}) # Extract and return first occurrence of tr
        columns = rows.find_all('td')
        notes_details =[]
        notes = []
        octaves = []
        frequencies = []

        for column in columns:
            notes_details.append(column.get_text().strip())
            notes.append(notes_details[::5])
            octaves.append(notes_details[::6])
            frequencies.append(notes_details[::7])

            # notes_filtered = [i for i in notes if 'Note Name' not in i]
            print(notes[0])



        # print(notes)
        



notes_parsing = NotesParsing()
notes_parsing.get_html_template()