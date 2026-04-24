import webbrowser
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppSender:
    def __init__(self):
        # Você pode configurar seu número no .env como WHATSAPP_NUMBER=5511999999999
        self.phone_number = os.getenv("WHATSAPP_NUMBER", "")

    def format_newsletter(self, articles):
        if not articles:
            return "Nenhuma nova notícia de IA encontrada hoje."

        message = "🚀 *AIPulse - Boletim de IA* 🚀\n\n"
        
        for art in articles:
            title = art.get('title', 'Sem título')
            summary = art.get('ai_summary', 'Resumo não disponível.')
            link = art.get('link', '')
            
            message += f"🔹 *{title}*\n"
            message += f"{summary}\n"
            if link:
                message += f"🔗 Leia mais: {link}\n"
            message += "\n" + "-"*20 + "\n\n"
            
        return message

    def send_via_desktop(self, message):
        """
        Abre o navegador ou WhatsApp Desktop com a mensagem preparada.
        """
        # Codifica o texto para URL
        encoded_message = urllib.parse.quote(message)
        
        # Link wa.me funciona tanto no Web quanto no Desktop (ele pergunta se quer abrir o app)
        url = f"https://wa.me/{self.phone_number}?text={encoded_message}"
        
        print(f"Abrindo WhatsApp para enviar {len(message)} caracteres...")
        webbrowser.open(url)

if __name__ == "__main__":
    # Teste rápido
    sender = WhatsAppSender()
    test_msg = sender.format_newsletter([
        {"title": "IA Revolucionária", "ai_summary": "Uma nova IA foi lançada hoje.", "link": "http://google.com"}
    ])
    sender.send_via_desktop(test_msg)
