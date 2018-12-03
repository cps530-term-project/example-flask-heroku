import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_json():
	with open('data.json', 'r') as f:
		return json.load(f)

def set_json(data):
	with open('data.json', 'w') as f:
		json.dump(data, f)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Get or post the array."""
	if request.method == 'GET':
		return jsonify(get_json())

	elif request.method == 'POST':
		data = request.json
		print(data)
		set_json(data)
		print(get_json())
		return jsonify(data)

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)
