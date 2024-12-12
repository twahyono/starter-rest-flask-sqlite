from flask import Flask

app = Flask(__name__)

import routes.contact as contact
import routes.auth as auth
from db.db import init_app

app.register_blueprint(contact.bp)
app.register_blueprint(auth.bp)

init_app(app)

@app.get("/")
def hello_world():
    return {"Hello":"World"}

