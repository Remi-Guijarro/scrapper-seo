from flask_restful import Resource, reqparse
from flask import app, request,jsonify
import requests
from services.scrapper_seo import search_keywords_result_count

class SearchResults(Resource):
    def post(self):        
        params = request.json['keywords']
        return search_keywords_result_count(params), 200                
