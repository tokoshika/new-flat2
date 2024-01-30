from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',title="嫌難しいな",message="本当にね")

@app.route('/about')
def about():
    return render_template('about.html')

