from wtforms import form
from flask_wtf import Flaskform
from wtforms.validators import DataRequired, Email, EqualTo, Lenght, NumberRange, Regexp
from wtforms import StringField, PasswordField, EmailFIeld, SubmitField, IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    email=EmailFIeld("Correo")