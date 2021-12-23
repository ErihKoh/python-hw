from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from flask_mail import Mail

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

# from assistant_app.models import User, Note
from assistant_app.auth.routes import auth_bp
from assistant_app.contacts.routes import contact_bp

app.register_blueprint(auth_bp)
app.register_blueprint(contact_bp)