from requests_html import HTML
import urllib

class NotesParsing:

    def get_html_template():
        url = "https://www.liutaiomottola.com/formulae/freqtab.htm"
        template = urllib.request.urlopen(url).read()

        with open('simple.html') as html_template:
            source = html_template.read()
            html = HTML(html=source)
        match = html.find('title')
        print(match)

