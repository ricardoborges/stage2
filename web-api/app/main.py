from flask import Flask, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "{'version': 'build 1'}"

@app.route("/news")
def news():
    
    resp = [{'title': 'teste 1'},{'title': 'teste 2'},{'title': 'teste 3'}]

    return jsonify(resp)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)