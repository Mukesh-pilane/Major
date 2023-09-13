from google.oauth2 import id_token
from google.auth.transport import requests
from flask import request,jsonify
# from config import CLIENTID
from functools import wraps

CLIENTID = "1044924794976-n418rqsvep3iiaiecfsqlkf1jf5895is.apps.googleusercontent.com"

def verify_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            data = id_token.verify_oauth2_token(token, requests.Request(), CLIENTID,clock_skew_in_seconds=10)
            userData = data
        except:
            return jsonify({"message": "Token is invalid"}), 401
        kwargs["userData"] = userData
        return func(*args, **kwargs)
    return wrapper

