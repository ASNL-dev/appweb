from flask import Blueprint

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)

from . import routes  # Importer les routes ici pour enregistrer les routes dans les blueprints

