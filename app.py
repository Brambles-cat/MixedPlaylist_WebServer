import secrets
import socket
from flask import Flask, render_template

# different value depending on whether my laptop is being used or an RPi
usingRPi = True
address = f"https://www.mixedplaylist.com"

def render_create(**context):
    return render_template("create.html", address=address, **context)

flaskapp = Flask(__name__)
flaskapp.secret_key = secrets.token_urlsafe()

flaskapp.config['SESSION_TYPE'] = 'filesystem'
flaskapp.config['SESSION_PERMANENT'] = True
