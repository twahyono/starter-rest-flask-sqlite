from flask import Blueprint, request
from db.db import get_db
import sqlite3
import json

bp = Blueprint("contact", __name__)

@bp.get("/contact")
def get_contact():
    try:
        limit = request.args.get("limit")
        offset = request.args.get("offset")
        if limit is None:
            limit=10
        if offset is None:
            offset=0
        con = get_db()
        cur = con.cursor()
        contact = cur.execute(
            "select id,name,email,createdAt from contact limit ? offset ?", (limit, offset)
        ).fetchall()
        columns = [col[0] for col in cur.description]
        data = [dict(zip(columns, row)) for row in contact]
        to_json = json.dumps(data, indent=2, default=str)
        return to_json
    except sqlite3.Error as error:
        print("Error occurred - ", error)
        return {"code":500, "message":str(error)}, 500
    except Exception as error:
        print("Error occurred - ", error)
        return {"code":500, "message":str(error)}, 500

@bp.get("/contact/<int:id>")
def get_contact_by_id(id):
    con = get_db()
    cur = con.cursor()

    contact = cur.execute("select * from contact where id=?", (id,)).fetchone()
    columns = ["id", "name", "email", "phone"]
    data = dict(zip(columns, contact))
    return json.dumps(data, default=str)


@bp.post("/contact")
def create_contact():
    newContact = request.get_json()
    con = get_db()
    cur = con.cursor()

    contact = cur.execute(
        "insert into contact (name,email,phone) values(?,?,?)",
        (
            newContact["name"],
            newContact["email"],
            newContact["phone"],
        ),
    )
    con.commit()
    columns = ["id", "name", "email", "phone"]
    data = dict(zip(columns, contact))
    return json.dumps(data, default=str)


@bp.put("/contact/<int:id>")
def update_contact_by_id(id):
    updateContact = request.get_json()
    con = get_db()

    cur = con.execute(
        "update contact set name=?, email=?, phone=? where id=?",
        (updateContact["name"], updateContact["email"], updateContact["phone"], id),
    )
    con.commit()
    updateContact["id"]=id
    return json.dumps(updateContact, default=str)


@bp.delete("/contact/<int:id>")
def delete_contact_by_id(id):
    con = get_db()
    con.execute("delete from contact where id=?", (id,))
    con.commit()
    return {"message": f"contact {id} is deleted."}
