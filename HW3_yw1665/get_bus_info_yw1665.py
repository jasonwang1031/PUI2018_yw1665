import pylab as pl
import os
import json
import sys
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib



def ReadData(key,line):
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(key,line)
	response = urllib.urlopen(url)
	data = response.read().decode("utf-8")
	data = json.loads(data)
	return data

def ProcessData(data):
	MonitedVehicles = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	
	file = open(FileName, "w")
	file.write("Latitude,Longitude,Stop Name,Stop Status\n")
	n = 0
	while n < len(MonitedVehicles):
		latitude = MonitedVehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		longitude = MonitedVehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		
		try:
			StopName =  MonitedVehicles[n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
		except:
			StopName = "N/A"
				
		try:
			Status = MonitedVehicles[n]['MonitoredVehicleJourney']["OnwardCalls"]['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
		except:
			Status = "N/A"
		file.write('{},{},{},{}\n'.format(latitude, longitude, StopName, Status))
		n+=1
	file.close()

key = sys.argv[1]
line = sys.argv[2]
FileName = sys.argv[3]
data = ReadData(key, line)
ProcessData(data)


