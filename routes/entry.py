from flask import redirect
from app import flaskapp, address

# might do some stuff here later idk lol
@flaskapp.route("/")
def enter():
	return redirect(f'{address}/create')
