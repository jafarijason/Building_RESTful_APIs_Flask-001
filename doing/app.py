from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_eorld():
    return 'Hello World'

@app.route('/super_simple')
def super_simple():
    return jsonify(message = 'Hello from the planetary api . boosdfsdfya')

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0') 