from neo4j import GraphDatabase
import csv

def run_query_and_save_to_csv(query, file_path):
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "123456789"

    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        with driver.session() as session:
            result = session.run(query)

            # Apri un file CSV nel percorso specificato
            with open(file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                # Scrivi l'intestazione del CSV basata sui nomi delle colonne
                csv_writer.writerow(result.keys())

                # Scrivi ogni riga del risultato nel file CSV
                for record in result:
                    csv_writer.writerow(record.values())

# Esegue le query e salva i risultati nei file CSV desiderati
run_query_and_save_to_csv("MATCH (c:Customers) RETURN c.id as id, c.name as name, c.surname as surname,[(c)-[:HAS_PHONE]->(Ph) | Ph.phone] as phone, [(c)-[:HAS_ADDRESS]->(add) | add.id] as address, [(c)-[:HAS_CLAIM]->(cl) | cl.id] as claim, [(c)-[:HAS_MAIL]->(em) | em.emailaddr] as email, [(c)-[:HAS_SSN]->(s) | s.ssn ] as ssn", "C:\\Users\\39377\\Desktop\\100\\Customers.csv")

run_query_and_save_to_csv("MATCH (c:Lawyers) RETURN c.id as id, c.name as name, c.surname as surname, [(c)-[:IS_INVOLVED]->(cl) | cl.id] as claims", "C:\\Users\\39377\\Desktop\\100\\Lawyers.csv")

run_query_and_save_to_csv("MATCH (c:Evaluators) RETURN c.id as id, c.name as name, c.surname as surname, [(c)-[:IS_EVALUATOR]->(cl) | cl.id] as claims", "C:\\Users\\39377\\Desktop\\100\\Evaluators.csv")
