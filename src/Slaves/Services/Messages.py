from flask import request as req
import requests as reqs
import json
from . import sayHi
from .. import Config


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

            Chatting.chatbotManagement(text, number, messageId, name)

            return "the message was sent"

        except Exception as e:
            return {"statusCode": 403, "res": str(e) + ". Error on receiving message"}

    def obtainWhatsappMessage(message):
        if "type" not in message:
            text = (
                "The message was not recognized. Please send a valid WhatsApp message."
            )
        typeMessage = message["type"]
        if typeMessage == "text":
            text = message["text"]["body"]


    def sendWhatsappMessage(data):
        try:
            whatsappCredentials = {
                "whatsappToken": Config.whatsappToken,  # Get this from your settings.py file
                "whatsappURL": Config.whatsappURL,
            }

            headers = {
                "Authorization": f"Bearer {whatsappCredentials['whatsappToken']}",
                "Content-Type": "application/json",
            }

            response = reqs.post(
                whatsappCredentials["whatsappURL"], headers=headers, data=data
            )

            if response.status_code != 200:
                return {
                    "statusCode": response.status_code,
                    "res": "Error on sending message",
                }
            else:
                print("Successfully sent the message!")
                return True

        except Exception as e:
            return {"statusCode": 403, "res": str(e) + "  Error on sending message"}


    def textMessage(number, text):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {"body": text},
            }
        )
        return data


    def chatbotManagement(text, number, messageId, name):
        text = str(text).lower()
        collection = []

        data = Chatting.textMessage(number, sayHi.Greeting.sayHello())
        Chatting.sendWhatsappMessage(data)
