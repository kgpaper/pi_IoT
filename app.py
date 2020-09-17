from flask import Flask, request, render_template
import aws_module.awsSocket_client as awsSocket_client

app = Flask(__name__)

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
        LIGHT = awsSocket_client.toPi("LIGHT ON")
    if lighton == "off":
        LIGHT = awsSocket_client.toPi("LIGHT OFF")
    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)


@app.route("/blind/<blindon>")
def blindControl(blindon):
    if blindon == "down":
        BLIND = awsSocket_client.toPi("BLIND DOWN")
    if blindon == "up":
        BLIND = awsSocket_client.toPi("BLIND UP")
        
    templateData = {
        'light' : LIGHT,
        'blind' : BLIND
    }

    return render_template("home.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0")