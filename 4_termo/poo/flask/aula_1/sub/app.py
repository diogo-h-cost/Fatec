from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def principal():
    frutas = ["Morango", "Perâ", "Uva", "Melão"]
    return render_template("index.html", fruta = frutas)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")