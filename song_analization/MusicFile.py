
import os 
import random
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from ShowSongAnalization import ShowSongAnalization
import os.path
from pathlib import Path

class MusicFile:

    def __init__(self):
      self.dir_wav_uploads = ''

    def save_file(self, request):
        path = os.getcwd()
        self.dir_wav_uploads = path + "/music_files/"
        random_number = random.randrange(1,100)
        path = os.getcwd()

        file_name = 'myfile'+str(random_number)+'.wav'
        file_in_dir = self.dir_wav_uploads+file_name

        while(Path(file_in_dir) == True):
          file_name = 'myfile'+str(random_number)+'.wav'
          file_in_dir = self.dir_wav_uploads+file_name
        
        
        with open(file_in_dir, mode='bx') as file:
          file.write(request.get_data())
          file.close()
              
        recorded_file = path + "/music_files/"+file_name
        ShowSongAnalization().combineSpeechAndNotesRecognition(recorded_file, 'New song')

    def checkIfFileNameExists(self,path):
      exists = False

      if os.path.isfile(path):
        exists = True
      else:
        exists = False

      return exists
      


