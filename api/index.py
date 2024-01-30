from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!ssssPPP'

@app.route('/about')
def about():
    return 'About2'

app.run(port=5000,debug=True)