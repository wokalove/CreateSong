from fpdf import FPDF 
import random
import os

class ConvertSongToPdf:
    def getValues(self):
        ''''''
    def convertDataToPdf(self):
        
        pdf = FPDF() 
        
        pdf.add_page() 
        
        pdf.set_font("Arial", size = 25) 
        
        # create a cell 
        pdf.cell(200, 10, txt = "JournalDev", 
                ln = 1, align = 'C') 
        
        pdf.cell(200, 10, txt = "Welcome to the world of technologies!", 
                ln = 2, align = 'C') 

        # TODO replace by name song or get next number of created song
        random_number = random.random()
        path = os.getcwd()

        pdf.output(path+"/song_pdfs/song"+str(random_number)+".pdf") 


ConvertSongToPdf().convertDataToPdf()