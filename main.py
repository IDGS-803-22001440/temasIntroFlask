from flask import Flask, render_template,request
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms

app=Flask(__name__)
app.secret_key="Esta es la clave screta"
csrf = CSRFProtect()

@app.errorhandler(400)
def page_not_found(e):
    return render_template('casa.html'), 404

@app.before_request
def before_request():
    g.nombre = "Mario"
    print(' Before request 1')


@app.after_request
def after_request(response):
    print(' After request 3')
    return response

@app.route('/')
def index():
    grupo="IDGS803"
    lista="Juan","Pedro","Mario"
    print("Holoa {}".format(g.nombre))
    return render_template("index.html",grupo=grupo,lista=lista)


@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    mat=''
    nom=''
    edad=''
    correo=''
    ape=''
    alumno_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumno_clase.validate():
        mat=alumno_clase.matricula.data
        ape=alumno_clase.apellidos.data
        nom=alumno_clase.nombre.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.email.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clase,mat=mat,nom=nom,ape=ape,edad=edad,correo=correo)


@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET","POST"])
def suma():
    if request.method == "POST":
        if  reques.form.get("Sumar") == "Sumar":
            num1=request.form.get("n1")
            num2=request.form.get("n2")
            rs=num1+num2
            return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)
        elif reques.form.get("Restar") == "Restar":
            num1=request.form.get("n1")
            num2=request.form.get("n2")
            rs=num1-num2
            return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)
        elif reques.form.get("Multiplicar") == "Multiplicar":
            num1=request.form.get("n1")
            num2=request.form.get("n2")
            rs=num1*num2
            return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)
        elif reques.form.get("Dividir") == "Dividir":
            num1=request.form.get("n1")
            num2=request.form.get("n2")
            rs=num1/num2
            return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)

@app.route("/cine")
def cine():
    return render_template("cine.html")

@app.route("/calculo", methods=["GET","POST"])
def calcularE():
    if request.method == "POST":
        request.form.get("calcular")
        name=request.form.get("name")
        num1=int(request.form.get("nc"))
        num2=int(request.form.get("nb"))
        trg=request.form.get("target")
        rs=0
        if (num1*7)>num2 :
            if trg == "no":
                if num2>5:
                    rs=(num2*12)*.85
                elif num2>2 and num2 <= 5:
                    rs=(num2*12)*.90
            elif trg == "si":
                if num2>5:
                    rs=(num2*12)*.75
                elif num2>2 and num2 <= 5:
                    rs=(num2*12)*.80
                elif num2>0 and num2 <= 2:
                    rs=(num2*12)*.90
        else:
            mesage="No puedes comprar esa cantidad de voletos "
            return render_template("cine.html",mesage=mesage)
        mesage=f"Hola {name} compraste {num2} boletos y tu total a pagar es {rs}$"
        return render_template("cine.html",mesage=mesage)


@app.route('/hola')
def hola():
    return "Hola!!!"

@app.route("/user/<string:user>")
def user(user):
    return f"hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} ID: {id}!!!"

"""@app.route("/default")
@app.route("/default/<string:nom")
def func(nom='pedro'):
    return "El nombre de Nom es: "+nom"""

@app.route("/foem1")
def form1():
    return '''
            <form>
            <label>Nombre: </label>
            <input type="text" name="nombre" placeholder="Nombre">
            </br>
        </form>
    '''

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=5000)

