from flask import Flask, jsonify
from flask_cors import CORS
from opengateway_sandbox_sdk import Simswap

app = Flask(__name__)
CORS(app)

PORT = 8000
APP_CLIENT_ID = "your-registered-app-client-id"
APP_CLIENT_SECRET = "your-registered-app-client-secret"

@app.route('/retrieve_date/<string:phone_number>')
def sdk_retrieve_date(phone_number = None):
    try:
        simswap_client = Simswap(APP_CLIENT_ID, APP_CLIENT_SECRET, phone_number)
    except Exception as e:
        print(e)
        return jsonify(message=str(e)), 401
    try:
        last_swap = simswap_client.retrieve_date()
        return jsonify(message=f'Last SIM card swap was happened {last_swap}')
    except Exception as e:
        print(e)
        return jsonify(message=str(e)), 500

@app.route('/check/<string:phone_number>/<int:max_age>')
def sdk_check(phone_number = None, max_age = 240):
    try:
        simswap_client = Simswap(APP_CLIENT_ID, APP_CLIENT_SECRET, phone_number)
    except Exception as e:
        print(e)
        return jsonify(message=str(e)), 401
    try:
        simswap_check = simswap_client.check(max_age=max_age)
        return jsonify(message=f'SIM card swapped in the last {max_age // 24} days: {simswap_check}')
    except Exception as e:
        print(e)
        return jsonify(message=str(e)), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
