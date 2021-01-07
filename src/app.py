# Modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Instance of Flask
app = Flask(__name__)

# Config Data Base
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jcjohan:password@localhost/flask_api_rest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique = True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

db.create_all()

# Schema
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many = True)

# Routes
@app.route('/tasks', methods = ['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

@app.route('/tasks', methods = ['GET'])
def get_task():
    all_tasks = Task.query.all()
    results = tasks_schema.dump(all_tasks)

    # String to JSON
    return jsonify(results)

@app.route('/tasks/<id>', methods = ['GET'])
def filter_task(id):
    task = Task.query.get(id)

    return task_schema.jsonify(task)

# Run Server
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 4000, debug = True)

