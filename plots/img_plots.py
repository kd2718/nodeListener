# THis is a ruff draft for serverside plotting for csc 687. This will 
# produce the actual media files to be displayed on the website created
# by Rick. This program needs extensive work to integrate wtih Rick's tools properly.

# plot all the things...


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pymssql
import time
from datetime import datetime
import numpy as np
import matplotlib.animation as animation
from pylab import ion, plot, draw

# Server type: Database Engine
# Server name: csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com,1433
# Authentication: SQL Server Authentication
# Login: sd_admin
# password: aaaaaaaa

delay = .03334

server = 'csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com'
suser = 'sd_admin'
spass = 'aaaaaaaa'

try:
    print "opening connection"
    conn = pymssql.connect(server=server, user=suser, password=spass, database="DogsData")
except Exception as e:
    print e


ion()

# try close and reopen connection...
cursor = conn.cursor()
k = True
#fig = plt.figure()

select_str = ('SELECT top 200 [datDateTime], [dValue]  FROM [DogsData].[dbo].[tReading] Where [iTypeNumber] = 20 AND [iUnitNumber] = 15 GROUP BY [datDateTime], [dValue] ORDER BY max([datDateTime]) DESC')

cursor.execute(select_str)

dat = []
for row in cursor:
    dat.append(row[1])

line, = plot(dat)    

print "starting main loop"
while True:

    cursor.execute(select_str)

    dat = []
    for row in cursor:
        dat.append(row[1])
        
    line.set_ydata(dat[::-1])
    #draw()
    savefig('test.png')
    
    time.sleep(delay)

conn.close()