#push
from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    """Greetings."""
    return 'Hello. Thanks for viewing my first project. :)'

@app.route('/iris')
def pandas_iris():
    df = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')
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