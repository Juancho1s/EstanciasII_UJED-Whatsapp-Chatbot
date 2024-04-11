from Slaves.Chat.Services import Formats, Messages
from Slaves.Models import ProceduresModel, SectionsModel
import time


class ConversationFlow:

    def chatbotManagement(text, number, messageId, name):
        sendingFormats = Formats.SendingFormats()
        proceduresModel = ProceduresModel.ProceduresModel()
        sectionsModel = SectionsModel.SectionsModel()


        text = str(text).lower()
        print(f"'{text}'")
        collection = []

        if ("hola" or "ayuda" or "reiniciar chatbot") in text:

            body = "¡Hola! Un gusto saludarte. ¿Te habla el chatbot interactivo de la UJED, en qué podemos ayudarte el día de hoy?"
            footer = "Atte: control escolar"
            options = ["Inscripciones", "Pagos", "Reglamentos"]

            
            replyButtonData = sendingFormats.interactiveButtonMessage(number, options, body, footer, "sed1")

            return Messages.Chatting.sendWhatsappMessage(replyButtonData)

        elif "documento de reglas" in text:

            textMessage = sendingFormats.textMessage(
                number,
                "¡Excelente! Le pedimos que espere unos momenotos en lo que conseguimos los documentos para su consulta.",
            )
            collection.append(Messages.Chatting.sendWhatsappMessage(textMessage))

            time.sleep(3)

            document = sendingFormats.documentMessage(
                number,
                "https://www.ujed.mx/doc/publicaciones/informes-de-actividades/5to-informe-2022-2023.pdf",
                "this is a test",
                "5to-informe-2022-2023.pdf",
                "Atte: control escolar",
            )
            collection.append(Messages.Chatting.sendWhatsappMessage(document))
            return  collection
        
        elif "nocturna(general)" in text:
            data = proceduresModel.getDataByName(["Nocturna(General)"])
            print(data)
            
            document = sendingFormats.documentMessage(
                number,
                data["url"][0],
                data["content"][0],
                data["name"][0],
                "Atte: control escolar"
            )
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "diurna(general)" in text:
            data = proceduresModel.getDataByName(["Diurna(General)"])
            print(data)
            
            document = sendingFormats.documentMessage(
                number,
                data["url"][0],
                data["content"][0],
                data["name"][0],
                "Atte: control escolar"
            )
            
            return Messages.Chatting.sendWhatsappMessage(document)

        
        elif "media superior" in text:
            proceduresData = proceduresModel.getDataByName(["Media superior"])
            print(proceduresData)
            
            listMessage = sendingFormats.interactiveListMessage(number, proceduresData, "Puedes consultar las secciones referentes en la siguiente lista", "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(listMessage)

        
        elif "por nivel educativo" in text:
            sectionsData = sectionsModel.getAllSectionsConnected(["por nivel educativo"])
            print(sectionsData)
            
            listMessage = sendingFormats.interactiveListMessage(number, sectionsData, "Puedes consultar las secciones referentes en la siguiente lista", "Atte: control escolar")

            return Messages.Chatting.sendWhatsappMessage(listMessage)
        
        elif "oferta educativa" in text:
            sectionsData = sectionsModel.getAllSectionsConnected(["Oferta educativa"])
            print(sectionsData)
            
            listMessage = sendingFormats.interactiveListMessage(number, sectionsData, "Puedes consultar las secciones referentes en la siguiente lista", "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(listMessage)

        else:
            time.sleep(3)

            body = "Lo siento mucho pero no pude enteneder el mensaje. ¿Quieres ayuda con alguno de los siguientes conceptos?"
            footer = "Atte: control escolar"
            options = ["Inscripciones", "Pagos", "Documento de reglas"]

            replyButtonData = sendingFormats.interactiveButtonMessage(
                number, options, body, footer, "sed1"
            )
            return Messages.Chatting.sendWhatsappMessage(replyButtonData)
