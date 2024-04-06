from flask import make_response, request
from app import flaskapp, ensure_cookies

@flaskapp.route('/switch_theme', methods=['POST'])
def switch_theme():
    resp = make_response("{result: 'Success'}")
    cookie_made = ensure_cookies(resp)

    if cookie_made:
        resp.set_cookie("theme", "dark", max_age=None, path='/', secure=True, httponly=True)
    else:
        resp.set_cookie(
            "theme",
            "dark" if request.cookies.get("theme") == "light" else "light",
            max_age=None, path='/', secure=True, httponly=True)
    
    return resp