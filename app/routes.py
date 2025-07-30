# app/routes.py
# (VERSIÓN COMPLETA Y CON INDENTACIÓN CORRECTA)

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, Usuario, Puesto
from .forms import LoginForm, RegistrationForm, PuestoForm, CalificacionForm
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    puestos = Puesto.query.all()
    return render_template('index.html', title='Inicio', puestos=puestos)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        email_ingresado = form.email.data
        usuario = Usuario.query.filter_by(email=email_ingresado).first()
        
        if usuario is None:
            flash(f'No se encontró ningún usuario con el email: {email_ingresado}', 'danger')
            return redirect(url_for('main.login'))
            
        if not usuario.check_password(form.password.data):
            flash(f'Contraseña incorrecta. Por favor, inténtalo de nuevo.', 'danger')
            return redirect(url_for('main.login'))
            
        login_user(usuario, remember=form.remember_me.data)
        flash('Has iniciado sesión correctamente.', 'success')
        next_page = request.args.get('next')
        return redirect(next_page or url_for('main.index'))
        
    return render_template('login.html', title='Iniciar Sesión', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Usuario(nombre_usuario=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('¡Felicidades, ahora eres un usuario registrado!', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', title='Registro', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado la sesión.', 'info')
    return redirect(url_for('main.index'))

@main.route('/add_puesto', methods=['GET', 'POST'])
@login_required
def add_puesto():
    form = PuestoForm()
    if form.validate_on_submit():
        puesto = Puesto(nombre=form.nombre.data,
                        descripcion=form.descripcion.data,
                        autor=current_user,
                        latitud=19.4326,
                        longitud=-99.1332)
        db.session.add(puesto)
        db.session.commit()
        flash('¡Tu puesto ha sido añadido con éxito!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_puesto.html', title='Añadir Puesto', form=form)
