from flask import redirect, session
from app import flaskapp, address

# might do some stuff here later idk lol
@flaskapp.route("/")
def enter():
	session.clear()
	return redirect(f'{address}/create')
