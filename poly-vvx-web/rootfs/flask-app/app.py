from flask import Flask, render_template, jsonify
import requests
import json
import os

app = Flask(__name__)
try:
    app.config.from_file('/data/options.json', json.load)
except:
    print('Could not load options file')

url = os.getenv('SUPERVISOR_URL', "http://supervisor/core/api/states/")
token = os.getenv('SUPERVISOR_TOKEN')

headers = {
    "Authorization": "Bearer " + token,
    "content-type": "application/json",
}

# Create a session to reuse TCP connections across sequential API requests
session = requests.Session()
session.headers.update(headers)

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error internally (can be enhanced with proper logging)
    print(f"Unhandled Exception: {e}")
    # Fail securely: do not expose stack traces or internal details
    return jsonify([{"friendly_name": "Error", "state_and_unit": "Internal Server Error"}]), 500

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/api")
def api():
    newDict = []
    # Use .get() to avoid KeyError if 'SENSOR_ENTITY_IDS' is missing from config
    for entity_id in app.config.get('SENSOR_ENTITY_IDS', []):
        try:
            # Use session to get connection pooling benefits
            response = session.get(url + entity_id, timeout=10)
            response.raise_for_status() # Raise exception for bad status codes

            # load json response into dict using built-in requests json parser
            haapi = response.json()
            friendly_name = haapi.get("attributes", {}).get("friendly_name", entity_id)
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi.get("attributes", {}).get("unit_of_measurement", "")
            state = haapi.get("state", "Unknown")

            newDict.append({'friendly_name': friendly_name, 'state_and_unit': state + " " + unit_of_measurement})
        except Exception as e:
            # Catch errors per sensor so one failing sensor doesn't break the whole dashboard
            print(f"Error fetching sensor {entity_id}: {e}")
            newDict.append({'friendly_name': entity_id, 'state_and_unit': 'Error fetching data'})

    return jsonify(newDict)
