from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return 'Hello World'

app.run(host = '0.0.0.0', port = 4000, debug = True)
