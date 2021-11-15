
import os 
import random
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from ShowSongAnalization import ShowSongAnalization

class MusicFile:
    def save_file(self, request):
        path = os.getcwd()
        dir_wav_uploads = path + "/music_files/"
        random_number = random.randrange(1,10)
        path = os.getcwd()

        file_name = 'myfile'+str(random_number)+'.wav'
        with open(dir_wav_uploads+file_name, mode='bx') as file:
          file.write(request.get_data())
          file.close()
        
        recorded_file = path + "/music_files/"+file_name
        ShowSongAnalization().combineSpeechAndNotesRecognition(recorded_file, 'New song')

    def check_if_file_is_wav(self):
        '''TODO'''

# MusicFile().save_file_from_url()


