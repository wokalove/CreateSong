import speech_recognition as sr
import pyttsx3


class SpeechRecognizer:
    def __init__(self):
        '''Init '''

    def sayText(self,text):
        engine = pyttsx3.init()
        engine.setProperty('rate',125)
        engine.say(text)
        engine.runAndWait()

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

def main():
    language = input('Select language:')
    speech_recognition = Speech().recognizeSpeech(language)

if __name__ == "__main__":
    main()
