from src.collector import NewsCollector
from src.summarizer import AISummarizer
from src.database import Database
from src.sender import WhatsAppSender
import time

def main():
    print("--- AIPulse News Pipeline Starting ---")
    
    collector = NewsCollector()
    summarizer = AISummarizer()
    db = Database()
    sender = WhatsAppSender()

    # 1. Coleta
    new_articles = collector.fetch_all()
    print(f"Encontrados {len(new_articles)} novos artigos.")

    if not new_articles:
        print("Sem novidades por enquanto.")
        return

    # 2. Processamento e Sumarização
    processed_articles = []
    # Limitamos a 5 para não estourar o limite de caracteres do WhatsApp em um único bloco
    for article in new_articles[:5]:
        print(f"\nProcessando: {article['title']}")
        
        summary = summarizer.summarize(article['title'], article['summary'])
        article['ai_summary'] = summary
        
        # 3. Salvar no Banco
        db.save_news(article)
        processed_articles.append(article)
        print(f"Resumo gerado e salvo.")
        
        time.sleep(1)

    # 4. Formatação e Envio (Desktop Link)
    if processed_articles:
        newsletter = sender.format_newsletter(processed_articles)
        print("\nGerando link para WhatsApp Desktop...")
        sender.send_via_desktop(newsletter)

    print(f"\n--- Pipeline Finalizado. {len(processed_articles)} artigos processados. ---")
    db.close()

if __name__ == "__main__":
    main()
