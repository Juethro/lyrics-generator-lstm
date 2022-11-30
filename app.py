from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from predict import *

app = Flask(__name__)
api = Api(app)
CORS(app)

rest = {
    'out1': 'kokok',
    'out2': 'wawaawa',
    'out3': 'duarrr',
    'out4': 'ancok'
}

class Home(Resource):
    def get(self):
        return rest, 200

    def post(self):
        # ab = request.get_json()
        return rest, 200

api.add_resource(Home, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
