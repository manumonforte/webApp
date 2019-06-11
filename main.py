# -*- coding: utf-8 -*-
"""
Created on Mon Jun 8 16:25:45 2019

@author: Manuel Monforte
"""

from flask import Flask, render_template
from modeloAnimales import prediceAnimales
from modeloTitanic import prediceTitanic

'''Definimos la aplicación'''
app = Flask(__name__)
    
'''Estableces el orgiden de la pagina'''
@app.route('/')
def home():
    return render_template('index.html')

'''Cargar la pagina predecir_animal'''
@app.route('/predecir_animal')
def predecir_animal():
    return render_template("predecir_animal.html")

'''Funcion que permite obtener la información del formulario de la gina predecir_animal'''
@app.route('/predecir_animal/send', methods=['GET', 'POST'])
def form_animal():
    
        modelo_animal = prediceAnimales()
        info = prediceAnimales().extraerCampos()
        return  modelo_animal.predice(info)
    
    
'''Cargar la pagina predecir_animal'''
@app.route('/predecir_titanic')
def predecir_titanic():
    return render_template("predecir_titanic.html")
    
'''Funcion que permite obtener la información del formulario para comporbar si sobrevivirias'''
@app.route('/predecir_titanic/send', methods=['GET', 'POST'])
def form_titanic():
    
        modelo_titanic = prediceTitanic()
        info = prediceTitanic().extraerCampos()
        return  modelo_titanic.predice(info)
    
if __name__ == '__main__':
    app.run(debug=False)