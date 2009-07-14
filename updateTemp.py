import sqlite3, sys, datetime
import getTemp

try:
	temp = getTemp.getTemp()
except:
	print "not able to get temp"
	sys.exit()

conn = sqlite3.connect("/home/simon/tempLog/temp.db")
c = conn.cursor()
date = datetime.datetime.now().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M")
sensor = "test"
c.execute("insert into temp values(?, ?, ?, ?)",[date, time, temp, sensor])
conn.commit();
c.close()
