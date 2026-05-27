from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Espacio, Reserva
from datetime import date

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

# ── Escritorios ────────────────────────────────────────
@main.route('/escritorios', methods=['GET', 'POST'])
@login_required
def escritorios():
    hoy = date.today().isoformat()
    fecha_sel = request.args.get('fecha', hoy)
    espacios = Espacio.query.filter_by(tipo='escritorio', activo=True).all()

    reservas_dia = Reserva.query.filter_by(fecha=fecha_sel, estado='activa').all()
    reservados_ids = {r.espacio_id for r in reservas_dia}
    mi_reserva_ids = {r.espacio_id for r in reservas_dia if r.user_id == current_user.id}

    for e in espacios:
        e.reservado = e.id in reservados_ids
        e.mi_reserva = e.id in mi_reserva_ids

    espacios_por_zona = {
        'Zona 1': [e for e in espacios if e.descripcion == 'Zona 1'],
        'Zona 2': [e for e in espacios if e.descripcion == 'Zona 2'],
        'Zona 3': [e for e in espacios if e.descripcion == 'Zona 3'],
        'Zona 4': [e for e in espacios if e.descripcion == 'Zona 4'],
    }

    return render_template('escritorios.html',
                           espacios_por_zona=espacios_por_zona,
                           fecha_sel=fecha_sel,
                           hoy=hoy)

@main.route('/reservar-escritorio', methods=['POST'])
@login_required
def reservar_escritorio():
    espacio_id = request.form.get('espacio_id')
    fecha = request.form.get('fecha')
    conflicto = Reserva.query.filter_by(
        espacio_id=espacio_id,
        fecha=fecha,
        estado='activa'
    ).first()
    if conflicto:
        flash('Este escritorio ya fue reservado para esa fecha.', 'danger')
        return redirect(url_for('main.escritorios'))
    mi_reserva = Reserva.query.filter_by(
        user_id=current_user.id,
        fecha=fecha,
        estado='activa'
    ).join(Espacio).filter(Espacio.tipo == 'escritorio').first()
    if mi_reserva:
        flash('Ya tienes un escritorio reservado para ese día.', 'warning')
        return redirect(url_for('main.escritorios'))
    nueva = Reserva(
        user_id=current_user.id,
        espacio_id=espacio_id,
        fecha=fecha,
        estado='activa'
    )
    db.session.add(nueva)
    db.session.commit()
    flash('¡Escritorio reservado exitosamente!', 'success')
    return redirect(url_for('main.mis_reservas'))

# ── Salas ──────────────────────────────────────────────
@main.route('/salas')
@login_required
def salas():
    espacios = Espacio.query.filter_by(tipo='sala', activo=True).all()
    return render_template('salas.html', espacios=espacios)

# ── Estacionamiento ────────────────────────────────────
@main.route('/estacionamiento')
@login_required
def estacionamiento():
    espacios = Espacio.query.filter_by(tipo='estacionamiento', activo=True).all()
    return render_template('estacionamiento.html', espacios=espacios)

# ── Mis reservas ───────────────────────────────────────
@main.route('/mis-reservas')
@login_required
def mis_reservas():
    reservas = Reserva.query.filter_by(
        user_id=current_user.id
    ).order_by(Reserva.fecha.desc()).all()
    return render_template('mis_reservas.html', reservas=reservas)