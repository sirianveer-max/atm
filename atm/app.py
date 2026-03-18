from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/balance")
def balance():
    return render_template("balance.html")

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

@app.route("/fastcash")
def fastcash():
    return render_template("fastcash.html")

@app.route("/statement")
def statement():
    return render_template("statement.html")

@app.route("/transfer")
def transfer():
    return render_template("transfer.html")

@app.route("/changepin")
def changepin():
    return render_template("changepin.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True)