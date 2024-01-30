from flask import Flask,render_template, render_template, request
from pyshorteners import Shortener

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',title="嫌難しいな",message="本当にね")

@app.route('/', methods=['POST'])
def post():
	name = request.form['name']
	
	shortened_link = Shortener().tinyurl.short(name)
	print(shortened_link)
	return render_template('index.html', \
		title = 'Form Sample(post)', \
		message = '短縮urlは、{}'.format(shortened_link))


@app.route('/about')
def about():
    return render_template('about.html')









