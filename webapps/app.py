from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("tet.html")

@app.route("/")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")