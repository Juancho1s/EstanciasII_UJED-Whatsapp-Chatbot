from flask import request as req
import requests as reqs
from .. import ConversationFlow as CF
import config
from Slaves.Models import ProceduresModel, SectionsModel
from Slaves.Chat.Services import Formats


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



class MessagesStructure:
    def __init__(self):
        self.sectionsModel = SectionsModel.SectionsModel()
        self.proceduresModel = ProceduresModel.ProceduresModel()
        self.sendingFormats = Formats.SendingFormats()
    
    
    def sectionListStrucutre(self, nameFilter: str, phoneNumber: int, messageBody: str, messageFooter: str):
        sectionsData = self.sectionsModel.getAllSectionsConnected([nameFilter])
        if sectionsData == None:
            return None
        print(sectionsData)
        
        return self.sendingFormats.interactiveListMessage(phoneNumber, sectionsData, messageBody, messageFooter)
    
    
    def sectionDetailStructure(self, nameFilter, phoneNumber, messageBody, messageFooter):
        sectionData = self.sectionsModel.getSectionsByName([nameFilter])
        if sectionData == None:
            return None
        print(sectionData)
        
        return self.sendingFormats.interactiveListMessage(phoneNumber, sectionData, messageBody, messageFooter)

    
    
    def procedureListStrucutre(self, idFilter: int, phoneNumber: int, messageBody: str, messageFooter: str):
        proceduresData = self.proceduresModel.getConnectedProceduresBySection([idFilter])
        if proceduresData == None:
            return None
        print(proceduresData)
        
        return self.sendingFormats.interactiveListMessage(phoneNumber, proceduresData, messageBody, messageFooter)
    
    
    def procedureDetailsStructure(self, nameFilter: int, phoneNumber: int, messageFooter: str):
        procedureData = self.proceduresModel.getDataByName([nameFilter])
        if procedureData == None:
            return None
        print(procedureData)
        
        return self.sendingFormats.documentMessage(phoneNumber, procedureData["url"][0], procedureData["content"][0], procedureData["name"][0], messageFooter)