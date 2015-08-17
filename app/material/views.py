from flask import Blueprint, jsonify
from .models import Material
from app import db

material = Blueprint('material', __name__, template_folder='templates')

@material.route('/')
def hello():
    return 'Hello material!'

@material.route('/materials')
def list():
    materials = Material.query.all()
    res = {}
    for m in materials:
        res[m.id] = {
            'matnr': m.matnr
        }
    return jsonify(res)

@material.route('/add')
def add():
    material = Material(matnr='mn1', matdb='md1')
    db.session.add(material)
    db.session.commit()
    return "ok"

from .forms import MaterialForm
from flask import request, redirect, url_for, render_template
@material.route('/material-add', methods=['GET', 'POST'])
def add_material():
    form = MaterialForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        matnr = request.form.get('matnr')
        matdb = request.form.get('matdb')
        material = Material(matnr, matdb)
        db.session.add(material)
        db.session.commit()
        return redirect(url_for('material.list'))
    return render_template('material-add.html', form=form)
