from wsgi import application as app

@app.route('/')
def index():
	return '<h1>Sacamela!</h1>'
