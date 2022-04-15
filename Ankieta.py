from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)
@app.route("/<name>")
def home(name):
    return render_template("index.html")

def Dane_os(name):
    return render_template("Dane_os.html")


if __name__ == "__main__":
    app.run()


