import flask
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.jsonify({
        'msg': 'Hello, World!'
    })

@app.route('/tokens/<address>', methods=['GET', 'POST'])
def getReport(address):
    response = {
        'address': address,
    }

    r = requests.get(f"https://explorer.mode.network/api/v2/smart-contracts/{address}")

    return flask.jsonify(response)

app.run(host='0.0.0.0', port=8000, debug=True)
