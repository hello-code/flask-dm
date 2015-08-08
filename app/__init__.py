from flask import Flask
from .material.views import material
from .bom.views import bom
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 加载配置文件
app.config.from_object('config')

# 数据库
db = SQLAlchemy(app)

# 蓝图
app.register_blueprint(bom, url_prefix='/bom')
app.register_blueprint(material, url_prefix='/material')

# 创建数据库
db.create_all()
