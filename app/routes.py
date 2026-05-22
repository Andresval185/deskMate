from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Espacio, Reserva

auth = Blueprint('auth', __name__)
main = Blueprint('main', __name__)

# ── Autenticación ──────────────────────────────────────
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.inicio'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.inicio'))
        flash('Email o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@auth.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('main.inicio'))
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        if User.query.filter_by(email=email).first():
            flash('Este email ya está registrado.', 'danger')
            return redirect(url_for('auth.registro'))
        user = User(nombre=nombre, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Cuenta creada exitosamente. Inicia sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('registro.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# ── Rutas principales ──────────────────────────────────
@main.route('/')
@main.route('/inicio')
@login_required
def inicio():
    return render_template('inicio.html')

@main.route('/escritorios')
@login_required
def escritorios():
    espacios = Espacio.query.filter_by(tipo='escritorio', activo=True).all()
    return render_template('escritorios.html', espacios=espacios)

@main.route('/salas')
@login_required
def salas():
    espacios = Espacio.query.filter_by(tipo='sala', activo=True).all()
    return render_template('salas.html', espacios=espacios)

@main.route('/estacionamiento')
@login_required
def estacionamiento():
    espacios = Espacio.query.filter_by(tipo='estacionamiento', activo=True).all()
    return render_template('estacionamiento.html', espacios=espacios)

@main.route('/mis-reservas')
@login_required
def mis_reservas():
    reservas = Reserva.query.filter_by(user_id=current_user.id).order_by(Reserva.fecha.desc()).all()
    return render_template('mis_reservas.html', reservas=reservas)