from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!ssss55552222'

@app.route('/about')
def about():
    return 'About'

app.run(port=5000,debug=True)