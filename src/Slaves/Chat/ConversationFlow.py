from Slaves.Chat.Services import sayHi, Formats, Messages
import time


class ConversationFlow:

    def chatbotManagement(text, number, messageId, name):
        sendingFormats = Formats.SendingFormats()
        text = str(text).lower()
        collection = []

        if ("hola" or "ayuda" or "reiniciar chatbot" or "si" or "sí") in text:

            body = "¡Hola! Un gusto saludarte. ¿Te habla el chatbot interactivo de la UJED, en qué podemos ayudarte el día de hoy?"
            footer = "Atte: control escolar"
            options = ["Inscripciones", "Pagos", "Documento de reglas"]

            
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
                "https://api32.ilovepdf.com/v1/download/2ynkAtvl1blkApzd9bp29x5w6fj0qwg6l8pb352sp8w6ffc0qphbcwb693yss33wn368rbsrx8f8sb1h3g5m1v192fd9chzykksczp8lht575Ag81zb6094g258bgqph11j8t3dh3dnn90sApvnbptzzgn92qgwl48hvmwkrmtwtntqAnw0q",
                "¡¡Hecho!!",
                "Devian_tutorial.pdf",
            )
            collection.append(Messages.Chatting.sendWhatsappMessage(document))

            time.sleep(3)

            body = "Aquí en este documento podrás encontrar nuestras reglas y pautas a considerar en nuestra institución"  # Insert the URL of your document here
            footer = "Atte: control escolar"
            options = ["Reiniciar chatbot"]

            replyButtonData = sendingFormats.interactiveButtonMessage(
                number, options, body, footer, "sed2"
            )

            collection.append(Messages.Chatting.sendWhatsappMessage(replyButtonData))
            return  collection

        else:
            time.sleep(3)

            body = "Lo siento mucho pero no pude enteneder el mensaje. ¿Quieres ayuda con alguno de los siguientes conseptos?"
            footer = "Atte: control escolar"
            options = ["Inscripciones", "Pagos", "Documento de reglas"]

            replyButtonData = sendingFormats.interactiveButtonMessage(
                number, options, body, footer, "sed1"
            )
            return Messages.Chatting.sendWhatsappMessage(replyButtonData)
