from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return 'Hello, Galicia!'
	
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080)