import json
from flask import Blueprint, request
from db.db import get_db
import sqlite3
import bcrypt

bp = Blueprint("auth", __name__)

@bp.post("/auth")
def auth():
    try:
        user = request.json
        con = get_db()
        cur = con.cursor()
        findUser = cur.execute(
            f"select id,email,password from user where email='{user['email']}'"
        ).fetchone()
        if findUser is None:
            return {"message":"user or password is not valid"}

        if not bcrypt.checkpw(user["password"].encode("utf-8"), findUser[2]):
            return {"message":"user or password is not valid"}
        
        columns = ["id","email"]
        data = dict(zip(columns, findUser)) 
        return json.dumps(data,default=str)

    except sqlite3.Error as error:
        print("Error occurred - ", error)

# Convert tuple with product details to dict
def product_row_to_dict(contact):
    return {"id": contact[0], "email": contact[1]}