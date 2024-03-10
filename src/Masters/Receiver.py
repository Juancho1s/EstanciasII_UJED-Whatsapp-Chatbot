from flask import Blueprint
from Slaves.Chat.Services import sayHi, Verifications, Messages



blueprint = Blueprint('api', __name__)

blueprint.route('/home', methods=["GET"])(sayHi.Greeting.sayHello)

blueprint.route('/webhook', methods=["GET"])(Verifications.TokensVerification.verifyUserToken)

blueprint.route('/webhook', methods=["POST"])(Messages.Chatting.receiveMessage)