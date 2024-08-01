from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

# Function to read data from the JSON file
def read_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)

@app.route('/data')
def get_data():
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
