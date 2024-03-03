import requests as reqs
import sayHi
import Config
import json


class Chatting:
    def obtainWhatsappMessage(self, message):
        if "type" not in message:
            text = (
                "The message was not recognized. Please send a valid WhatsApp message."
            )
        typeMessage = message["type"]
        if typeMessage == "text":
            text = message["text"]["body"]

    def sendWhatsappMessage(self, data):
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

    def textMessage(self, number, text):
        data = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number, 
                "type": "text",
                "text": {
                    "body": text
                },
            }
        )
        return data

    def chatbotManagement(text, number, messageId, name):
        text = str(text).lower()
        collection = []

        data = textMessage(number, sayHi.Greeting.sayHello())