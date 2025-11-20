from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    username = request.form.get("username")
    print(username)
    return(render_template("main.html"))

@app.route("/paynow", methods=["GET", "POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__":
    app.run()
