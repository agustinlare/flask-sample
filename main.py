from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	asd = random.randint(1,70)

	if request.method == 'GET':
		return 'Esta es una pruebaaa'
	
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080)