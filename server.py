from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#from flask.ext.jsonpify import jsonpify
from linkedin_api import Linkedin

app = Flask(__name__)
api = Api(app)

class Messages(Resource):
    def get(self, profileName):
        linkedin = Linkedin('digitkauconsulting@gmail.com', 'R35bpmdq')
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
     app.run(port='5002')
     