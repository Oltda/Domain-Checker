from zeep import Client
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")

@app.route('/overit-domenu', methods=['POST'])
@cross_origin()
def overit_domenu():

    body = request.get_json()
    domain_name = body.get('domain_name')

    try:
        client = Client('http://regtons.com/wsdl')
        result = client.service.Login(USER, PASSWORD)
        ssid = result.data['ssid']
        checked_domain = client.service.Check_Domain(ssid, domain_name)
        availability = checked_domain['data']['avail']

        return jsonify({
            'akce': 'overeni domeny',
            'name': domain_name,
            'status': 'Ok',
            'availability': availability
        })
    except:
        return jsonify({
            'akce': 'overeni domeny',
            'status': 'invalid',
            'name': domain_name,
        })


