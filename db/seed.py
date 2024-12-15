import sqlite3
import bcrypt

con = sqlite3.connect("./db/dev.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS user;")
cur.execute("DROP TABLE IF EXISTS contact;")

cur.execute(
    """
        CREATE TABLE user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL, 
        password TEXT NOT NULL, 
        createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """
)

cur.execute(
    """
        CREATE TABLE contact(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        email TEXT, 
        phone TEXT, 
        createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );"""
)

cur.execute(
    "insert into user (email,password) values(?,?)",
    (
        "superadmin@gmail.com",
        bcrypt.hashpw(b"superadmin", bcrypt.gensalt()),
    ),
)

cur.execute(
    "insert into user (email,password) values(?,?)",
    (
        "admin@gmail.com",
        bcrypt.hashpw(b"justadmin", bcrypt.gensalt()),
    ),
)
cur.execute(
    "insert into user (email,password) values(?,?)",
    (
        "user@gmail.com",
        bcrypt.hashpw(b"funuser", bcrypt.gensalt()),
    ),
)

cur.execute(
    "insert into contact (name,email,phone) values(?,?,?)",
    (
        "Ray Gun",
        "raygun@gmail.com",
        "",
    ),
)

cur.execute(
    "insert into contact (name,email,phone) values(?,?,?)",
    (
        "Kataky",
        "Kataky@gmail.com",
        "",
    ),
)

cur.execute(
    "insert into contact (name,email,phone) values(?,?,?)",
    (
        "Amir Setya",
        "amirsetya@gmail.com",
        "",
    ),
)

con.commit()
cur.close()
con.close()
