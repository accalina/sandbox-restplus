from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__)
# blueprint = Blueprint('api', __name__, url_prefix='/swagger')

api = Api(blueprint, version='1.0', title='Member API',
    description='A simple Member API',
)

from blueprints.member import member_namespace
api.add_namespace(member_namespace)

from blueprints.division import division_namespace
api.add_namespace(division_namespace)