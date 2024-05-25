from flask import Flask, render_template, request
app = Flask(__name__)

frutas = []

@app.route("/", methods = ["GET", "POST"])
def principal():
    #frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maça", "Pêra", "Melão", "Abacaxi"]
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas = frutas)

@app.route("/sobre")
def sobre():
    notas = {"fulano": 5.0, "Beltrano": 6.0, "Aluno": 7.0, "Sicrano": 8.5, "Rodrigo": 9.5}
    return render_template("sobre.html", notas = notas)