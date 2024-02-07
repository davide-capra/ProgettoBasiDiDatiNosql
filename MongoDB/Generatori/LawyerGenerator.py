from faker import Faker
import csv

fake = Faker()  

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Lawyers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 4688):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Lawyers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 3516):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Lawyers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 2344):
        writer.writerow([i, fake.first_name(), fake.last_name()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Lawyers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'surname'])
    for i in range(1, 1172):
        writer.writerow([i, fake.first_name(), fake.last_name()])
