from flask import Flask, request, render_template
import aws_module.light as light

app = Flask(__name__)

LIGHT = "OFF"
BLIND = "UP"

@app.route("/")
def home():
    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)

@app.route("/light/<lighton>")
def lightControl(lighton):
    if lighton == "on":
        LIGHT = "ON"
    if lighton == "off":
        LIGHT = "OFF"

    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)


@app.route("/blind/<blindon>")
def blindControl(blindon):
    if blindon == "down":
        BLIND = "DOWN"
    if blindon == "up":
        BLIND = "UP"

    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0")