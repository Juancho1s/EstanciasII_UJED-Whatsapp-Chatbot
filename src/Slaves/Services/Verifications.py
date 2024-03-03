from flask import request as req
from .. import Config


class TokensVerification:
    def verifyUserToken(self):
        try:
            token = req.args.get("hub.verify_token")
            challenge = req.args.get("hub.challenge")

            if token == Config.whatsappToken and challenge != None:
                return {"statusCode": 200, "res": challenge}
            else:
                return {"statusCode": 403, "res": "Invalid token."}

        except Exception as e:
            return {"statusCode": 401, "res": str(e) + " Invalid or expired token."}