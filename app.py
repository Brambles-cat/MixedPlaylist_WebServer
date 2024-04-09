from flask import Flask, render_template, request, make_response, Response
import secrets
import uuid
import os

# different value depending on whether my laptop is being used or an RPi
usingRPi = os.getenv('usingRPi')
address = "https://www.mixedplaylist.com" if usingRPi else "127.0.0.1:5000" # f"http://{socket.gethostbyname(socket.gethostname())}"


flaskapp = Flask(__name__)
flaskapp.secret_key = secrets.token_urlsafe()

flaskapp.config['SESSION_PERMANENT'] = False

def render_create(**context):
    return render_template("create.html", address=address, theme=request.cookies.get("theme", "light") , **context)

def ensure_cookies(resp: Response) -> bool:
    if request.cookies.get("uid") is None:
        resp.set_cookie("uid", str(uuid.uuid4()), max_age=None, path='/', secure=True, httponly=True)
        resp.set_cookie("theme", "light", max_age=None, path='/', secure=True, httponly=True)
        return True
    return False
