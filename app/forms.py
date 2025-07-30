# app/forms.py
# (VERSIÓN COMPLETA Y CON SANGRÍA CORRECTA)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, NumberRange
from .models import Usuario

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = Usuario.query.filter_by(nombre_usuario=username.data).first()
        if user is not None:
            raise ValidationError('Este nombre de usuario ya está en uso.')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email ya está registrado.')

class PuestoForm(FlaskForm):
    nombre = StringField('Nombre del Puesto', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Añadir Puesto')

class CalificacionForm(FlaskForm):
    puntuacion = IntegerField('Puntuación (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5, message="La puntuación debe ser entre 1 y 5.")])
    comentario = TextAreaField('Comentario', validators=[DataRequired()])
    submit = SubmitField('Enviar Calificación')
