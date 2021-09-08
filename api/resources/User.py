from flask_restful import Resource, reqparse

class User(Resource):
    def get(self):
        return {'data': {
         'name' : 'remi',
         'lastname' : 'guijarro espinosa',
         'age' : 23   
        }}, 200