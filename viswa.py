
#Autohor: Viswa

import os
# os.system('cls')
# Importing important libraries
import pandas as pd
from scipy.signal import find_peaks
import numpy as np
import configparser
import math


df=pd.read_csv('trial.csv')

#FINDING MAX AND MIN
#p=df['Level'].max()
#q=df['Level'].min()
#print(p)


# Get row number of observations that are peaks
x=df['Level']
time_stamps=df['Time(us)']
#Filtering the Ascan file to get area of interest
x=x[43111:91051]
time_stamps=time_stamps[43111:91051].values
idx = find_peaks(x, height=36)
print(idx)
print('order\n')
print(idx[0])
order=idx[0]
print("Values\n")
print(idx[1]['peak_heights'])
unfiltered_peaks=idx[1]['peak_heights']
filtered_peaks=unfiltered_peaks[unfiltered_peaks>41]
order_index=[]
filtered_peaks2=[]
for i,x in enumerate(unfiltered_peaks):
    if x > 41:
       order_index.append(i)
       filtered_peaks2.append(x)
print('filtered_peaks\n')
print(filtered_peaks)
print("done by for loop")
print(filtered_peaks2)
print('Order Index')
print(order_index)
print('\nFirst peak time stamp\n')
#print(order[order_index[0]])
#print(time_stamps[order[order_index[0]]])
peak_times_index=[]
peak_time_stamps=[]
for i,x in enumerate(order_index):
    #peak_time_stamps.apend(time_stamps[order[order_index[i]]])
    #print(order[order_index[i]])
    peak_times_index.append(order[order_index[i]])
print(peak_times_index)
[peak_time_stamps.append(time_stamps[i]) for i in peak_times_index]
print(peak_time_stamps)


filteres_peak_times=np.diff(peak_time_stamps)
print('peak times')
print(filteres_peak_times)
print('\nTof\t')
tof=[]
[tof.append(x) for x in filteres_peak_times if x > 10]
print(tof)

