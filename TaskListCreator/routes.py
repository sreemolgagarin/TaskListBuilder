from TaskListCreator import app
from flask import render_template,request,redirect,url_for,flash
from TaskListCreator import db
from TaskListCreator.models import Tasks

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home_page():
    all_data = Tasks.query.all()
    return render_template('home.html', tasks=all_data)

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method =='POST':
        name = request.form['name']
        task_to_add=Tasks(task_name=name,status="To do")
        db.session.add(task_to_add)
        db.session.commit()
        flash("Task added successfully!")
    return redirect(url_for('home_page'))

@app.route('/update', methods=['GET','POST'])
def update():

    if request.method == 'POST':
        edit_task=Tasks.query.get(request.form.get('id'))
        edit_task.task_name=request.form['name']
        edit_task.status = request.form['status']
        db.session.commit()
        flash("Task updated!")
        return redirect(url_for('home_page'))


@app.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
    delete_task = Tasks.query.get(id)
    db.session.delete(delete_task)
    db.session.commit()
    flash("Task Removed!")

    return redirect(url_for('home_page'))