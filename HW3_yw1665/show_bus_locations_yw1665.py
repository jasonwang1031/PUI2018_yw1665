import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def ReadData(key,line):
        #pull and read data from mta api
        #return a json file
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&LineRef={}".format(key,line)
	response = urllib.urlopen(url)
	data = response.read().decode("utf-8")
	data = json.loads(data)
	return data

def ProcessData(data):
        #print latitude and longitude of each bus
	MonitedVehicles = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	print("Bus Line : "+line)
	print("Number of Active Buses : {}".format(len(MonitedVehicles)))

	n = 0
	while n < len(MonitedVehicles):
		latitude = MonitedVehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		longitude = MonitedVehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print("Bus {} is at latitude {} and longitude {}".format(n, latitude, longitude))
		n+=1


key = sys.argv[1]
line = sys.argv[2]
data = ReadData(key, line)
ProcessData(data)

