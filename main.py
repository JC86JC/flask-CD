#push
from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    """Greetings."""
    return 'Hello. Thanks for viewing my first project.'

@app.route('/iris')
def pandas_iris():
    df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    return jsonify(df.to_dict())

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is demo page for my first project</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)