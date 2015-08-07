from flask import Blueprint

bom = Blueprint('bom', __name__)

@bom.route('/')
def hello():
    return 'Hello bom!'
