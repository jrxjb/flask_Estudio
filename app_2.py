from flask import Flask, render_template

app2= Flask(__name__)


#clase para la pelicula 

class Pelicula:
    def __init__(self,nombre,año, protagonista):
        self.nombre       = nombre
        self.año          = año
        self.protagonista = protagonista

clase_pelicula = Pelicula(nombre="volver al futuro",año="1985",protagonista="Quien sabe el nombre")

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
    return render_template("Estructuras.html", movies=peliculas,destacada=lobo,favorita=clase_pelicula)

@app2.route("/condicionales")
def condiconales_pruebas():
    return render_template("condicionales.html")








if __name__=="__main__":
    app2.run()

    