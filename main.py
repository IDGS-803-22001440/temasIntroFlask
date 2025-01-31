from flask import Flask, render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    grupo="IDGS803"
    lista="Juan","Pedro","Mario"
    return render_template("index.html",grupo=grupo,lista=lista)


@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET","POST"])
def suma():
    if request.method == "POST":
        val = reques.form.get("Sumar")
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        rs=num1+num2
        return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)

@app.route("/resultado", methods=["GET","POST"])
def resta():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        rs=num1-num2
        return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)


@app.route("/resultado", methods=["GET","POST"])
def multiplicacion():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        rs=num1*num2
        return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)

@app.route("/resultado", methods=["GET","POST"])
def division():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        rs=num1/num2
        return render_template("OperasBas.html",n1=num1,n2=num2,rs=rs)



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

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}!!!".format(n1+n2)

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
    app.run(debug=True, port=5000)

