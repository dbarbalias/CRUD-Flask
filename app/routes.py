from app import app, db
from flask import redirect, render_template, request, url_for
from app.modules import Task
from datetime import datetime
from app.queries import same_day, roll_over

@app.route('/')
@app.route('/home')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        task_today = db.session.execute(same_day)
        task_today = [i[0] for i in task_today]
        task_today = Task.query.filter(Task.id.in_(task_today)).all()

        task_unfinished = db.session.execute(roll_over)
        task_unfinished = [i[0] for i in task_unfinished]
        task_unfinished = Task.query.filter(Task.id.in_(task_unfinished)).all()
        print(task_unfinished)

        date = datetime.utcnow()
        return render_template('index.html', title='Master Template', task_today=task_today, task_unfinished=task_unfinished, date=date)
    else:
        pass

        redirect(url_for('index'))

@app.route('/about')
def about():
    return '<h1>ABOUT</h1>'

@app.route('/status/<int:id>')
def status(id):
    obj_to_change = Task.query.get(id)
    if obj_to_change.status:
        obj_to_change.status = False
    else:
        obj_to_change.status = True
    
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html', title='Add Content')
    else:
        try:
            content = Task(content=request.form['content'])
            db.session.add(content)
            db.session.commit()
            return redirect(url_for("index"))
        except:
            return 'an error occurred'

@app.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify(id):
    if request.method == 'GET':
        task_to_modify = Task.query.get(id)
        return render_template('modify.html', title='Modify Content', task=task_to_modify)
    else:
        try:
            task_to_modify = Task.query.get(id)
            task_to_modify.content = request.form['content']
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'an error occurred'