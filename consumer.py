import json
from kafka import KafkaConsumer

# Initialiser un consommateur Kafka
consumer = KafkaConsumer(
    'topic-stock-prices',  # Nom du topic à consommer
    bootstrap_servers=['localhost:9092' ],
    auto_offset_reset='earliest',  # Commencer à consommer dès le début du topic
    enable_auto_commit=True,
    group_id='stock-analysis-group',  # ID de groupe pour ce consommateur
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

