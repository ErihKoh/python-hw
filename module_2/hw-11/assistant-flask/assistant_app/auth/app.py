from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from assistant_app.auth import routes