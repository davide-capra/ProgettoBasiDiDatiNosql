from faker import Faker
import csv

fake = Faker()

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\SSNs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'ssn'])
    for i in range(1, 31251):
        writer.writerow([i, fake.ssn()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\SSNs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'ssn'])
    for i in range(1, 23438):
        writer.writerow([i, fake.ssn()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\SSNs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'ssn'])
    for i in range(1, 15626):
        writer.writerow([i, fake.ssn()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\SSNs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'ssn'])
    for i in range(1, 7813):
        writer.writerow([i, fake.ssn()])