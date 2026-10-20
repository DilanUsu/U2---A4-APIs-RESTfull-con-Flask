from flask import Blueprint
from flask_restful import Api

# Blueprint con prefijo /api  ->  todas las rutas quedan como /api/...
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

# Importar routes al final para evitar importaciones circulares
from api import routes  # noqa: E402,F401
