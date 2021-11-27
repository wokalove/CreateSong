import os
from SpeechRecognizer import SpeechRecognizer
from MusicNoteDetection import MusicNoteDetection
from ConvertSongToPdf import ConvertSongToPdf
from LanguageRecognition import LanguageRecognition

class ShowSongAnalization:
    def combineSpeechAndNotesRecognition(self, audio_file, title, sample):
        sr = SpeechRecognizer()
        detected_lang = LanguageRecognition().recognizeLanguageFromAudio(sample,audio_file)
        text = sr.textTransciption(audio_file, detected_lang)
        notes = MusicNoteDetection().note_detect(audio_file)
        
        # ConvertSongToPdf().convertDataToPdf(text, notes, title, detected_lang)

if __name__ == "__main__":
    path = os.getcwd()
    eng_sample = 44100
    es_sample = 32000

    file_name_eng = path + "/test_music_files/english.wav"
    file_name_es = path + "/test_music_files/espanol.wav"
    title = "New song"

    # ShowSongAnalization().combineSpeechAndNotesRecognition(file_name_eng, title, eng_sample)
    
    ShowSongAnalization().combineSpeechAndNotesRecognition(file_name_es, title, es_sample)
    