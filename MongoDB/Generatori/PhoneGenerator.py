from faker import Faker
import csv

fake = Faker() 

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\PhNumbers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'phone'])
    for i in range(1, 21876):
        writer.writerow([i, fake.phone_number()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\PhNumbers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'phone'])
    for i in range(1, 16407):
        writer.writerow([i, fake.phone_number()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\PhNumbers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'phone'])
    for i in range(1, 10938):
        writer.writerow([i, fake.phone_number()])

with open('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\PhNumbers.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'phone'])
    for i in range(1, 5469):
        writer.writerow([i, fake.phone_number()])