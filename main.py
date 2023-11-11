from flask import Flask, request, jsonify
from flask_restful import Api, Resource,reqparse,abort
import requests
from GoogleSearch import *
import numpy as np
import pandas as pd
import random

app = Flask(__name__)
api = Api(app)

driver_path = r"C:\Users\Administrator\Desktop\Arvan\chromedriver-win64\chromedriver.exe" 

class ScrapeURL(Resource):
    def get(self,ProductName,SiteName):
        try:
            google_scrapper = ScrapeGoogle(driver_path)
            google_scrapper.start_driver()
            time.sleep(random.randint(2,5))
            Url = google_scrapper.find_proper_link(ProductName,SiteName)
            google_scrapper.stop_driver()
            response = {"Url":Url}
            return response,200
        except Exception as e:
            return {"error":str(e)}, 500

api.add_resource(ScrapeURL,"/ScrapeUrl/<string:ProductName>/<string:SiteName>")

if __name__ == "__main__":
    app.run(debug = False)
 

