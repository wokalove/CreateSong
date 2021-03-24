import speech_recognition as sr
import pyttsx3


class Speech:
    def __init__(self):
        '''Init '''
    def sayText(self,text):
        engine = pyttsx3.init()
        engine.setProperty('rate',125)
        engine.say(text)
        engine.runAndWait()

    def recognizeSpeech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Speak anything:')
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio,language='pl-PL')
                print('You said: {}'.format(text))
                self.sayText(text)
            except:
                print('Could not recognize your voice')

def main():
    speech_recognition = Speech().recognizeSpeech()

if __name__ == "__main__":
    main()
