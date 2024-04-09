from app import flaskapp
from modules.routes import entry, create, playlist, switch_theme, validator
import modules.bag_o_nifty_stuff as bag

if __name__ == '__main__':
	print(bag.API_KEY)
	flaskapp.run(host='0.0.0.0', port=5000, debug=False)