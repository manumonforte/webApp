from flask import Flask, render_template, request


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
        param1 = request.form['Param1']
        param2 = request.form['Param2']
        param3 = request.form['Param3']
        param4 = request.form['Param4']
        
        return render_template('respuesta_animal.html',param1=param1,
                               param2=param2,param3=param3,
                               param4=param4)
    



if __name__ == '__main__':
    app.run(debug=False)