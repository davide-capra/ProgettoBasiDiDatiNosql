import pymongo
import time
import csv

client = pymongo.MongoClient()
db = client['Insurance100']
lawyers = db["Lawyers"]
customers = db["Customers"]
#filter_customers = {"_id": 0, "name": 1, "surname": 1}
query_lawyers = {'id': 3}
num_executions = 30

# Cancella la cache per Lawyers e Customers
db.command({"planCacheClear": "Lawyers"})
db.command({"planCacheClear": "Customers"})
# definisci la pipeline di query
query_pipeline = [
    {"$match": {"id": 3}},
    {"$project": {"_id": 0, "claims": 1}},
    {"$unwind": "$claims"},
    {"$lookup": {
        "from": "Customers",
        "localField": "claims",
        "foreignField": "claim",
        "as": "customer"
    }},
    {"$unwind": "$customer"},
    {"$project": {"name": "$customer.name", "surname": "$customer.surname"}}
]

# Prima esecuzione
beginning = time.time()
cust_claims = list(lawyers.aggregate(query_pipeline))
end = time.time() - beginning
time_not_cached = end * 1000  # Converte in millisecondi
print("Results of the first execution:")
for result in cust_claims:
    print(result)

# Prossime 30 esecuzioni
time_query = []
beginning_30 = time.time()
for _ in range(num_executions):
    beg_query = time.time()
    cust_claims = list(lawyers.aggregate(query_pipeline))
    end_query = time.time() - beg_query
    time_query.append(end_query * 1000)  # Converte in millisecondi

# Calcola il tempo medio
mean_time = sum(time_query) / len(time_query)

# scrive sul file CSV
with open("C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\MongoDB\\Risultati\\Query100%\\QueryIII100%.csv", 'w', newline='') as csvfile:
    fieldnames = ['Not Cached', 'Execution Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Not Cached': '{:.6f}'.format(time_not_cached), 'Execution Time': ''})
    for i, query_time in enumerate(time_query, start=1):
        writer.writerow({'Not Cached': '', 'Execution Time': '{:.6f}'.format(query_time)})
    writer.writerow({'Not Cached': 'Mean Time', 'Execution Time': '{:.6f}'.format(mean_time)})
