import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self, db_path="data/news.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS news (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    link TEXT,
                    published_date TEXT,
                    source TEXT,
                    summary TEXT,
                    category TEXT,
                    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def is_news_seen(self, news_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM news WHERE id = ?", (news_id,))
        return cursor.fetchone() is not None

    def save_news(self, news_data):
        with self.conn:
            self.conn.execute("""
                INSERT OR IGNORE INTO news (id, title, link, published_date, source, summary, category)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                news_data['id'],
                news_data['title'],
                news_data['link'],
                news_data.get('published_date'),
                news_data.get('source'),
                news_data.get('summary'),
                news_data.get('category')
            ))

    def close(self):
        self.conn.close()
