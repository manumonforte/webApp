# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:26:33 2019

@author: Manuel Monforte
"""

from flask import render_template, request
from sklearn.externals import joblib
import pandas as pd

class prediceTitanic:
    
    '''Funcion que inicialzia el modelo'''
    def __init__(self):
        self.modelo = joblib.load('pipeline_titanic.pkl')
        print (self.modelo)
        
    '''Funcion que clasifica en funcion del input'''
    def predice(self, info):
        try:
            sobrevive = self.modelo.predict(pd.DataFrame(info,index=[0]))[0]
            if sobrevive == 0 :
                sobrevive = 'Lo siento, hubieras sido uno de los fallecidos en el titanic'
            else :
                sobrevive = 'Enhorabuena, hubieras sobrevivido a la tragedia del titanic'
            return render_template('respuesta_titanic.html',respuesta = sobrevive)
                           
        except :
            return render_template('errores.html')
        
    def extraerCampos(self):
        if request.method=='POST':
            info = {
            'clase billete' : request.form['billete'],
            'edad' : request.form['edad'],
            'n_hermanos_esposos' : request.form['n_hermanos_esposos'],
            'n_hijos_padres' : request.form['n_hijos_padres'],
            'precio_billete' : request.form['precio_billete'],
            'genero_hombre' : request.form['hombre'],
            'genero_mujer' : request.form['mujer'],
            'puerto_salida_C' : request.form['C'],
            'puerto_salida_Q' : request.form['Q'],
            'puerto_salida_S' : request.form['S'],
        }
        return info