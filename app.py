from flask import Flask, request, render_template

app = Flask(__name__)

LEDC = "OFF"

@app.route("/index")
def index():
    return render_template("tet.html")

@app.route("/")
def home():
    templateData = {
        'led' : LEDC
    }

    return render_template("home.html", **templateData)

@app.route("/light/<onoff>")
def status(onoff):
    if onoff == "on":
        LEDC = "ON"
    if onoff == "off":
        LEDC = "OFF"

    templateData = {
        'led' : LEDC
    }

    return render_template("home.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0")