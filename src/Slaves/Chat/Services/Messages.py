from flask import request as req
import requests as reqs
import json
from .. import ConversationFlow as CF
from . import sayHi
import config


class Chatting:
    """
    The `receiveMessage` function processes incoming messages, extracts relevant information, and
    interacts with a chatbot before returning a success message or error.
    :return: The function `receiveMessage` is returning either "the message was sent" if the message
    was successfully processed, or a dictionary with a status code of 403 and an error message if an
    exception occurred during message processing.
    """

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

    """
    The function `sendWhatsappMessage` sends a WhatsApp message using the provided data and returns
    a success message or an error response.
    
    :param data: The `data` parameter in the `sendWhatsappMessage` function should contain the
    message content and recipient information needed to send a WhatsApp message. This could include
    details such as the recipient's phone number, the message text, and any other relevant
    information required for sending the message via the WhatsApp API
    :return: The function `sendWhatsappMessage` returns either a dictionary with the keys
    "statusCode" and "res" in case of an error, or `True` if the message was successfully sent.
    """

    def sendWhatsappMessage(data):
        try:
            whatsappCredentials = {
                "whatsappToken": config.whatsappToken,  # Get this from your settings.py file
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
