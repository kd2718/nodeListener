# plot all the things...

import pymssql
# import matplotlib.pyplot as plt

# Server type: Database Engine
# Server name: csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com,1433
# Authentication: SQL Server Authentication
# Login: sd_admin
# password: aaaaaaaa

server = 'csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com'
suser = 'sd_admin'
spass = 'aaaaaaaa'

try:
    print "opening connection"
    conn = pymssql.connect(server=server, user=suser, password=spass, database="DogsData")
    print "is it open?"
except Exception as e:
    print e

cursor = conn.cursor()
    
while True:

    cursor.execute('SELECT top 5 [datDateTime], [dValue] FROM [DogsData].[dbo].[tReading] Where [iTypeNumber] = 20 AND [iUnitNumber] = 15 ORDER BY [datDateTime] DESC')

    l1 = cursor.fetchall()

    print l1
    print list(l1)

    for i in l1:
        print list(i)[1]

conn.close()