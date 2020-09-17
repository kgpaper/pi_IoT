from flask import Flask, request, render_template
import aws_module.awsSocket_client as awsSocket_client

app = Flask(__name__)

awsSocket_client.connectPi()

LIGHT = "LIGHT OFF"
BLIND = "BLIND UP"

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
        LIGHT = "LIGHT ON"
    if lighton == "off":
        LIGHT = "LIGHT OFF"

    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)


@app.route("/blind/<blindon>")
def blindControl(blindon):
    if blindon == "down":
        BLIND = "BLIND DOWN"
        awsSocket_client.toPi(BLIND)
    if blindon == "up":
        BLIND = "BLIND UP"
        awsSocket_client.toPi(BLIND)

    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0")