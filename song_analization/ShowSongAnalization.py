import os
from SpeechRecognizer import SpeechRecognizer
from MusicNoteDetection import MusicNoteDetection

class ShowSongAnalization:
    def combineSpeechAndNotesRecognition(self, audio_file):
        sr = SpeechRecognizer()
        sr.textTransciption(file_name)
        MusicNoteDetection().note_detect(file_name)
	

if __name__ == "__main__":
    path = os.getcwd()
    file_name = path + "/music_files/wokal2.wav"

    ShowSongAnalization().combineSpeechAndNotesRecognition(file_name)
    
    