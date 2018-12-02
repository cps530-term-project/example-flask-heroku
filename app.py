from flask import Flask, jsonify
app = Flask(__name__)

my_array = []

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Get or post the array."""
	if request.method == 'GET':
		return jsonify(my_array)
	elif request.method == 'POST':
		my_array = request.json
		print(my_array)
		return jsonify(my_array)

if __name__ == '__main__':
	app.run(debug=True)
