# plot all the things...

import pymssql
#import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
#import numpy as np
#import matplotlib.animation as animation
#from pylab import *

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
except Exception as e:
    print e


#ion()

# try close and reopen connection...
cursor = conn.cursor()
k = True
#fig = plt.figure()

select_str = ('SELECT top 2000 [datDateTime], [dValue], [iTypeKey], [iUnitKey]  FROM [DogsData].[dbo].[tReading] GROUP BY [datDateTime], [dValue], [iTypeKey], [iUnitKey] ORDER BY max([datDateTime]) DESC')

cursor.execute(select_str)

with open('db_out.csv','w+') as fid:
    fid.write('datDateTime, dValue, iTypeKey, iUnitKey\n')
    for row in cursor:
        out = str(row[0]) +',' + str(row[1]) + ',' + str(row[2])+ ',' +str(row[3])+  '\n'
        fid.write(out)
    conn.close()
