from flask import Flask, request

app = Flask(__name__)

import routes.contact as contact
import routes.auth as auth
from db.db import init_app
import jwt
import os

app.register_blueprint(contact.bp)
app.register_blueprint(auth.bp)

init_app(app)

@app.get("/")
def hello_world():
    return "<h2>Hello, World!</h2>"

# middleware for jwt validation execute before blueprint route
@app.before_request
def auth_path():
    if request.path.startswith('/contact'):
        res = jwt_validation(request)
        return res
    
def jwt_validation(request):
    try:
        authorizationHeader = request.headers.get("Authorization")
        token = authorizationHeader.split()[1]
        decoded = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        print(decoded)
    except jwt.exceptions.InvalidTokenError as error:
        print("Error occurred - ", error)
        return {"code":401, "message": str(error)}, 401
    except jwt.exceptions.ExpiredSignatureError as error:
        print("Error occurred - ", error)
        return {"code":401, "message":str(error)}, 401
    except Exception as error:
        print("Error occurred - ", error)
        return {"code":500, "message":str(error)}, 500