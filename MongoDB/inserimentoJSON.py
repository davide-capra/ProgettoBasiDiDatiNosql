import pymongo
import json

client = pymongo.MongoClient('mongodb://localhost:27017')
database = client.Insurance100 # Connessione al database basta cambiare il nome del database per selezionare un altro database
collection_names = ['Claims', 'Customers', 'Emails', 'Evaluators', 'Houses', 'Lawyers', 'PhNumbers', 'SSNs']

for name in collection_names: # for per inserire tutti i file JSON
    collection = database[name]
    
    with open(f'C:\\Users\\39377\\Desktop\\JSON\\100\\{name}.json') as file: # Inserire il percorso del file JSON
        data = json.load(file) # Carica il file JSON
        collection.insert_many(data) # Inserisce i documenti in MongoDB
    
    print(f'Inseriti {len(data)} documenti in MongoDB nella collezione {name}.')
