import os
from SpeechRecognizer import SpeechRecognizer

class ShowSongAnalization:
    def combineSpeechAndNotesRecognition(self, audio_file):
        sr = SpeechRecognizer()
        sr.recognizeFromAudio(file_name)
	

if __name__ == "__main__":
    path = os.getcwd()
    file_name = path + "/wokal.wav"
    ShowSongAnalization().combineSpeechAndNotesRecognition(file_name)
    