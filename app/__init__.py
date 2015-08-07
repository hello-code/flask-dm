from flask import Flask
from .material.views import material
from .bom.views import bom

app = Flask(__name__)
app.register_blueprint(bom)
app.register_blueprint(material)
