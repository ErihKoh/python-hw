from flask import Blueprint

contact_bp = Blueprint('contacts', __name__)

from assistant_app.contacts import routes