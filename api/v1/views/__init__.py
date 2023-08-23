from flask import Blueprint
from api.v1.views import app_views

app_views = Blueprint('api', __name__, url_prefix='/api/v1')


from api.v1.views.index import *