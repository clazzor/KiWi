import flask

app = flask.Flask("Kiwi")
app.config["DEBUG"] = True
app.config["TESTING"] = True

@app.route('/')
def hello():
    return '<h1>Hello, World!!!</h1>'

app.run(host='0.0.0.0', port=3310, use_reloader=False)
