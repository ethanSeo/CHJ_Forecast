
# coding: utf-8

# In[24]:

import requests
import re
from collections import OrderedDict
import json
import matplotlib.pyplot as plt
import numpy as np


w="https://api2.sktelecom.com/weather/yesterday?version=1&lat=36.5038&lon=127.4166&isTimeRange=Y&appKey=84ccae67-8c6b-4269-8b4d-9131c5eae607"
rp = requests.get(w).json()
Date=rp["weather"]["yesterday"][0]["day"]["timeRelease"]
temp=[]
time=[]
hum=[]

for i in range(24):
    NOW_Temp = float(rp["weather"]["yesterday"][0]["day"]["hourly"][i]["temperature"])
    NOW_Hum = float(rp["weather"]["yesterday"][0]["day"]["hourly"][i]["humidity"])
    NOW_Time = rp["weather"]["yesterday"][0]["day"]["hourly"][i]["timeRelease"]
    
    temp.append(NOW_Temp)
    hum.append(NOW_Hum)
    time.append(int(NOW_Time[11:13]))

time[23]= 24


# In[25]:

print(Date)


# In[26]:

plt.figure(figsize=(8,4))
plt.plot(time, temp, color='#617bfb')
plt.suptitle("Past Weather - "+Date, fontweight='bold')
plt.xlabel("Time(Hr)", fontsize='large', fontweight='bold')
plt.ylabel("Temperature(\u2103)", fontsize='large', fontweight='bold', color='#617bfb')
plt.xticks(np.arange(0, 25, 3), fontsize='large')
plt.yticks(color='#617bfb')
plt.xlim(-2, 26)
plt.grid(True, linestyle='--')

humX = plt.twinx()
humX.plot(time, hum, 'o', label='Humidity', color='teal')
humX.set_ylabel("Humidity(%)", fontsize='large', fontweight='bold', color='teal')
humX.tick_params(axis='y', colors='teal', direction='out', length=13, width=3)
humX.set_ylim(0, 100)


plt.savefig(Date+'.png', dpi=100)
plt.show()


# In[27]:

'''The most recent date gets written at the very end. 
Read the date, and see if the file is not up-to-date, 
append the data in the correct format.'''

from datetime import datetime as dt # "datetime.datetime" MUST have a different name, as "datetime" gets imported as well.
import datetime # interpreter can't differentiate "datetime.datetime" and "datetime"

today = dt.today()
oneDay = datetime.timedelta(days=1)
yesterday = today-oneDay

f = open('pastWeather.txt', 'ab+') # Open file as "append mode" in "byte form". Plus sign(+) creates the file if not found in the directory. 
# Seek -10th character, probing from the end
f.seek(-10,2)
readDate = f.read(10).decode('utf-8')
recentDate = dt.strptime(readDate, '%Y-%m-%d') # Convert String to datetime.datetime object

output = '\nT:'+str(temp)+'\nH:'+str(hum)+'\n'+Date

if (yesterday - recentDate) > oneDay:
    f.write(output.encode()) # Encode the output into "byte form" because the file was opened in the "append - byte form" (ab+)
    f.close()
    print("File Updated!")
else:
    print("File is Up-To-Date :)")


# In[ ]:



