from flask import request as req
import requests as reqs
import json
from .. import ConversationFlow as CF
from . import sayHi
import config


class Chatting:

    def receiveMessage():
        try:
            body = req.get_json()
            value = body["entry"][0]["changes"][0]["value"]
            message = value["messages"][0]
            name = value["contacts"][0]["profile"]["name"]
            number = message["from"]
            messageId = message["id"]

            text = Chatting.obtainWhatsappMessage(message)

            return CF.ConversationFlow.chatbotManagement(text, number, messageId, name)

        except Exception as e:
            print(e)
            return {"statusCode": 403, "res": str(e) + ". Error on receiving message"}
        

    def obtainWhatsappMessage(message):
        if "type" not in message:
            text = (
                "The message was not recognized. Please send a valid WhatsApp message."
            )
            return text

        typeMessage = message["type"]
        if typeMessage == "text":
            text = message["text"]["body"]

        elif typeMessage == "button":
            text = message["button"]["text"]

        elif (
            typeMessage == "interactve"
            and message["interactive"]["type"] == "list_reply"
        ):
            text = message["interactive"]["list_reply"]["title"]

        elif (
            typeMessage == "interactve"
            and message["interactive"]["type"] == "button_reply"
        ):
            text = message["interactive"]["button_reply"]["title"]

        else:
            text = f'This type of message ("{typeMessage}") is not supported yet.'

        return text
    

    def sendWhatsappMessage(data):
        try:
            whatsappCredentials = {
                "whatsappToken": config.whatsappToken,
                "whatsappURL": config.whatsappURL,
            }

            headers = {
                "Authorization": f'Bearer {whatsappCredentials["whatsappToken"]}',
                "Content-Type": "application/json",
            }

            res = reqs.post(
                url=whatsappCredentials["whatsappURL"], headers=headers, json=data
            )
            statusCode = res.status_code

            if (
                statusCode != 204
            ):  # HTTP Status Code 204 means No Content (which is successful).
                return {"statusCode": statusCode, "res": res.json()}
            else:  # If no errors occurred, we can assume that the message has been sent.
                return True

        except Exception as e:
            return {"statusCode": 403, "res": str(e) + "  Error on sending message"}
