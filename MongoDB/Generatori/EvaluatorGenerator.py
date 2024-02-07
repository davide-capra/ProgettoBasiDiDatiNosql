from faker import Faker
import csv

fake = Faker() 

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Evaluators.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 3126):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Evaluators.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 2344):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Evaluators.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 1563):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Evaluators.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 1563):
        writer.writerow([i, fake.first_name(), fake.last_name()])