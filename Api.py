from flask import Flask, request,jsonify
from flask_cors import CORS
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from song_analization.MusicFile import ExportJson


app = Flask(__name__)

# @app.route("/user/create-song", methods=['POST', 'OPTIONS'])
@app.route("/user/create-song", methods=['POST'])
def hello():
  #  return jsonify("Bu")
  #  content = request.get_json(silent=True)
   
   if request.method == 'POST':
     print(request.files['file'])
     ExportJson().get_data_from_request(request.files['file'])
   return "json got"
  

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Origin, Accept, X-Requested-With, X-CSRF-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE, OPTIONS')
    return response

if __name__ == "__main__":
  CORS(app.run(debug=True), resources={r"/user/create-song": {"origins": "*"}})
  data = request.args.get("data")
  print(data)
  


#CORS
# https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0