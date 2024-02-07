import pymongo
import time
import csv

client = pymongo.MongoClient()  # Connessione al server MongoDB in Docker
db = client['Insurance100']
lawyers = db["Lawyers"]
customers = db["Customers"]
houses = db["Houses"]

# Esecuzione della query senza cache
start_time_first = time.time()

result = lawyers.aggregate([
    {"$match": {"id": 3}},
    {"$lookup": {"from": "Claims", "localField": "claims", "foreignField": "id", "as": "lawyer_claims"}},
    {"$unwind": "$lawyer_claims"},
    {"$lookup": {"from": "Customers", "localField": "lawyer_claims.id", "foreignField": "claim", "as": "customer"}},
    {"$unwind": "$customer"},
    {"$lookup": {"from": "Houses", "localField": "customer.address", "foreignField": "zip", "as": "house"}},
    {"$project": {"_id": 0, "customer_name": "$customer.name", "customer_surname": "$customer.surname", "customer_address": "$house.address"}}
])

cust_living_in_place = list(result)

end_time_first = time.time()
execution_time_first = (end_time_first - start_time_first) * 1000  # Tempo in millisecondi

print("Tempo della query senza cache:", execution_time_first, "ms")

# Esecuzioni successive (30 volte)
time_queries = []
for i in range(30):
    start_time = time.time()

    result = lawyers.aggregate([
        {"$match": {"id": 3}},
        {"$lookup": {"from": "Claims", "localField": "claims", "foreignField": "id", "as": "lawyer_claims"}},
        {"$unwind": "$lawyer_claims"},
        {"$lookup": {"from": "Customers", "localField": "lawyer_claims.id", "foreignField": "claim", "as": "customer"}},
        {"$unwind": "$customer"},
        {"$lookup": {"from": "Houses", "localField": "customer.address", "foreignField": "zip", "as": "house"}},
        {"$project": {"_id": 0, "customer_name": "$customer.name", "customer_surname": "$customer.surname", "customer_address": "$house.address"}}
    ])

    cust_living_in_place = list(result)


    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Tempo in millisecondi
    time_queries.append(execution_time)

# Calcolo del mean time
mean_time = sum(time_queries) / len(time_queries)

# Scrivi i tempi nel file CSV
csv_filename = "C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\MongoDB\\Risultati\\Query100%\\QueryIV100%.csv"
with open(csv_filename, 'w', newline='') as results_file:
    writer = csv.writer(results_file)
    writer.writerow(['Execution', 'Time'])
    writer.writerow(['Not Cached', execution_time_first])
    for i, time_query in enumerate(time_queries, start=1):
        writer.writerow([i, time_query])
    writer.writerow(['Mean Time', mean_time])


