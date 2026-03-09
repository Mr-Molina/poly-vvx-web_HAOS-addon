from flask import Flask, render_template, jsonify
import requests
import json
import os
import time

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

# ⚡ Bolt: Cache API responses to prevent hammering the HA Supervisor API when multiple phones poll
API_CACHE = {"data": None, "last_updated": 0}
CACHE_TTL = 15

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/api")
def api():
    current_time = time.time()
    if API_CACHE["data"] is not None and (current_time - API_CACHE["last_updated"]) < CACHE_TTL:
        return jsonify(API_CACHE["data"])

    newDict = []
    for entity_id in app.config.get('SENSOR_ENTITY_IDS', []):
        # Use session to get connection pooling benefits
        response = session.get(url + entity_id, timeout=10)
        try:
            # load json response into dict using built-in requests json parser
            haapi = response.json()
            friendly_name = haapi["attributes"]["friendly_name"]
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi["attributes"].get("unit_of_measurement", "")
            newDict.append({'friendly_name': friendly_name, 'state_and_unit': str(haapi["state"]) + " " + unit_of_measurement})
        except:
            raise Exception('Could not load json from HA API')

    API_CACHE["data"] = newDict
    API_CACHE["last_updated"] = current_time
    return jsonify(newDict)
