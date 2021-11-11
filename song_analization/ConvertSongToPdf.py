from fpdf import FPDF 
import random
import os
import json

class ConvertSongToPdf:
    def __init__(self):
        self.path = os.getcwd()
        
    def translation_from_json(self,detected_language):
        json_file = self.path+"/translations/pdfTranslations.json"
        translations = json.loads(open(json_file,encoding='utf-8').read())

        for language, text in translations['languages'].items():
                if language == detected_language:
                        notes_header = translations['languages'][language]['notes'] 
                        lyrics_header = translations['languages'][language]['lyrics'] 
                        break
        return notes_header, lyrics_header
        
    def convertDataToPdf(self, lyrics, notes, title, detected_lang):
                
        pdf = FPDF() 
        pdf.add_page() 
        notes_header, lyrics_header = self.translation_from_json(detected_lang)
        
        path = os.getcwd()
        font_dir = path + "/fonts/"

        pdf.add_font('DejaVu', '', font_dir+'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 14)
        

        pdf.cell(200, 10, txt = title,
                ln = 1, align = 'C') 

        pdf.cell(200, 10, txt = notes_header,
                ln = 1, align = 'L') 
        
        
        for n in notes.split(','):
            pdf.write(8, n)
            pdf.ln(8)

        pdf.cell(200, 10, txt = lyrics_header,
                ln = 1, align = 'L') 
        
        for txt in lyrics.split('\n'):
            pdf.write(8, txt)
            pdf.ln(8)


        # TODO replace by name song or get next number of created song
        random_number = random.random()
        path = os.getcwd()

        # pdf.output(path+"/song_pdfs/song"+str(random_number)+".pdf") 
        pdf.output(path+"/song_pdfs/song.pdf") 


# ConvertSongToPdf().translation_from_json("en-en")