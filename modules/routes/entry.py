from flask import redirect, session
from app import flaskapp

@flaskapp.route("/")
def enter():
	session.clear()
	return redirect(f'/create')
