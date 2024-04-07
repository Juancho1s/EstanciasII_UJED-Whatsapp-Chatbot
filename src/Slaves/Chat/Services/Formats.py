from flask import request as req
import requests as reqs
import json
from . import sayHi
import config


class SendingFormats:

    def interactiveButtonMessage(self, number, options, body, footer, sedd):
        """
        The function `interactiveButtonMessage` generates a message with interactive buttons for a
        WhatsApp recipient.
        
        :param number: The `number` parameter in the `interactiveButtonMessage` function represents the
        recipient's phone number to whom the interactive message will be sent
        :param options: The `options` parameter in the `interactiveButtonMessage` function is a list of
        options that will be displayed as buttons in the interactive message. Each option in the list
        will be converted into a button with a unique ID and title for the user to interact with
        :param body: The `body` parameter in the `interactiveButtonMessage` function is a text message
        that will be displayed as the main content of the interactive message. It is the primary message
        that you want to convey to the recipient
        :param footer: The `footer` parameter in the `interactiveButtonMessage` function is a string
        that represents the text to be displayed at the bottom of the interactive message. It typically
        provides additional information or context related to the message content
        :param sedd: The `sedd` parameter in the `interactiveButtonMessage` function seems to be used as
        a prefix for generating unique button IDs. It is concatenated with "_btn_" and the index of the
        button to create a unique ID for each button. This helps in identifying and handling button
        responses in the interactive
        :return: The function `interactiveButtonMessage` returns a data object containing information
        for creating an interactive button message. The data object includes details such as the
        messaging product (WhatsApp), recipient type, recipient number, message type (interactive),
        button type, message body, message footer, and the buttons with their respective titles and IDs.
        """
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
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": body},
                "footer": {"text": footer},
                "action": {"buttons": buttons},
            },
        }
        return data

    
    def interactiveListMessage(self, number, options, body, footer, sedd):
        """
        The function `interactiveListMessage` generates a message with a list of options for a WhatsApp
        recipient.
        
        :param number: The `number` parameter in the `interactiveListMessage` function represents the
        phone number of the recipient to whom the interactive list message will be sent
        :param options: The `options` parameter in the `interactiveListMessage` function is a list of
        options that will be displayed in the interactive list. Each option will be shown as a row in
        the interactive list with a title
        :param body: The `interactiveListMessage` function you provided seems to be creating a
        structured message for a messaging platform, possibly WhatsApp. The function takes in several
        parameters such as `number`, `options`, `body`, `footer`, and `sedd` to construct the message
        :param footer: The `footer` parameter in the `interactiveListMessage` function is a text that
        will be displayed at the bottom of the interactive list message. It can be used to provide
        additional information, instructions, or a call to action for the recipient of the message
        :param sedd: It looks like there might be a typo in the parameter name "sedd". It seems like you
        intended to use "seed" instead. The "seed" parameter is likely meant to be a seed value for
        generating unique identifiers for the interactive list rows. This can be useful for
        distinguishing between different interactive
        :return: The function `interactiveListMessage` returns a data structure containing information
        for creating an interactive list message. The data structure includes details such as the
        recipient's number, message options, body text, footer text, and a button action to review
        options.
        """
        rows = []
        for i, options in enumerate(options):
            rows.append(
                {
                    "type": sedd + "_row_" + str(i + 1),
                    "title": options,
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
                    "button": "Revisar opciones!",
                    "sections": [{"title": "Sections", "row": rows}],
                },
            },
        }
        return data

    def documentMessage(self, number, url, caption, filename, footer):
        """
        The function `documentMessage` generates a data structure for sending a WhatsApp message with a
        document link and interactive elements.
        
        :param number: The `number` parameter in the `documentMessage` function represents the phone
        number of the individual recipient to whom the message will be sent
        :param url: The `url` parameter in the `documentMessage` function is the URL of the document
        that will be included in the message. This URL will be used as the link for the "Revisar
        documento" action button in the interactive message that will be sent to the recipient
        :param caption: The `caption` parameter in the `documentMessage` function is used to provide the
        text or message that will be displayed as the body of the interactive message being sent. It
        typically contains information or context related to the document or content being shared with
        the recipient
        :param filename: The `filename` parameter in the `documentMessage` function is used as the text
        for the header of the interactive message
        :param footer: The `footer` parameter in the `documentMessage` function is used to provide a
        text that will be displayed at the bottom of the interactive message. It can be used to add
        additional information, disclaimers, or any other relevant text to the message
        :return: The `documentMessage` function returns a dictionary `data` containing information for
        sending a WhatsApp message with a document link. The dictionary includes details such as the
        recipient's number, the document URL, caption, filename, and footer text. The message is
        structured as an interactive message with a call-to-action button that links to the provided
        URL.
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "cta_url",
                "header": {"type": "text", "text": filename},
                "body": {"text": caption},
                "footer": {"text": footer},
                "action": {
                    "name": "cta_url",
                    "parameters": {
                        "display_text": "Revisar documento",
                        "url": url,
                    },
                },
            },
        }
        return data

    def textMessage(self, number, text):
        """
        The function `textMessage` takes a phone number and a text message as input and returns a
        formatted data dictionary for sending a WhatsApp text message.
        
        :param number: The `number` parameter in the `textMessage` function is the phone number of the
        recipient to whom you want to send the text message
        :param text: The `textMessage` function takes three parameters: `self`, `number`, and `text`.
        The `number` parameter represents the phone number of the recipient to whom you want to send the
        text message. The `text` parameter represents the actual text message that you want to send
        :return: The `textMessage` method is returning a dictionary `data` that contains information
        about a text message to be sent via WhatsApp. The dictionary includes details such as the
        messaging product (WhatsApp), recipient type (individual), recipient number (`number`
        parameter), message type (text), and the text message content (`text` parameter).
        """
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
