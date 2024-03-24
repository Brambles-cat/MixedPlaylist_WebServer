from app import flaskapp
from routes import entry, create, playlist

if __name__ == '__main__':
	flaskapp.run(host='0.0.0.0', port=5000, debug=True)