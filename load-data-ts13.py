#
#
#Will iterate through the all-data-2.csv csv file and put into Riak in batches of 100
#SMDE 09/05/16

from riak import RiakClient
from riak.util import unix_time_millis,datetime_from_unit_time_millis

from datetime import datetime
import calendar
import csv

            
c=RiakClient()
c.ping()


#to load data in the table

totalcount=0
batchcount=0
batchsize=100  #most efficient batch size per documentation and testing
ds=[]
t=c.table('aarhus13-4')
print t


with open('./traffic_feb_june/all-data-2.csv', 'rU') as infile:  #need to change pathing to match where source file is as necessary
    r=csv.reader(infile)
    for l in r:
		if l[0]!='status':
			newl=[l[0],str(l[3]),datetime.strptime(l[5],'%Y-%m-%dT%H:%M:%S'),int(l[1]),int(l[2]),int(l[4]),int(l[6]),int(l[7]),int(l[8])]
			totalcount=totalcount+1
			#print count
			ds.append(newl)
			newl=""
			batchcount=batchcount+1
			if batchcount==batchsize:
				#add the records to the table
				print "Count at  ", totalcount
				to=t.new(ds)
				print "Created ts object"
				print "Storage result:  ",to.store()
				batchcount=0
				ds=[]       
infile.close()
print "Input file closed"
to=t.new(ds)
print "Storage result:  ",to.store()
print totalcount
