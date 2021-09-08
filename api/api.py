from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from resources.User import User
from resources.SearchResults import SearchResults

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(SearchResults, '/search')

if __name__ == '__main__':
    app.run()