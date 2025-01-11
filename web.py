# V3rtex - a web-based client for K3rnel
# Developed by Arslaan Pathan - xminecrafterfun@gmail.com
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    # Remove debug mode in production
    app.run("0.0.0.0", 443, debug=True, ssl_context=("ssl/server.crt", "ssl/server.key"))
