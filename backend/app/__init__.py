from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
api = Api(doc='/docs') # serves the docs at "localhost:5000/docs"

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from .routes import courses_ns, auth_ns, notes_ns, assignments_ns, chat_ns, prog_assignments_ns, summary_ns
    
    # register namespaces
    api.add_namespace(courses_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(notes_ns)
    api.add_namespace(assignments_ns)
    api.add_namespace(chat_ns)
    api.add_namespace(prog_assignments_ns)
    api.add_namespace(summary_ns)

    return app