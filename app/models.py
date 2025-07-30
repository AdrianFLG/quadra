# app/models.py
# (VERSIÓN FINAL Y CORRECTA)

from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # CORRECCIÓN FINAL: Aumentamos la longitud a 256
    password_hash = db.Column(db.String(256), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    puestos = db.relationship('Puesto', backref='autor', lazy=True)
    calificaciones = db.relationship('Calificacion', backref='autor', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Puesto(db.Model):
    __tablename__ = 'puestos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    foto_url = db.Column(db.String(255), nullable=True)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    calificaciones = db.relationship('Calificacion', backref='puesto', lazy=True, cascade="all, delete-orphan")

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id = db.Column(db.Integer, primary_key=True)
    puntuacion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    puesto_id = db.Column(db.Integer, db.ForeignKey('puestos.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('usuario_id', 'puesto_id', name='_usuario_puesto_uc'),)
