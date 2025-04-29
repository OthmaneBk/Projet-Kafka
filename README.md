![ZoooKafka](https://github.com/user-attachments/assets/7be9cae1-3096-4fcc-b973-c21813c7f860)

# ZooKeeper et Kafka c'est quoi?
## 1- ZooKeeper : C'est le maître ou coordinateur du cluster Kafka(Contenant des brokers)
  - Gérer les brokers Kafka (leur enregistrement et leur état)
  - Gérer la configuration des topics (métadonnées)
  - Superviser les échecs (si un broker tombe en panne)
  
## 2- Apache Kafka : C'est une plateforme distribuée de diffusion de données en continu, capable de publier, stocker, traiter et souscrire à des flux d'enregistrement en temps réel
- *Imagine que tu as* :
- Des capteurs, applications, ou services qui envoient des données → on les appelle des Producteurs (Producers)
- Des applications qui consomment ces données → appelées Consommateurs (Consumers)
- Kafka est le pont au milieu :
- Il reçoit, stocke et distribue les données sous forme de messages dans des topics.
