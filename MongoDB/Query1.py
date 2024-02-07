import pymongo
import time
import csv


client = pymongo.MongoClient("mongodb://localhost:27017/") # Connessione al server MongoDB in Docker
db = client['Insurance100'] # Connessione al database
lawyers_collection = db['Lawyers'] # Connessione alla collezione Lawyers
filter_lawyers = {"_id": 0, "claims": 1} # Filtra i risultati per mostrare solo i campi "claims"
query_lawyers = {'id': 3} # Filtra i risultati per mostrare solo i Lawyers con id 3
num_executions = 30 # Numero di esecuzioni successive

# Clear plan cache for Lawyers
db.command({"planCacheClear": "Lawyers"}) # Pulisce la cache per la collezione Lawyers

def run_query(): # Esecuzione della query senza cache
    # Define the pipeline stages for the query
    query_pipeline = [{"$match": query_lawyers},{"$project": filter_lawyers},{"$unwind": "$claims"}] # Definizione delle fasi del pipeline per la query

    # First execution
    beginning = time.time() # Inizio del cronometro
    claims_result = list(lawyers_collection.aggregate(query_pipeline)) # Esecuzione della query
    end = time.time() - beginning # Fine del cronometro
    time_not_cached = end * 1000  # Convert to milliseconds

    # Print results of the first execution
    print("Results of the first execution:")
    for result in claims_result:
        print(result)

    # Next 30 executions
    time_query = []
    beginning_30 = time.time()
    for _ in range(num_executions): # Esecuzioni successive (30 volte)
        beg_query = time.time()
        claims_result = list(lawyers_collection.aggregate(query_pipeline))
        end_query = time.time() - beg_query
        time_query.append(end_query * 1000)  # Convert to milliseconds

    # Calculate mean time
    mean_time = sum(time_query) / len(time_query) # Calcolo del mean time

    # Write to CSV with string conversion for decimal values
    with open("C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\MongoDB\\Risultati\\Query100%\\QueryI100%.csv", 'w', newline='') as csvfile:
        fieldnames = ['Not Cached', 'Execution Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
        writer.writerow({'Not Cached': '{:.6f}'.format(time_not_cached), 'Execution Time': ''})
        for i, query_time in enumerate(time_query, start=1):
            writer.writerow({'Not Cached': '', 'Execution Time': '{:.6f}'.format(query_time)})
        writer.writerow({'Not Cached': 'Mean Time', 'Execution Time': '{:.6f}'.format(mean_time)})

# Esempio di utilizzo
run_query() # Esecuzione della query senza cache
