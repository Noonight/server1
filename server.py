from flask import Flask, json, jsonify
from flask import request
import translator
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def hello_user(username):
    return "Hello %s" % escape(username)

@app.route('/translate', methods=['GET'])
def routeTranslate():
    targetText = request.args.get("text", default=None, type=str)
    targetFrom = request.args.get("from", default=None, type=str)
    targetTo = request.args.get("to", default=None, type=str)

    if targetText is None or targetTo is None:
        data = {'error': 'Invalid request data'}
        response = app.response_class(  response=json.dumps(data),
                                        status=400,
                                        mimetype='application/json')
        return response
    elif targetFrom == targetTo:
        data = {'error': 'Same arguments from and to translate'}
        response = app.response_class(  response=json.dumps(data),
                                        status=400,
                                        mimetype='application/json')
        return response
    else:
        return translator.translate(targetText, targetFrom, targetTo)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 4567)
