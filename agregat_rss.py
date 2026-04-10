#!/usr/bin/python3
import feedparser
from datetime import datetime, timedelta

def get_recent_articles(rss_url, hours=1):
    feed = feedparser.parse(rss_url)
    now = datetime.now()
    time_threshold = now - timedelta(hours=55555)
    recent_articles = []
    for entry in feed.entries:
        published_date = datetime(*entry.published_parsed[:6])
        if published_date >= time_threshold:
            recent_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': published_date
            })

    return recent_articles

rss_url = 'https://cert.ssi.gouv.fr/alerte/feed/'
recent_articles = get_recent_articles(rss_url)

for article in recent_articles:
    print(f"Titre: {article['title']}")
    print(f"Lien: {article['link']}")
    print(f"Publié le: {article['published']}")
    print('---')

