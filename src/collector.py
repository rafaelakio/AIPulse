import feedparser
import json
import os
from src.database import Database

class NewsCollector:
    def __init__(self, feeds_config="config/feeds.json"):
        with open(feeds_config, 'r') as f:
            self.feeds = json.load(f)['feeds']
        self.db = Database()

    def fetch_all(self):
        all_new_articles = []
        for feed in self.feeds:
            print(f"Fetching from: {feed['name']}")
            parsed = feedparser.parse(feed['url'])
            for entry in parsed.entries:
                article_id = entry.get('id', entry.link)
                
                if not self.db.is_news_seen(article_id):
                    article = {
                        'id': article_id,
                        'title': entry.title,
                        'link': entry.link,
                        'published_date': entry.get('published', ''),
                        'source': feed['name'],
                        'summary': entry.get('summary', '')
                    }
                    all_new_articles.append(article)
                    # We don't save yet, we return them for summarization first
        return all_new_articles

if __name__ == "__main__":
    collector = NewsCollector()
    new_stuff = collector.fetch_all()
    print(f"Found {len(new_stuff)} new articles.")
