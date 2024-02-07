import csv
from faker import Faker

fake = Faker()
with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Houses.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['zip', 'address'])
    for i in range (1, 25001):
        writer.writerow([i, fake.address()])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Houses.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['zip', 'address'])
    for i in range (1, 18751):
        writer.writerow([i, fake.address()])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Houses.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['zip', 'address'])
    for i in range (1, 12501):
        writer.writerow([i, fake.address()])
        
with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Houses.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['zip', 'address'])
    for i in range (1, 6251):
        writer.writerow([i, fake.address()])
