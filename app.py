from flask import Flask, app, render_template, request, redirect


app = Flask(__name__)
lista_registros = []

@app.route('/')
def inicio():
    return render_template('registro.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', registros=lista_registros)

@app.route('/registro')
def registro():

    return render_template('registro.html')

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']

    registro = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    }

    lista_registros.append(registro)

    return redirect('/lista')

if __name__ == '__main__':
    app.run(debug=True)






