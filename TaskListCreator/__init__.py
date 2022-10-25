from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/TaskDB'
app.config['SECRET_KEY']='aafdb3c968c1df4eeb962cf6'
db = SQLAlchemy(app)

from TaskListCreator import routes