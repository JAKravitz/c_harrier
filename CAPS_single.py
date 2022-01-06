#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:18:09 2022

@author: jakravit
"""
#%%
## IMPORT NECESSARY LIBRARIES 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates

sensor = 'es'
path = '/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR_CAPS/today20211019ground/'
fname = 'CAP_L_211019_173152_URC.csv'

## Read in file and separate data into sensors
file = path+fname
data = pd.read_csv(file, sep=',', encoding='ISO-8859-1', index_col='DateTimeUTC')
sensors = {'es': data.iloc[:,5:24],
           'li': data.iloc[:,24:43],
           'lt': data.iloc[:,43:]}
name = fname[:-4]

## plot
fig, ax = plt.subplots(figsize=(8,5))
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
means = []
stds = []
labels = []
for i,b in enumerate(sensors[sensor].columns):
    #print (i,b)
    data.index = pd.to_datetime(data.index)
    ax.scatter(data.index,data[b], marker='o',s=3)
    mean = data[b].mean()
    std = data[b].std()
    means.append(mean)
    stds.append(std)
    labels.append('{}, \u03BC={:.1e}, \u03C3={:.1e}'.format(b.split(' ')[0], mean, std))
ax.legend(labels,bbox_to_anchor=(1.09, 1.05),fontsize='medium')
ax.set_title('{} -- {}'.format(sensor,name))
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
ax.set_ylabel('W/cm2/nm')
plt.xticks(rotation=45)

ax2 = ax.twinx()
ax2.plot(data.iloc[:,3], label='Roll (deg)') # roll
ax2.plot(data.iloc[:,4], label='Pitch (deg)') # pitch
ax2.set_ylabel('Degrees')
ax2.legend(loc='upper left')
