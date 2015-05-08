# THis is a ruff draft for serverside plotting for csc 687. This will 
# produce the actual media files to be displayed on the website created
# by Rick. This program needs extensive work to integrate wtih Rick's tools properly.
#
# This will now read in several files and create plots that way

# plot all the things...


import plotly.plotly as py
from plotly.graph_objs import *
#import pymssql
#import _mssql
#import time
#from datetime import datetime
#import numpy as np
#from pylab import plot
from sys import argv
import os
import csv
#from default_ini import ini as default

# Server type: Database Engine
# Server name: csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com,1433
# Authentication: SQL Server Authentication
# Login: sd_admin
# password: aaaaaaaa

print os.path.dirname('in.csv')
# for matplotlib

# get file path and name
# defalut ini values
ini = {}
full_path = argv[1]
with open(full_path,'r') as fin:
    file = csv.reader(fin)
    for row in file:
        ini[row[0]] = row[1]

x = []
y = []
with open(ini['data_in'],'r') as dat:
    data = csv.reader(dat)
    for d in data:
        x.append(int(d[0]))
        y.append(int(d[1]))

print 'setting up final plot'
t = Scatter(x=x,y=y)
data = Data([t])
plot_url = py.plot(data, filename='basic-line')
print plot_url
#line, = plt.plot(x,y)
#out_loc = os.path.join(ini['output_location'], ini['output_file'])
#plt.savefig('test.png')