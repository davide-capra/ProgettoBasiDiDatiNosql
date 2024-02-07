import csv
from faker import Faker

fake=Faker()


with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Emails.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','email'])
    for i in range (1, 21876):
        writer.writerow([i,fake.email()])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Emails.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','email'])
    for i in range (1, 16407):
        writer.writerow([i,fake.email()])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Emails.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','email'])
    for i in range (1, 10938):
        writer.writerow([i,fake.email()])
with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Emails.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','email'])
    for i in range (1, 5469):
        writer.writerow([i, fake.email()])