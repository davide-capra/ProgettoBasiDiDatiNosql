import random, string
import csv


with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\100%\\Claims.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','code'])
    for i in range (1, 6251):
        writer.writerow([i,''.join(random.choices(string.ascii_letters + string.digits, k=16))])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\75%\\Claims.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','code'])
    for i in range (1, 4688):
        writer.writerow([i,''.join(random.choices(string.ascii_letters + string.digits, k=16))])

with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\50%\\Claims.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','code'])
    for i in range (1, 3125):
        writer.writerow([i,''.join(random.choices(string.ascii_letters + string.digits, k=16))])
with open ('C:\\Users\\39377\\Desktop\\ProgettoDbNoSql\\CSV\\25%\\Claims.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','code'])
    for i in range (1, 1562):
        writer.writerow([i, ''.join(random.choices(string.ascii_letters + string.digits, k=16))])
        