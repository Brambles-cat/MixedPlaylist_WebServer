from flask import Flask, redirect, url_for, request, send_from_directory
app = Flask(__name__)

@app.route('/playlist/<id>')
def playlist(id: str):
	pass

@app.route("/create")
def create():
	return send_from_directory('templates', 'create.html')

@app.route('/')
def enter():
	return send_from_directory('templates', 'index.html')

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/add_video', methods=['POST', 'GET'])
def add_video():
	if request.method == 'POST':
		return request.form['url']
	else:
		print("idkman")

@app.route('/login', methods=['POST', 'GET'])
def login():
	print("meodrt\n\n\nfy")
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))


if __name__ == '__main__':
	app.run(host='localhost', port=5000)
