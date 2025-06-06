import json 
from kafka import KafkaProducer 


# Initialiser un producteur Kafka
producer = KafkaProducer( 
    bootstrap_servers=[ 'localhost:9092' ], 
    value_serializer= lambda x: json.dumps(x).encode( 'utf-8' ) 
)
