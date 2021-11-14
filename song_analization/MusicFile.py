from pydub import AudioSegment
import os 
import json
import urllib.request
# from werkzeug import secure_filename

uploads_dir = os.path.join(os.path.dirname(__file__),'..', 'uploads')
# os.makedirs(uploads_dir)

class ExportJson:
    def get_data_from_request(self, data):
        data.save(os.path.join(uploads_dir, data.filename))
        print(type(data),data)
        
        # for key, value in json_dict.items():
        #     print(key, '\t', value)
        # output = json.loads(data)
        
class MusicFile:
    def save_file_from_url(self):
        path = os.getcwd()
        music_files_dir = path + "/music_files/"

        music_file = urllib.request.URLopener()
        music_file.retrieve("blob:http://127.0.0.1:8000/9d4a9897-3edb-4e0e-9c8d-f3c9562aa45a", music_files_dir+"file.wav")

        # block_blob_service = BlockBlobService(account_name='myaccount', account_key='mykey')

        # block_blob_service.get_blob_to_path('mycontainer', 'myblockblob', 'out-sunset.png')
    def check_if_file_is_wav(self):
        '''TODO'''

# MusicFile().save_file_from_url()


