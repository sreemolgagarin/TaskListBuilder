from TaskListCreator import db

class Tasks(db.Model):
    id=db.Column(db.Integer(),db.Identity(start=1),primary_key=True)
    task_name=db.Column(db.String(length=50),unique=True,nullable=False)
    status = db.Column(db.String(length=20),nullable = False)
