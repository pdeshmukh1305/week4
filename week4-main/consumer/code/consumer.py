import requests
from flask import Flask,render_template
from flask import request
import os
from urllib.request import urlopen

app = Flask(__name__,template_folder='templates',static_folder='staticFiles')


@app.route('/')
def get_reco():
    r =requests.get("http://api:5000/meal")
    return render_template('recommendation.html',result=r.text)
    
    

if __name__ == '__main__':
    port = os.environ.get('CONSUMER_PORT',80)
    app.run(host='0.0.0.0',port=80)

