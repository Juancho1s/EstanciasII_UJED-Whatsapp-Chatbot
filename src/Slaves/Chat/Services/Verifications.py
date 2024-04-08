from flask import request as req
import config


class TokensVerification:
    def verifyUserToken():
        try:
            token = req.args.get('hub.verify_token')
            challenge = req.args.get('hub.challenge')

            if token == config.whatsappToken and challenge != None:
                return {"statusCode": 200, "res": challenge}
            else:
                return {"statusCode": 403, "res": "Invalid token."}

        except Exception as e:
            return {"statusCode": 401, "res": str(e) + " Invalid or unexpired token."}
