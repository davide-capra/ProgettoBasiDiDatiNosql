from neo4j import GraphDatabase

# Connessione al database
def connect_neo(ip: str='localhost', port: str='7687', user: str='neo4j', password: str='123456789'):
    uri = "neo4j://" + ip + ":" + port
    return GraphDatabase.driver(uri, auth=(user, password))

# Creazione di un oggetto Graph
graph = connect_neo().session()

# Query per creare nodi Customers
graph.run("""
    LOAD CSV FROM "file:///Customers.csv" AS csvLine
    CREATE (:Customers {id: csvLine[0], name: csvLine[1], surname: csvLine[2]})
""")

# Query per creare nodi Lawyers
graph.run("""
    LOAD CSV FROM "file:///Lawyers.csv" AS csvLine
    CREATE (:Lawyers {id: csvLine[0], name: csvLine[1], surname: csvLine[2]})
""")

# Query per creare nodi Evaluators
graph.run("""
    LOAD CSV FROM "file:///Evaluators.csv" AS csvLine
    CREATE (:Evaluators {id: csvLine[0], name: csvLine[1], surname: csvLine[2]})
""")

# Query per creare nodi Houses
graph.run("""
    LOAD CSV FROM "file:///Houses.csv" AS csvLine
    CREATE (:Houses {id: csvLine[0], address: csvLine[1]})
""")

# Query per creare nodi Emails
graph.run("""
    LOAD CSV FROM "file:///Emails.csv" AS csvLine
    CREATE (:Emails {id: csvLine[0], emailaddr: csvLine[1]})
""")

# Query per creare nodi PhoneNumbers
graph.run("""
    LOAD CSV FROM "file:///PhNumbers.csv" AS csvLine
    CREATE (:PhoneNumbers {id: csvLine[0], phone: csvLine[1]})
""")

# Query per creare nodi SSNs
graph.run("""
    LOAD CSV FROM "file:///SSNs.csv" AS csvLine
    CREATE (:SSNs {id: csvLine[0], ssn: csvLine[1]})
""")

# Query per creare nodi Claims
graph.run("""
    LOAD CSV FROM "file:///Claims.csv" AS csvLine
    CREATE (:Claims {id: csvLine[0], code: csvLine[1]})
""")

print('Fine popolazione')

graph.run("""WITH range(1,3) as custRange 
MATCH (c:Customers)
WITH collect(c) as customers, custRange
MATCH (h:Houses)
WITH h, apoc.coll.randomItems(customers, apoc.coll.randomItem(custRange)) as customers
FOREACH (customer in customers | CREATE (h)<-[:HAS_ADDRESS]-(customer))""")
print('primo Random')

graph.run("""WITH range (1,3) as emrange
MATCH (e:Emails)
WITH collect(e) as em, emrange
MATCH (c:Customers)
WITH c, apoc.coll.randomItems(em, apoc.coll.randomItem(emrange)) as emails
FOREACH (email in emails | CREATE (c)-[:HAS_MAIL]->(email))""")
print('secondo Random')

graph.run("""WITH range (1,2) as phrange
MATCH (p:PhoneNumbers)
WITH collect(p) as num, phrange
MATCH (c:Customers)
WITH c, apoc.coll.randomItems(num, apoc.coll.randomItem(phrange)) as phnumbers
FOREACH (phnumber in phnumbers | CREATE (c)-[:HAS_PHONE]->(phnumber))""")
print('terzo random')

graph.run("""WITH range (1,1) as ssnrange
MATCH (s:SSNs)
WITH collect(s) as ss, ssnrange
MATCH (c:Customers)
WITH c, apoc.coll.randomItems(ss, apoc.coll.randomItem(ssnrange)) as ssns
FOREACH (ssn in ssns | CREATE (c)-[:HAS_SSN]->(ssn))""")
print ('quarto random')
graph.run("""WITH range(1,5) as claimRange
MATCH (c:Claims)
WITH collect(c) as claims, claimRange
MATCH (l:Lawyers)
WITH l, apoc.coll.randomItems(claims, apoc.coll.randomItem(claimRange)) as claims
FOREACH (claim in claims | CREATE (l)-[:IS_INVOLVED]->(claim))""")

print ('quinto random')

graph.run("""WITH range(1,5) as claimRange
MATCH (c:Claims)
WITH collect(c) as claims, claimRange
MATCH (e:Evaluators)
WITH e, apoc.coll.randomItems(claims, apoc.coll.randomItem(claimRange)) as claims
FOREACH (claim in claims | CREATE (e)-[:IS_EVALUATOR]->(claim))""")
print ('sesto random')


graph.run("""WITH range(0,5) as claimRange
MATCH (c:Claims)
WITH collect(c) as claims, claimRange
MATCH (cu:Customers)
WITH cu, apoc.coll.randomItems(claims, apoc.coll.randomItem(claimRange)) as claims
FOREACH (claim in claims | CREATE (cu)-[:HAS_CLAIM]->(claim))""")
print ('settimo random')



