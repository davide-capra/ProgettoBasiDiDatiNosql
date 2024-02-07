import pymongo
import time
import csv

client = pymongo.MongoClient()
db = client['Insurance100']
lawyers = db["Lawyers"]
evaluators = db["Evaluators"]
#filter_evaluators = {"_id": 0, "name": 1, "surname": 1}
query_lawyers = {'id': 3}
num_executions = 30

def run_query():
    # Clear plan cache for Lawyers and Evaluators
    db.command({"planCacheClear": "Lawyers"})
    db.command({"planCacheClear": "Evaluators"})
    query_pipeline = [
        {"$match": {"id": 3}},
        {"$project": {"_id": 0, "claims": 1}},
        {"$unwind": "$claims"},
        {"$lookup": {
            "from": "Evaluators",
            "localField": "claims",
            "foreignField": "claims",
            "as": "evaluator"
        }},
        {"$unwind": "$evaluator"},
        {"$project": {"name": "$evaluator.name", "surname": "$evaluator.surname"}}
    ]

    # First execution
    beginning = time.time()
    evaluators_result = list(lawyers.aggregate(query_pipeline))
    end = time.time() - beginning
    time_not_cached = end * 1000  # Convert to milliseconds

    # Print results of the first execution
    print("Results of the first execution:")
    for result in evaluators_result:
        print(result)

    # Next 30 executions
    time_query = []
    beginning_30 = time.time()
    for _ in range(num_executions):
        beg_query = time.time()
        evaluators_result = list(lawyers.aggregate(query_pipeline))
        end_query = time.time() - beg_query
        time_query.append(end_query * 1000)  # Convert to milliseconds

    # Calculate mean time
    mean_time = sum(time_query) / len(time_query)

    # Write to CSV
    with open("C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\MongoDB\\Risultati\\Query100%\\QueryII100%.csv", 'w', newline='') as csvfile:
        fieldnames = ['Not Cached', 'Execution Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Not Cached': '{:.6f}'.format(time_not_cached), 'Execution Time': 'Not Cached'})
        for i, query_time in enumerate(time_query, start=1):
            writer.writerow({'Not Cached': '', 'Execution Time': '{:.6f}'.format(query_time)})
        writer.writerow({'Not Cached': 'Mean Time', 'Execution Time': '{:.6f}'.format(mean_time)})

run_query() # funzione che esegue la query e salva i risultati in un file CSV
