from flask import Flask, render_template, jsonify
import requests
import json
import os
import urllib.parse

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
    try:
        newDict = []
        for entity_id in app.config.get('SENSOR_ENTITY_IDS', []):
            # Sanitize entity_id to prevent SSRF and Path Traversal
            safe_entity_id = urllib.parse.quote(str(entity_id), safe='')
            # Use session to get connection pooling benefits
            response = session.get(url + safe_entity_id, timeout=10)

            # load json response into dict using built-in requests json parser
            haapi = response.json()
            friendly_name = haapi["attributes"]["friendly_name"]
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi["attributes"].get("unit_of_measurement", "")
            newDict.append({'friendly_name': friendly_name, 'state_and_unit': haapi["state"] + " " + unit_of_measurement})
        return jsonify(newDict)
    except Exception as e:
        # Secure error handling: do not leak stack traces
        print(f"API Error: {e}")
        return jsonify([{"friendly_name": "Error", "state_and_unit": "Internal Server Error"}]), 500
