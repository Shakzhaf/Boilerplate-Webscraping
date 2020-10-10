"""
Author      : Shrikant Pathak
Created At  : 11 July2019
Description : Hackathon problem to design the pattern
Dependancies: .
Assumptions : This is just a sample program and I am too bored to create multiple files ideally all the 
              status should come from config file
"""

from flask import Flask, request, jsonify
from pprint import pprint
import requests
import utils
app = Flask(__name__)
app.config["DEBUG"] = True

  
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({ "status": "404","data" : "Page Not Found!" })

#http://localhost:8888/api/v1/resources/getProduct?productName=apple
@app.route('/api/v1/resources/getProduct', methods=['GET'])
def api_id():
    """
        Check if an ID was provided as part of the URL.
        If ID is provided, assign it to a variable.
        If no ID is provided, display an error in the browser.
    """
    if 'productName' in request.args:
        productName = request.args['productName']
        if utils.specialCharCheck(productName):
            return jsonify({ "status": "200","data" : "Special Character is not allowed in the search!" })
    else:
        return jsonify({ "status": "200","data" : "Please specify product name" })

    itemList = []
    try :
        # below path needs to come from the configuration file
        path='E:/Project/Bar Raiser/11 July - Scrapping Hathagon/chromedriver.exe'
        url='https://www.amazon.in/s?k='+productName
        browser= utils.getDriverInfo(path)
        htmlSourceSoup=utils.getHtmlSource(url, browser)
        linkDiv = htmlSourceSoup.find_all('div', {'class' : 'sg-col-inner'})
        itemList=utils.getJsonFromHtml(linkDiv)

        if not itemList:
            result = {
                "status" : "200",
                "productList" : "Product not found!"
            }
        else:
            result = { 
                "status" : "200",
                "productList" : itemList
            }

        return jsonify(result)
    except Exception as ex:
        return jsonify({ "status": "500","data" : "Server error while processing the request", "error":ex })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
