from flask import Flask, render_template, jsonify
import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor

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
    def fetch_sensor(entity_id):
        # Use session to get connection pooling benefits
        response = session.get(url + entity_id, timeout=10)
        try:
            # load json response into dict using built-in requests json parser
            haapi = response.json()
            friendly_name = haapi["attributes"]["friendly_name"]
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi["attributes"].get("unit_of_measurement", "")
            return {'friendly_name': friendly_name, 'state_and_unit': haapi["state"] + " " + unit_of_measurement}
        except Exception as e:
            # Raise exception to be caught outside
            raise Exception('Could not load json from HA API')

    try:
        # Use ThreadPoolExecutor to fetch sensor APIs concurrently instead of sequentially
        # This converts the O(n * latency) waiting time to O(max(latency))
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Using map preserves the order of the configuration array
            results = executor.map(fetch_sensor, app.config['SENSOR_ENTITY_IDS'])
            newDict = list(results)
    except Exception as e:
        raise Exception('Could not load json from HA API')

    return jsonify(newDict)
