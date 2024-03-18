from flask import redirect
from app import flaskapp

# might do some stuff here later idk lol
@flaskapp.route("/")
def enter():
	return redirect('https://www.mixedplaylist.com/create')
