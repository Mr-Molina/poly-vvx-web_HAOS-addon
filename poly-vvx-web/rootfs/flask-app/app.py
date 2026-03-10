from flask import Flask, render_template, jsonify
import requests
import json
import os

app = Flask(__name__)
try:
    with open('/data/options.json', 'r') as f:
        options = json.load(f)
        # Security Enhancement: Only load expected configuration keys to prevent
        # overwriting sensitive Flask config variables (like DEBUG or SECRET_KEY)
        app.config['SENSOR_ENTITY_IDS'] = options.get('SENSOR_ENTITY_IDS', [])
except:
    print('Could not load options file')
    app.config['SENSOR_ENTITY_IDS'] = []

url = "http://supervisor/core/api/states/"
token = os.getenv('SUPERVISOR_TOKEN')

headers = {
    "Authorization": "Bearer " + token,
    "content-type": "application/json",
}

# Create a session to reuse TCP connections across sequential API requests
session = requests.Session()
session.headers.update(headers)

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/api")
def api():
    newDict = []
    for entity_id in app.config['SENSOR_ENTITY_IDS']:
        # Use session to get connection pooling benefits
        response = session.get(url + entity_id, timeout=10)
        try:
            # load json response into dict using built-in requests json parser
            haapi = response.json()
            friendly_name = haapi["attributes"]["friendly_name"]
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi["attributes"].get("unit_of_measurement", "")
            newDict.append({'friendly_name': friendly_name, 'state_and_unit': haapi["state"] + " " + unit_of_measurement})
        except:
            raise Exception('Could not load json from HA API')
    return jsonify(newDict)
