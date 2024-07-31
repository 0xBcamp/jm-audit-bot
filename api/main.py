import flask
import requests
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return flask.jsonify({
        'msg': 'Hello, World!'
    })

@app.route('/audit', methods=['GET'])
def getReport():
    address = flask.request.args.get('address')
    if not address:
        return flask.jsonify({
            'error': 'Address is required'
        })
    response = {
        'address': address,
    }
    r = requests.get(f"https://explorer.mode.network/api/v2/smart-contracts/{address}")

    return flask.jsonify(response)

app.run(host='0.0.0.0', port=8000, debug=True)
