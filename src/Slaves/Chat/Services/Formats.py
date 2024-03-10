from flask import request as req
import requests as reqs
import json
from . import sayHi
import config


class SendingFormats:
    """
    The function `interactiveButtonMessage` generates a JSON data structure for sending an
    interactive button message via WhatsApp.

    :param number: The `number` parameter in the `interactiveButtonMessage` function is the phone
    number of the recipient to whom the interactive button message will be sent
    :param options: The `options` parameter in the `interactiveButtonMessage` function is expected
    to be a list of strings representing the options that will be displayed as buttons in the
    interactive message. Each option will be displayed as a button that the user can click on to
    interact with the message
    :param body: The `body` parameter in the `interactiveButtonMessage` function is the main text or
    message that will be displayed in the interactive button message. It is the content that you
    want to show to the user before the buttons
    :param footer: The `footer` parameter in the `interactiveButtonMessage` function is a string
    that represents the text to be displayed at the bottom of the interactive message. It typically
    provides additional information or context related to the message content
    :param sedd: The `sedd` parameter seems to be used as a prefix for generating unique button IDs
    in the `interactiveButtonMessage` function. It is concatenated with "_btn_" and the index of the
    button to create a unique ID for each button. This helps in identifying and handling button
    responses uniquely
    :return: The function `interactiveButtonMessage` returns a JSON string containing information
    for creating an interactive button message for a WhatsApp recipient. The JSON structure includes
    messaging product, recipient type, recipient number, message type, message body, message footer,
    and interactive button actions.
    """

    def interactiveButtonMessage(self, fromNumber, options, body, footer, sedd):
        buttons = []
        for i, options in enumerate(options):
            buttons.append(
                {
                    "type": "reply",
                    "reply": {"id": sedd + "_btn_" + str(i + 1), "title": options},
                }
            )

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": fromNumber,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": body},
                "footer": {"text": footer},
                "action": {"buttons": buttons},
            },
        }
        return data

    """
    The function `interactiveListMessage` generates a JSON data structure for sending an interactive
    list message via WhatsApp.
    
    :param number: The `number` parameter is the phone number of the recipient to whom the
    interactive list message will be sent
    :param options: It looks like there is a mistake in the code snippet you provided. The variable
    `options` is being redefined in the for loop, which may cause unexpected behavior. To fix this
    issue, you can change the loop variable name to something different from the list variable name.
    Here's the corrected code
    :param body: The `interactiveListMessage` function you provided seems to be a Python function
    for generating a JSON message for a WhatsApp interactive list. The `body` parameter in this
    function is used to specify the main text content of the message body. It will be displayed as
    part of the interactive list message that will
    :param footer: The `footer` parameter in the `interactiveListMessage` function is a string that
    represents the text to be displayed at the bottom of the interactive list message. It typically
    contains additional information or a call to action for the recipient
    :param sedd: The parameter `sedd` in the `interactiveListMessage` function is used to determine
    the type of row in the interactive list. It is concatenated with "_row_" and the index of the
    row to create the specific type for each row in the interactive list
    :return: The function `interactiveListMessage` returns a JSON string containing data for
    creating an interactive list message. The data includes information such as recipient number,
    message body, footer, and options for the list.
    """

    def interactiveListMessage(self, number, options, body, footer, sedd):
        rows = []
        for i, options in enumerate(options):
            rows.append(
                {
                    "type": sedd + "_row_" + str(i + 1),
                    "title": option,
                    "description": "",
                }
            )

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "Universidad Juárez del Estado de Durango",
                },
                "body": {"text": body},
                "footer": {"text": footer},
                "action": {
                    "button": "Take a look at the options!",
                    "sections": [{"title": "Sections", "row": rows}],
                },
            },
        }
        return data

    """
    The function `documentMessage` creates a JSON message for sending a document to a specific
    recipient via messaging.
    
    :param number: The `number` parameter in the `documentMessage` function is the phone number of
    the recipient to whom you want to send the document message
    :param url: The `url` parameter in the `documentMessage` function is the URL of the
    document/file that you want to send in the message
    :param caption: The `caption` parameter in the `documentMessage` function is used to provide a
    description or title for the document being sent. It is a text that accompanies the document and
    provides additional context or information about the file
    :param filename: The `filename` parameter in the `documentMessage` function is used to specify
    the name of the file that will be sent in the message. It is a string value that represents the
    name of the file being shared
    :return: a JSON string containing information about a document message to be sent.
    """

    def documentMessage(self, number, file, caption, filename):
        data = {
            "messaging_product": "document",
            "recipient_type": "individual",
            "to": number,
            "type": "file",
            "file": {"":"", "caption": caption, "filename": filename},
        }
        return data

    """
    The function `textMessage` takes a phone number and a text message as input and returns a JSON
    object formatted for sending a WhatsApp text message to the specified number.
    
    :param number: The `number` parameter in the `textMessage` function is the phone number of the
    recipient to whom you want to send a text message via WhatsApp
    :param text: The `textMessage` function takes two parameters: `number` and `text`. The `number`
    parameter is the phone number of the recipient to whom you want to send the text message. The
    `text` parameter is the actual message content that you want to send in the text message
    :return: The `textMessage` function returns a JSON string containing information about a
    WhatsApp text message to be sent to a specific phone number with the provided text message
    content.
    """

    def textMessage(self, number, text):
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {"body": text},
        }
        return data


class ReceivingFormats:
    pass
