from flask import Blueprint
import Slaves.Services.sayHi as sayHi
import Slaves.Services.Verifications as Verifications
import Slaves.Services.Messages as Messages



blueprint = Blueprint('api', __name__)

blueprint.route('/home', methods=["GET"])(sayHi.Greeting.sayHello)

blueprint.route('/webhook', method=["GET"])(Verifications.TokensVerification.verifyUserToken)

blueprint.route('/webhook', method=["POST"])(Messages.Chatting.receiveMessage)