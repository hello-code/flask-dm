from flask import Blueprint

bom = Blueprint('bom', __name__)

@bom.route('/bom')
def hello():
    return 'Hello bom!'
