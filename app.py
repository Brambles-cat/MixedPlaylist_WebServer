import secrets
import socket
from flask import Flask, render_template
import os
import dotenv

dotenv.load_dotenv()
# different value depending on whether my laptop is being used or an RPi
usingRPi = os.getenv('usingRPi')
address = "https://www.mixedplaylist.com" if usingRPi else f"http://{socket.gethostbyname(socket.gethostname())}"

def render_create(**context):
    return render_template("create.html", address=address, **context)

flaskapp = Flask(__name__)
flaskapp.secret_key = secrets.token_urlsafe()

flaskapp.config['SESSION_PERMANENT'] = False