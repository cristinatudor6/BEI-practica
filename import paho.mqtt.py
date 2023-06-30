import paho.mqtt.client as mqtt
from pymongo import MongoClient

# Setări pentru MQTT
mqtt_broker = "adresa_brokerului_mqtt"
mqtt_port = 1883
mqtt_topic = "topicul_tau"

# Setări pentru MongoDB
mongo_host = "adresa_serverului_mongodb"
mongo_port = 27017
mongo_db = "numele_bazei_de_date"
mongo_collection = "numele_colecției"

# Funcție pentru gestionarea mesajelor primite prin MQTT
def on_message(client, userdata, msg):
    # Decodifică mesajul JSON primit
    payload = msg.payload.decode('utf-8')
    
    # Salvează datele în baza de date
    try:
        client = MongoClient(mongo_host, mongo_port)
        db = client[mongo_db]
        collection = db[mongo_collection]
        collection.insert_one(payload)
        print("Datele au fost salvate cu succes în baza de date.")
    except Exception as e:
        print("Eroare la salvarea datelor în baza de date:", str(e))
    finally:
        client.close()

# Crează un client MQTT și setează funcția de gestionare a mesajelor
client = mqtt.Client()
client.on_message = on_message

# Conectează-te la brokerul MQTT
client.connect(mqtt_broker, mqtt_port)
client.subscribe(mqtt_topic)

# Intră în bucla de așteptare pentru a primi mesaje
client.loop_forever()