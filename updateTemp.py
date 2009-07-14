import sqlite3, sys, datetime
import getTemp

#setings
sensorLookUp = {"10 DE C6 35 1 8 0 86" : "outside", \
		"10 C4 EB 35 1 8 0 6" : "test"}


date = datetime.datetime.now().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M")
sensorReadings = {}
while 1:
	try:
		temp, rom = getTemp.getTemp()
	except:
		print "not able to get temp at", date, time
		sys.exit()
	if rom != "null":
		sensorReadings[sensorLookUp[rom]] = temp
	else:
		break
	


conn = sqlite3.connect("/home/simon/tempLog/temp.db")
c = conn.cursor()
for sensor in sensorReadings:
	c.execute("insert into temp values(?, ?, ?, ?)",\
		 [date, time, sensorReadings[sensor], sensor])

conn.commit();
c.close()
