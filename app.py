from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temporada_2024_25.json')
def json_data():
    return send_from_directory(os.getcwd(), 'temporada_2024_25.json')

if __name__ == '__main__':
    app.run(debug=True)