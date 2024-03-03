from flask import request as req
import Config


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

    def receiveMessage(self):
        try:
            body = req.get_json()
            entry = body['entry'][0]
            changes = entry['changes'][0]
            value = changes['value']
            message = value['messages'][0]
            number = message['from']
            messageId = message['id']
            contacts = value['contacts'][0]
            name = contacts['profile']['name']

        except Exception as e:
            return  {"statusCode": 403, "res": str(e) + "  Error on receiving message"}