# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:25:45 2019

@author: Manuel Monforte
"""

from flask import render_template, request
from sklearn.externals import joblib
import pandas as pd


'''CLASE QUE CONTIENE LA LOGICA PARA CLASIFICAR ANIMALES POR CLASE'''
class prediceAnimales:
    
    '''Funcion que inicialzia el modelo'''
    def __init__(self):
        self.modelo = joblib.load('pipeline_animales.pkl')
        print(self.modelo)
        
                
    '''Funcion que clasifica en funcion del input'''
    def predice(self, info):
        try:
            animalPredicho = self.modelo.predict(pd.DataFrame(info,index=[0]))
            info_animales = pd.read_csv('dataset/class.csv',header=None)
            animalPredicho = info_animales.loc[animalPredicho[0],:]
            return render_template('respuesta_animal.html',
                           clase=animalPredicho[2],
                           numero = animalPredicho[1],
                           ejemplos = animalPredicho[3])
        except :
            return render_template('errores.html')
        
    def extraerCampos(self):
        if request.method=='POST':
            info = {
            'pelo' : request.form['pelo'],
            'plumas' : request.form['plumas'],
            'huevos' : request.form['huevos'],
            'leche' : request.form['leche'],
            'vuela' : request.form['vuela'],
            'acuatico' : request.form['acuatico'],
            'depredador' : request.form['depredador'],
            'dientes' : request.form['dientes'],
            'columnaVertebral' : request.form['columnaVertebral'],
            'pulmones' : request.form['pulmones'],
            'venenoso' : request.form['venenoso'],
            'aletas' : request.form['aletas'],
            'patas' : request.form['patas'],
            'cola' : request.form['cola'],
            'domestico' : request.form['domestico']
        }
        return info
        
                            
     