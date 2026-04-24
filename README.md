# AIPulse 🚀

**AIPulse** é um agregador de notícias de Inteligência Artificial automatizado que coleta feeds, resume conteúdos usando GPT-4 e envia um boletim formatado diretamente para o WhatsApp.

Este projeto foi desenhado para profissionais e entusiastas que desejam se manter atualizados com o que há de mais relevante no mundo da IA sem ruídos.

---

## 🛠️ Funcionalidades

- **Coleta Multi-fonte:** Suporte a múltiplos feeds RSS configuráveis.
- **Deduplicação Inteligente:** Armazenamento em SQLite para evitar o reprocessamento de notícias já lidas.
- **Sumarização com IA:** Resumos concisos (3-5 linhas) focados em impacto, gerados por modelos de ponta (OpenAI GPT-4).
- **Integração WhatsApp:** Abre automaticamente o WhatsApp Desktop com o boletim pronto para envio.
- **Arquitetura Modular:** Fácil de estender com novos coletores ou métodos de envio (Telegram, Slack, e-mail).

---

## 📂 Estrutura do Projeto

```text
AIPulse/
├── config/             # Configurações de feeds (JSON)
├── data/               # Banco de dados local (SQLite)
├── src/                # Código fonte (Collector, Summarizer, Sender)
├── tests/              # Testes unitários e de integração
├── .env.example        # Modelo de variáveis de ambiente
├── GEMINI.md           # Contexto operacional para IA (Gemini CLI)
└── requirements.txt    # Dependências do projeto
```

---

## 🚀 Como Começar

### Pré-requisitos
- Python 3.10 ou superior.
- Uma conta na [OpenAI](https://platform.openai.com/) (para sumarização).
- WhatsApp Desktop instalado (opcional, para envio via Desktop).

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/aipulse.git
   cd aipulse
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Copie o arquivo `.env.example` para `.env` e preencha suas chaves.
   ```bash
   cp .env.example .env
   ```

### Execução

Para rodar o pipeline completo de coleta, sumarização e preparação do envio:
```bash
python src/main.py
```

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! 

1. Faça um **Fork** do projeto.
2. Crie uma **Branch** para sua feature (`git checkout -b feature/nova-feature`).
3. Faça o **Commit** de suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Envie para o **Repo Principal** (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

*Desenvolvido com o auxílio do Gemini CLI.*
