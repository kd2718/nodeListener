# THis is a for serverside plotting for csc 687. This will 
# produce the actual media files to be displayed on the website created
# by Rick. 
# Inputs: 
#    input file: comma seperated (csv file). Format of input file is in progress.
#    Datafile: path to datafile is specifed in input file.
# 
#
# This will now read in several files and create plots that way

# plot all the things...


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
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

####### SAMPLE INI
# rate,1
# xscale,20
# ymax,100
# ymin,-1
# title,This is the plot Title
# xlabel,this is the x axis label
# ylabel,this is the y axis label
# color,red
# output_location,
# output_file,name.png
# data_in,in.csv

ini = {}
full_path = argv[1]

fig = plt.figure()
with open(full_path,'r') as fin:
    file = csv.reader(fin)
    for row in file:
        ini[row[0]] = row[1]

x = []
y = []
with open(ini['data_in'],'r') as dat:
    data = csv.reader(dat)
    for d in data:
        # this is the exact format from the server
        xdate = datetime.strptime(d[0],'%Y-%m-%d %H:%M:%S.%f')
        x.append(xdate)
        y.append(float(d[1]))

# use ini defaults if not provided
plt.plot(x,y)
plt.xlabel(ini['xlabel'])
plt.ylabel(ini['ylabel'])
plt.title(ini['title'])
print x[1], x[-1], int(ini['ymin']), int(ini['ymax'])
plt.axis([min(x), max(x), int(ini['ymin']), int(ini['ymax'])])
out_loc = os.path.join(ini['output_location'], ini['output_file'])
print out_loc
fig.autofmt_xdate()
plt.savefig(out_loc)