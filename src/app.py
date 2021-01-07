# Modules
from flask import Flask, request
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

    print(title)
    print(description)
    return 'Received'

# Run Server
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 4000, debug = True)

