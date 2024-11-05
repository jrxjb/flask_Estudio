from flask import Flask, render_template

app2= Flask(__name__)

@app2.route("/estructuras")
def estructura_datos():
    peliculas = [
        "El lobo de wall Street",
        "Harry Potter",
        "Volver al futuro"
    ]
    lobo={
        "nombre":"Lobo de wall street",
        "Año":2013
    }
    return render_template("Estructuras.html", movies=peliculas,destacada=lobo)

if __name__=="__main__":
    app2.run()