from flask_wtf import Form
from wtforms import TextField

class MaterialForm(Form):
    matnr = TextField('物料代码')
    matdb = TextField('物料描述')
