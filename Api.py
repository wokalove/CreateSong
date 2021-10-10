from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)


@app.route("/user/create-song")
def hello():
   return jsonify(request.args.get('data'))

if __name__ == "__main__":
  CORS(app.run())


#CORS
# https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0