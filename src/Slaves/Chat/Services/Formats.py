class SendingFormats:

    def interactiveButtonMessage(self, number, options, body, footer, sedd):
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

    
    def interactiveListMessage(self, number: int, options: dict, body: str, footer: str):
        rows = []
        for i in range(len(options["id"])):
            rows.append(
                {
                    "id": f"Seed{options["id"][i]}_row_{i + 1}",
                    "title": options["name"][i],
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
                    "sections": [
                        {
                            "title": "Sections",
                            "rows": rows
                        }
                    ],
                },
            },
        }
        return data


    def documentMessage(self, number, url, caption, filename, footer):
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
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {"body": text},
        }
        return data