import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from song_analization.LanguageRecognition import LanguageRecognition

class LanguageRecognitionTest(unittest.TestCase):
    def test_recognize(self):
        path = os.getcwd()
        file_name = path + "/music_files/wokal2.wav"
    
        self.assertAlmostEqual(LanguageRecognition().recognizeLanguageFromAudio(44100,file_name), "pl-pl")
        

if __name__ == '__main__':
    unittest.main()

# .assertEqual(one,two) means one == two (Our above example) 
# .assertTrue(expr) means boolean(expr) is True 
# .assertFalse(expr) means boolean(expr) is False 
# .assertIs(one,two) means one is two 
# notesParsing 
# SpeechRecognizer
#Music Note Detection