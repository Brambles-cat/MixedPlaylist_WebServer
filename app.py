import secrets
import socket
from flask import Flask

ip = socket.gethostbyname(socket.gethostname())

flaskapp = Flask(__name__)
flaskapp.secret_key = secrets.token_urlsafe()

flaskapp.config['SESSION_TYPE'] = 'filesystem'
flaskapp.config['SESSION_PERMANENT'] = True
