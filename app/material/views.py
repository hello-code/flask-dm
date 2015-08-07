from flask import Blueprint

material = Blueprint('material', __name__)

@material.route('/')
def hello():
    return 'Hello material!'
