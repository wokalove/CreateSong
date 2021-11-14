import os
from SpeechRecognizer import SpeechRecognizer
from MusicNoteDetection import MusicNoteDetection
from ConvertSongToPdf import ConvertSongToPdf
from LanguageRecognition import LanguageRecognition

class ShowSongAnalization:
    def combineSpeechAndNotesRecognition(self, audio_file, title):
        sr = SpeechRecognizer()
        detected_lang = LanguageRecognition().recognizeLanguageFromAudio(audio_file)
        text = sr.textTransciption(file_name, detected_lang)
        notes = MusicNoteDetection().note_detect(file_name)
        
        ConvertSongToPdf().convertDataToPdf(text, notes, title, detected_lang)
	

if __name__ == "__main__":
    path = os.getcwd()
    file_name = path + "/music_files/polska.wav"
    title = "New song"
    ShowSongAnalization().combineSpeechAndNotesRecognition(file_name, title)
    
    