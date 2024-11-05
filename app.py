from flask import Flask, render_template
from app_2 import  estructura_datos

# crear unainstancia 

app = Flask(__name__)

#Describimos una url

#url principal
@app.route("/")
def principal():
    return render_template("primera_pagina.html")



@app.route("/primera")
def primera_elegante():
    return"""
                <html lang="es">
                    <head>
                        <meta charset="UTF-8">
                        <style> 
                            body {background-color: lightblue};
                        </style> 

                    </head>
                    <body>
                        <h1> Saludos!!! </h1>
                        <p> holis <p>

                    </body>
                </html>
                        """

@app.route("/segunda")
def segunda():
    return render_template("segunda_pagina.html")

@app.route("/tercera/variable")
def tercera_hola_nombre():
    return render_template("variable.html",nombre="José", curso="Flask") #se agregan las variables del html

#Se agregaran las variables de otra forma
@app.route("/tercera/variable/2")
def tercera_hola_nombre_2():
    nombre="José Bustamante" 
    curso="Flask con python, html5 y css"
    return render_template("variable.html",nombre=nombre,curso=curso) 


#Se agregaran las variables de otra forma
@app.route("/tercera/variable/3")
def tercera_hola_nombre_3():
    kwargs = {
    "nombre" : "José Bustamante 3",
    "curso"   : "Flask con python, html5 y css"
    }
    return render_template("variable.html", **kwargs) 


#Para ejecutarlo desde el mismo documento 

if __name__=="__main__":
    app.run()