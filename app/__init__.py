from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

# 加载配置文件
app.config.from_object('config')

# 数据库
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
bootstrap = Bootstrap(app)

# 待db初始化后再引用views,因为views会引用models，而models会引用app里的db（就是这里的db）。如果把from .bom.views import bom和from .material.views import material放在db = SQLAlchemy(app)的前面，就会出现“ImportError: cannot import name 'db'”的错误。
# 蓝图
from .bom.views import bom
from .material.views import material
app.register_blueprint(bom, url_prefix='/bom')
app.register_blueprint(material, url_prefix='/material')

# 创建数据库
db.create_all()
