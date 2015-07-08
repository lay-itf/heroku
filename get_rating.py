import os
import urllib2
import json
import cgi 
import requests

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def get_rating():
    users=request.args.getlist("user")
    output="Get CodeForces's Rating from API<br>"
    for name in users:    
        res = requests.get("http://codeforces.com/api/user.info",params={'handles':name})
        data = res.json()
        print data["status"]
        if(data["status"] != "OK"):
            output += cgi.escape(data["comment"][9:])+"<br>"
            continue
        if(data["result"][0].has_key("rating")):
            output += cgi.escape(data["result"][0]["handle"])+": "+ str(data["result"][0]["rating"]) +"<br>"
        else:
            output += cgi.escape(data["result"][0]["handle"])+": unrated<br>"         
        print output
    return output
    
if __name__ == '__main__':
    app.run(debug=True)