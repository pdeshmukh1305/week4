from random import random
from flask import Flask
import os
import random
import json 

app = Flask(__name__)

meal_plan = {'Today, you can put your foot in your mouth!':'$0.00',
        'Just eat your words today!':'$0.00',
        'All you can eat breakfast buffet.':'$25.99',
        'Have some beers! Cheers!':'$17.99',
        'Dont eat anything today.':'$0.00',
        'Just smoke cigarettes for lunch.':'$12.00',
        'You only get black coffee today.':'$4.99',
        'Today, have some fresh air.':'$0.00',
        'Too many cooks spoilt your broth today. No food for you.':'$0.00',
        'Smoke a joint for brunch?':'$10.99',
        'All you get today is....... an insult.':'$0.00',
        'The milk is spilt. Drink your tears.':'$0.00',
        'You only get a slap today.':'$0.00',
        'Just drink a bottle of wine.':'$30.00',
        'Only eat an apple today.':'$2.50'}

os.environ["API_ENDPOINT"]='meal'

api_endpoint = os.environ.get("API_ENDPOINT")
@app.route('/'+api_endpoint)
def get_reco():
    return json.dumps(random.choice(list(meal_plan.items())))

if __name__ == '__main__':
    port = os.environ.get('API_PORT',5000)
    app.run(host='0.0.0.0',port=port)
 