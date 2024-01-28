from flask import Blueprint
from Slaves.Services.sayHi import Greeting

blueprint = Blueprint('api', __name__)

blueprint.route('/home', methods=[GET])(sayHi.Greeting.sayHello)