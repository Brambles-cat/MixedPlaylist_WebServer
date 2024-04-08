from flask import redirect, session
from app import flaskapp, address

@flaskapp.route("/")
def enter():
	session.clear()
	return redirect(f'/create')
