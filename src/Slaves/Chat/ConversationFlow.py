from Slaves.Chat.Services import sayHi, Formats, Messages
import time


class ConversationFlow:

    def chatbotManagement(text, number, messageId, name):
        sendingFormats = Formats.SendingFormats()
        text = str(text).lower()
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

        else:
            time.sleep(5)

            body = "Lo siento mucho pero no pude enteneder el mensaje. ¿Quieres ayuda con alguno de los siguientes conceptos?"
            footer = "Atte: control escolar"
            options = ["Inscripciones", "Pagos", "Documento de reglas"]

            replyButtonData = sendingFormats.interactiveButtonMessage(
                number, options, body, footer, "sed1"
            )
            return Messages.Chatting.sendWhatsappMessage(replyButtonData)
