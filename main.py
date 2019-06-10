from flask import Flask, render_template, request
from sklearn.externals import joblib
import pandas as pd

'''FUNCIONES DE AYUDA'''
def comprobarDatos(info):
   for i in info.keys():
       try:
           value = int(info.get(i,""))
       except:
            print("ATENCIÓN: Debe ingresar un número entero.")

'''Definimos la aplicación'''
app = Flask(__name__)

'''Estableces el orgiden de la pagina'''
@app.route('/')
def home():
    return render_template('index.html')

'''A conitnuacion se crean funciones para las funcionalidades de la pagina'''

'''PAGINA PREDECIR ANIMAL'''

'''Caragar la pagina predecir_animal'''
@app.route('/predecir_animal')
def predecir_animal():
    return render_template("predecir_animal.html")

'''Funcion que permite obtener la información del formulario de la gina predecir_animal'''
@app.route('/send', methods=['GET', 'POST'])
def form_animal():
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
        '''Cargamos modelo y predecimos'''
        modelo = joblib.load('pipeline_animales.pkl')
        try:
            comprobarDatos(info)
            animalPredicho = modelo.predict(pd.DataFrame(info,index=[0]))
            info_animales = pd.read_csv('dataset/class.csv',header=None)
        
            animalPredicho = info_animales.loc[animalPredicho[0],:]
        
            return render_template('RESPUESTA_ANIMAL.html',clase=animalPredicho[2],
                               numero = animalPredicho[1],ejemplos = animalPredicho[3])
        except ValueError:
            return render_template('errores.html')

if __name__ == '__main__':
    app.run(debug=False)