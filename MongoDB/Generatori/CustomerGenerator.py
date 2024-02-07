from faker import Faker
import csv

fake = Faker() 

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Customers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 31251):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Customers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name','surname'])
    for i in range(1, 23438):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Customers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name','surname'])
    for i in range(1, 15626):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Customers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name','surname'])
    for i in range(1, 7813):
        writer.writerow([i, fake.first_name(), fake.last_name()])