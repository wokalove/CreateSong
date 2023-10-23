import unittest
import os
import sys

#locate song_analization module
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from song_analization.LanguageRecognition import LanguageRecognition
from song_analization.MusicFile import MusicFile
from song_analization.ConvertSongToPdf import ConvertSongToPdf


class SongAnalizationTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SongAnalizationTests, self).__init__(*args, **kwargs)
        self.path = os.getcwd()
        self.file_name =  self.path + "/test_music_files/polska.wav"
        self.language_code = 'pl-pl'

    # def test_recognize_language_from_audio(self):
    #     #define sample rate of an audio
    #     sample_rate = 44100
    #     #check if result is as expected
    #     self.assertAlmostEqual(LanguageRecognition().recognizeLanguageFromAudio(sample_rate,self.file_name), self.language_code)

    def test_check_if_file_exists(self):
        #self.file_name - path to file which exists
        #check if result is True
        self.assertTrue(MusicFile().checkIfFileNameExists(self.file_name))

    def test_check_if_file_no_exists(self):
        #override self.file_name - path to file which no exist
        self.file_name =  self.path + "/test_music_files/non_existing_file.wav"
        #check if result is False
        self.assertFalse(MusicFile().checkIfFileNameExists(self.file_name))
    
    # def test_pdf_generated_headers(self):
    #     expected_headers =  ("Nowa piosenka", "Rozpoznane dźwięki", "Słowa piosenki")
    #     #check if result is as expexted headers tuple
    #     self.assertAlmostEqual(ConvertSongToPdf().translation_from_json(self.language_code),expected_headers)

if __name__ == '__main__':
    unittest.main()
