import speech_recognition as sr
import pyttsx3
import os
from LanguageRecognition import LanguageRecognition

import string
from langcodes import *


class SpeechRecognizer:
    def __init__(self):
        '''Init '''

    def sayText(self,text):
        engine = pyttsx3.init()
        engine.setProperty('rate',125)
        engine.say(text)
        engine.runAndWait()
        
  
    def textTranscriptionFromAudio(self,audio_file, detected_lang):
        r = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio,language=detected_lang)

            print("Language:",Language.get(detected_lang).autonym())

            words = s.split()
            count_words = len(words)

            words_limit = 6
            verse = words[:words_limit]

            counter = 0
            for w in range(0, count_words):
                if(w % 6):
                    verse = words[counter:counter+words_limit]
                    if not verse:
                        break
                    print(verse)
                    counter += 6
                    

        except Exception as e:
            print("Exception:" +str(e))

    def recognizeSpeech(selfm,language):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Speak anything:')
            audio = recognizer.listen(source)

            try:
                if language == 'PL':
                    text = recognizer.recognize_google(audio,language='pl-PL')
                else:
                    text = recognizer.recognize_google(audio,language='en-US')

                print('You said: {}'.format(text))
                self.sayText(text)

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service")
            except:
                print('Could not recognize your voice or tts failed')
    def textTransciption(self,file_name):
         detected_lang = LanguageRecognition().recognizeLanguageFromAudio(file_name)
         SpeechRecognizer().textTranscriptionFromAudio(file_name,detected_lang)

# def main():
#     # language = input('Select language:')
#     # speech_recognition = Speech().recognizeSpeech(language)
#     path = os.getcwd()
#     file_name = path + "/wokal.wav"

   

# if __name__ == "__main__":
#     main()
