from py2neo import Graph
import time
import csv

# Modifica queste variabili con i tuoi dati di connessione
uri = "bolt://localhost:7687"
user = "neo4j"
password = "123456789"

# Connessione al database
graph = Graph(uri, auth=(user, password))

timequery = []
mean = 0

# Prima esecuzione
graph.run("""CALL db.clearQueryCaches()""")
beginning = time.time()
res = graph.run("""MATCH (l:Lawyers {id: '3'})-[:IS_INVOLVED]->(Claims)
RETURN Claims.id""")
for re in res:
    print(re)
end = (time.time() - beginning) * 1000  # Converti il tempo in millisecondi

# Prossime 30 esecuzioni
beginning30 = time.time()
for i in range(1, 31):
    begquery = time.time()
    res = graph.run("""MATCH (l:Lawyers {id: '3'})-[:IS_INVOLVED]->(Claims)
RETURN Claims.id""")
    endquery = (time.time() - begquery) * 1000  # Converti il tempo in millisecondi
    timequery.append(endquery)
    #for re in res:
        #print(re)
end30 = (time.time() - beginning) * 1000  # Converti il tempo in millisecondi

# Calcolo del tempo medio
for i in range(len(timequery)):
    mean += timequery[i]
mean /= len(timequery)

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\Neo4j\\RisultatiNeo4j\\Query100%\\QueryI100%.csv', 'w') as results:
    writer = csv.writer(results)
    writer.writerow(['Esecuzione', 'Tempo (ms)'])
    writer.writerow(['Non memorizzato nella cache', end])
    for i in range(len(timequery)):
        writer.writerow([i+1, timequery[i]])
    writer.writerow(['Tempo Medio', mean])

