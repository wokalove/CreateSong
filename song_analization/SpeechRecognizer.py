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
            whole_lyrics = []
            counter = 0

            for w in range(0, count_words):
                if(w % 6):
                    verse = words[counter:counter+words_limit]
                    verse_string= ' '.join(verse)
                    if not verse:
                        break
                    print(verse_string)
                    whole_lyrics.append(verse_string)
                    counter += 6
                
            return '\n'.join(whole_lyrics)
            

        except Exception as e:
            print("Exception:" +str(e))

    def recognizeLiveFromMicrophone(selfm):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Speak anything:')
            audio = recognizer.listen(source)
            engine = pyttsx3.init()
  
            # We can use file extension as mp3 and wav, both will work
            engine.save_to_file(audio, 'new_song.wav')

            print('Recognizing language...')
            language  = LanguageRecognition().recognizeLanguageFromAudio(audio)
            print('Recognized language:', language)
            
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
                print('NOTE: Detected silence is considered as the end of recording!')

    def textTransciption(self,file_name, detected_lang):
        #  detected_lang = LanguageRecognition().recognizeLanguageFromAudio(file_name)
         return SpeechRecognizer().textTranscriptionFromAudio(file_name,detected_lang)
         
    

# path = os.getcwd()
# file_name = path + "/music_files/wokal.wav"
# speech_recognition = SpeechRecognizer().textTranscriptionFromAudio(file_name,"pl")
# print(type(speech_recognition),speech_recognition)

   


# TODO
# SpeechRecognizer().recognizeLiveFromMicrophone()

