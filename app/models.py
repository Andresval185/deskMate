from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    rol = db.Column(db.String(20), default='colaborador')  # colaborador o admin
    area = db.Column(db.String(100))
    dias_presenciales = db.Column(db.Integer, default=3)
    activo = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class Espacio(db.Model):
    __tablename__ = 'espacios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # escritorio, sala, estacionamiento
    capacidad = db.Column(db.Integer, default=1)
    descripcion = db.Column(db.String(255))
    activo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Espacio {self.nombre}>'

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    espacio_id = db.Column(db.Integer, db.ForeignKey('espacios.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    estado = db.Column(db.String(20), default='activa')  # activa, cancelada
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref='reservas')
    espacio = db.relationship('Espacio', backref='reservas')

    def __repr__(self):
        return f'<Reserva {self.id}>'