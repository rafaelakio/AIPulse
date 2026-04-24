import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AISummarizer:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("Warning: OPENAI_API_KEY not found in .env")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def summarize(self, title, content):
        if not self.client:
            return "Summarization skipped: No API Key."

        prompt = f"""
        Resuma a seguinte notícia de IA para um boletim de WhatsApp.
        Instruções:
        - Use no máximo 3 a 5 linhas.
        - Use bullets para destaques se necessário.
        - Linguagem clara e profissional.
        - Foque no impacto da notícia.
        - Se possível, categorize em: Pesquisa, Modelo, Mercado ou Regulação.

        Título: {title}
        Conteúdo: {content}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Você é um especialista em IA resumindo notícias para profissionais."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Erro na sumarização: {str(e)}"

if __name__ == "__main__":
    summarizer = AISummarizer()
    test_res = summarizer.summarize("Novo modelo Claude 3.5 Sonnet", "A Anthropic lançou o Claude 3.5 Sonnet que supera o GPT-4o em benchmarks.")
    print(test_res)
