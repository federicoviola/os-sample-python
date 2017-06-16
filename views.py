from fedeapp import app

@app.route('/')
def index():
	return '<h1>Sacamela!</h1>'
