from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

#https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell/
#https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment