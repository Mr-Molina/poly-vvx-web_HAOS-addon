from flask import Flask, render_template, jsonify
import requests
import json
import os

app = Flask(__name__)
try:
    app.config.from_file('/data/options.json', json.load)
except:
    print('Could not load options file')

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

    # Security Enhancement: Validate configuration type to prevent unhandled TypeErrors
    # if a user provides a null or non-list value in options.json
    sensor_ids = app.config.get('SENSOR_ENTITY_IDS')
    if not isinstance(sensor_ids, list):
        return jsonify([{"friendly_name": "Error", "state_and_unit": "Invalid sensor configuration"}]), 500

    for entity_id in sensor_ids:
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
