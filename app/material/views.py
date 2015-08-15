from flask import Blueprint, jsonify
from .models import Material

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

from sqlite3 import connect
import config

@material.route('/add')
def add():
    # conn = connect(app.config["SQLALCHEMY_DATABASE_URI "])  # wrong!
    # 数据库文件路径:sqlite://///home/z/projects/flask/flask-dm/mydb.db
    db_path = config.SQLALCHEMY_DATABASE_URI
    # conn = connect(db_path[11:])  # /home/z/projects/flask/flask-dm/mydb.db
    conn = connect(db_path)
    curs = conn.cursor()
    curs.execute('insert into material values(?,?)', (2, 'm2'))
    conn.commit()
    return str(curs.rowcount)
