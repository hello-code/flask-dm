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
    # res = {}
    # for m in materials:
    #     res[m.id] = {
    #         'matnr': m.matnr
    #     }
    # return jsonify(res)
    return render_template('materials.html', materials=materials)

@material.route('/add')
def add():
    material = Material(matnr='mn1', matdb='md1')
    db.session.add(material)
    db.session.commit()
    return "ok"

from .forms import MaterialForm
from flask import request, redirect, url_for, render_template, flash
@material.route('/material-add', methods=['GET', 'POST'])
def add_material():
    form = MaterialForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        matnr = request.form.get('matnr')
        matdb = request.form.get('matdb')
        material = Material(matnr, matdb)
        db.session.add(material)
        db.session.commit()
        flash('物料 %s 添加成功！' % matnr, 'success')
        return redirect(url_for('material.list'))
    return render_template('material-add.html', form=form)

@material.route('/table')
def hstable():
    materials = Material.query.all()
    data = [['id','matnr','matdb']]
    for m in materials:
        data.append([m.id, m.matnr, m.matdb])
    return render_template('table.html',data=data)
