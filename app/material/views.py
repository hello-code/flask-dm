from flask import Blueprint

material = Blueprint('material', __name__)

@material.route('/material')
def hello():
    return 'Hello material!'
