# plot all the things...

import pymssql
import matplotlib.pyplot as plt
import time
from datetime import datetime
import numpy as np
import matplotlib.animation as animation
from pylab import *

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

ion()

# try close and reopen connection...
cursor = conn.cursor()
k = True
#fig = plt.figure()
count =9

cursor.execute('SELECT top 5 [datDateTime], [dValue] FROM [DogsData].[dbo].[tReading] Where [iTypeNumber] = 20 AND [iUnitNumber] = 15 ORDER BY [datDateTime] DESC')

l1 = cursor.fetchall()

dat = []
for i in l1[::-1]:
    dat.append(i[1])

line, = plot(dat)    


while count > 0:

    cursor.execute('SELECT top 5 [datDateTime], [dValue] FROM [DogsData].[dbo].[tReading] Where [iTypeNumber] = 20 AND [iUnitNumber] = 15 ORDER BY [datDateTime] DESC')

    #l1 = cursor.fetchall()
    l1 = cursor.fetchmany()

    print 'for loop'
    dat = []
    for i in l1[::-1]:
        dat.append(list(i)[1])
    line.set_ydata(dat)
    draw()
    
    time.sleep(1)
    
    count += 1

conn.close()