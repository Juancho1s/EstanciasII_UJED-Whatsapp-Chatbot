from flask import Blueprint
from Slaves.Services.sayHi import Greeting
from Slaves.Services.Verifications import TokensVerification



blueprint = Blueprint('api', __name__)

blueprint.route('/home', methods=["GET"])(Greeting.sayHello)

blueprint.route('/webhook', method=["GET"])(TokensVerification.verifyUserToken)

blueprint.route('/webhook', method=["POST"])