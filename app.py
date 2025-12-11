from flask import Flask, render_template, request
import sqlite3, datetime


app = Flask(__name__)

flag = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global flag
    flag = 1
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    global flag
    if flag == 1:
        username = request.form.get("username")
        print(username)
        timestamp = datetime.datetime.now()
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        c.execute("Insert into user(name, timestamp) values(?,?)", (username, timestamp))
        conn.commit()
        conn.close()
        flag = 0
    return(render_template("main.html"))

@app.route("/paynow", methods=["GET", "POST"])
def paynow():
    return(render_template("paynow.html"))


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    return(render_template("deposit.html"))

@app.route("/userlog", methods=["GET", "POST"])
def userlog():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECt * from USER")
    r = ""
    for row in c:
        r = r+str(row)
    print(r)
    conn.close()
    return(render_template("userlog.html", r=r))

@app.route("/deleteuserlog", methods=["GET", "POST"])
def deleteuserlog():
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("DELETE from user")
    conn.commit()
    conn.close()
    return(render_template("deleteuserlog.html"))

if __name__ == "__main__":
    app.run()
