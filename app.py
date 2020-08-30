from flask import Flask, request, render_template
import aws_module.light as light

app = Flask(__name__)

LEDC = "OFF"

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