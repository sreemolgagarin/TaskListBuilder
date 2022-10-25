from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField
class TaskForm(FlaskForm):
    task_name = StringField(label='Task')
    add = SubmitField(label='Add')

class EditForm(FlaskForm):
    task_name = StringField(label='Task')
    status = StringField(label='Status')
    update = SubmitField(label='Update')