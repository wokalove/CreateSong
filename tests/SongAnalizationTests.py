import unittest
import os 
from song_analization.LanguageRecognition import LanguageRecognition


class LanguageRecognitionTest(unittest.TestCase):
    def test_recognize(self):
        path = os.getcwd()
        file_name = path + "/music_files/wokal2.wav"
        self.assertAlmostEqual(LanguageRecognition().recognizeLanguageFromAudio(file_name), "pl-pl")
        # self.assertAlmostEqual(LanguageRecognition().recognizeLanguageFromAudio(file_name), "en-en")

