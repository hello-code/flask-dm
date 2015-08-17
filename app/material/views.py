from flask import Blueprint, jsonify
from .models import Material
from app import db

material = Blueprint('material', __name__)

@material.route('/')
def hello():
    return 'Hello material!'

@material.route('/materials')
def list():
    materials = Material.query.all()
    res = {}
    for m in materials:
        res[m.id] = {
            'name': m.name
        }
    return jsonify(res)

@material.route('/add')
def add():
    material = Material('test')
    db.session.add(material)
    db.session.commit()
    return "ok"
