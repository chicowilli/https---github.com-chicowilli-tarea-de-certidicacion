from flask import Flask, app, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/inicio.html', methods=['POST'])
def submit():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    password = request.form['password']
    email = request.form['email']

    # Here you can process the form data, e.g., save it to a database or send an email

    return redirect('/')  # Redirect back to the index page after submission    

if __name__ == '__main__':
    app.run(debug=True)







