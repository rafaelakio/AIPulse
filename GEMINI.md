# AIPulse: AI News Aggregator & WhatsApp Newsletter

## Project Overview
**AIPulse** is an automated pipeline designed to collect, filter, summarize, and deliver the latest news in Artificial Intelligence directly to WhatsApp. It focuses on high-relevance content, including scientific research, model releases, market trends, and regulations.

## Core Features
1.  **Multi-source Collection:** RSS feeds and web scraping for diverse coverage.
2.  **Smart Filtering:** Deduplication and keyword-based normalization (AI, LLM, Open Source).
3.  **AI Summarization:** Concise summaries (3-5 lines) and bulleted highlights using LLMs (Claude/GPT).
4.  **WhatsApp Optimized Formatting:** Automatic message splitting (~1600 chars) and categorized sections.
5.  **Automated Delivery:** Scheduled daily/weekly updates via Twilio or WhatsApp Cloud API.

## Recommended Architecture
| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Collection** | RSS + Scraping (BeautifulSoup/feedparser) | Source ingestion |
| **Processing** | Python | Business logic, filtering, and normalization |
| **Intelligence** | OpenAI GPT-4 / Anthropic Claude | Summarization and categorization |
| **Storage** | SQLite / PostgreSQL | News history and deduplication |
| **Automation** | n8n / GitHub Actions / Cron | Scheduling and workflow orchestration |
| **Delivery** | Twilio / WhatsApp Cloud API | Message transmission |

## Directory Structure (Planned)
- `src/`: Python source code for collectors, processors, and senders.
- `config/`: Configuration files for RSS feeds and API keys.
- `data/`: Local storage for the news database (SQLite).
- `tests/`: Unit tests for scrapers and summarization logic.

## Getting Started
### Prerequisites
- Python 3.10+
- API Keys for OpenAI/Anthropic and Twilio/Meta.

### Setup (TODO)
- [ ] Initialize Python environment (`venv`).
- [ ] Install dependencies (`pip install feedparser beautifulsoup4 openai twilio`).
- [ ] Configure environment variables (`.env`).

## Development Conventions
- **Category Tags:** 🧠 Research, 🤖 Models, 💼 Market, ⚠️ Regulation.
- **Message Limit:** Hard limit of 1600 characters per message chunk.
- **Scraping Ethics:** Respect `robots.txt` and implement sensible delays.
