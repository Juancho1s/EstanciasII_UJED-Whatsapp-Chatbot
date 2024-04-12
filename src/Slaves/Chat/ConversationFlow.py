from Slaves.Chat.Services import Formats, Messages
import time


class ConversationFlow:

    def chatbotManagement(text, number, messageId, name):
        sendingFormats = Formats.SendingFormats()
        messagesStructure = Messages.MessagesStructure()


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
        
        #Detailed procedures options:
                
        elif "nocturna(general)" in text:
            document = messagesStructure.procedureDetailsStructure("Nocturna(General)", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "diurna(general)" in text:
            document = messagesStructure.procedureDetailsStructure("Diurna(General)", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "nocturna(semiesc)" in text:
            document = messagesStructure.procedureDetailsStructure("Nocturna(Semiesc)", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "diurna(música)" in text:
            document = messagesStructure.procedureDetailsStructure("Diurna(Música)", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "ciencias/tecnologías" in text:
            document = messagesStructure.procedureDetailsStructure("Ciencias/Tecnologías", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        elif "ciencias/cumanidades" in text:
            document = messagesStructure.procedureDetailsStructure("Ciencias/Humanidades", number, "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(document)
        
        #Sections lists
        elif "media superior" in text:
            listMessage = messagesStructure.procedureListStrucutre("Media superior", number, "Puedes consultar las secciones referentes a educacion media superior en la siguiente lista", "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(listMessage)
        
        elif "por nivel educativo" in text:
            listMessage = messagesStructure.sectionListStrucutre("Por nivel educativo", number, "Puedes consultar las secciones referentes a nivel ecucativo en la siguiente lista", "Atte: control escolar")

            return Messages.Chatting.sendWhatsappMessage(listMessage)
        
        elif "oferta educativa" in text:
            listMessage = messagesStructure.sectionListStrucutre("Oferta educativa", number, "Puedes consultar las secciones referentes a oferta educativa en la siguiente lista", "Atte: control escolar")
            
            return Messages.Chatting.sendWhatsappMessage(listMessage)

        else:
            time.sleep(3)

            body = "Lo siento mucho pero no pude enteneder el mensaje. ¿Quieres ayuda con alguno de los siguientes conceptos?"
            footer = "Atte: control escolar"
            options = ["oferta educativa", "documento de reglas"]

            replyButtonData = sendingFormats.interactiveButtonMessage(
                number, options, body, footer, "btn_sed1"
            )
            return Messages.Chatting.sendWhatsappMessage(replyButtonData)
