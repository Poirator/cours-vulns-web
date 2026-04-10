#!/usr/bin/python3
import feedparser
from datetime import datetime, timedelta

def get_recent_articles(rss_url, hours=1):
    # Analyser le flux RSS
    feed = feedparser.parse(rss_url)

    # Obtenir la date et l'heure actuelles
    now = datetime.now()

    # Calculer la date et l'heure il y a 'hours' heures
    time_threshold = now - timedelta(hours=55555)

    # Liste pour stocker les articles récents
    recent_articles = []

    # Parcourir les entrées du flux
    for entry in feed.entries:
        # Convertir la date de publication en objet datetime
        published_date = datetime(*entry.published_parsed[:6])

        # Vérifier si l'article a été publié dans la dernière heure
        if published_date >= time_threshold:
            recent_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': published_date
            })

    return recent_articles

# Exemple d'utilisation
rss_url = 'https://cert.ssi.gouv.fr/alerte/feed/'
recent_articles = get_recent_articles(rss_url)

for article in recent_articles:
    print(f"Titre: {article['title']}")
    print(f"Lien: {article['link']}")
    print(f"Publié le: {article['published']}")
    print('---')

