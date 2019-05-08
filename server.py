from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#from flask.ext.jsonpify import jsonpify
from linkedin_api import Linkedin
import os

app = Flask(__name__)
api = Api(app)

class Messages(Resource):
    def get(self, profileName):
        linkedin = Linkedin('userName', 'password')
        profile = linkedin.get_profile('leandrovalido')
        firstName = profile['firstName']
        print(firstName)
        profile_urn_id = profile['profile_id']
        conversation_details = linkedin.get_conversation_details(profile_urn_id)
        conversation_id = conversation_details['id']
        return linkedin.send_message(conversation_urn_id=conversation_id, message_body="No I will not be your technical cofounder")

class Diagnostics(Resource):
    def get(self):
        return "ping"

api.add_resource(Messages, '/messages/<profileName>') # Route_1
api.add_resource(Diagnostics, '/diagnostics')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(port=port,host='0.0.0.0',debug=True)
     