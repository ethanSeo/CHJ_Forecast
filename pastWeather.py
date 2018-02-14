
# coding: utf-8

# In[68]:

import requests
import re
from collections import OrderedDict
import json
import matplotlib.pyplot as plt
import numpy as np
w="https://api2.sktelecom.com/weather/yesterday?version=1&lat=36.5038&lon=127.4166&isTimeRange=Y&appKey=84ccae67-8c6b-4269-8b4d-9131c5eae607"
rp = requests.get(w).json()
date=rp["weather"]["yesterday"][0]["day"]["timeRelease"]
temp=[]
time=[]

for i in range(24):
    NOW_Temp = float(rp["weather"]["yesterday"][0]["day"]["hourly"][i]["temperature"])
    NOW_Time = rp["weather"]["yesterday"][0]["day"]["hourly"][i]["timeRelease"]
    temp.append(NOW_Temp)
    time.append(int(NOW_Time[11:13]))

time[23]= 24


# In[69]:

print(temp)
print(time)


# In[81]:

plt.plot(time, temp)
plt.suptitle("Past Weather - "+date, fontweight='bold')
plt.xlabel("Time(Hr)", fontsize='large', fontweight='bold')
plt.ylabel("Temperature(\u2103)", fontsize='large', fontweight='bold')
plt.xticks(np.arange(0, 25, 3), fontsize='large')
plt.xlim(-2, 26)
plt.grid(True, linestyle='--')
plt.savefig(date+'.png')
plt.show()


# In[ ]:



