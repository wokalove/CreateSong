from google.cloud import speech_v1p1beta1 as speech
from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\googleKey\mytone-330517-71e1f6a21c36.json"

class LanguageRecognition:
    def recognizeLanguageFromAudio(self, speech_file):

        client = speech.SpeechClient()

        first_lang = "en-US"
        second_lang = "pl"

        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            audio_channel_count=2,
            language_code=first_lang,
            alternative_language_codes=[second_lang],
        )

        print("Waiting for recognizing language...")
        response = client.recognize(config=config, audio=audio)


        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            language_code = result.language_code
            # print("-" * 20)
            # print(u"First alternative of result {}: {}".format(i, alternative))
            # print("Language Code: ",language_code)
            # print(u"Transcript: {}".format(alternative.transcript))
        return language_code


