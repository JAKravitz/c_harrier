#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:53:19 2022

@author: jakravit
"""
## IMPORT NECESSARY LIBRARIES 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates

sensor = 'es'
path = '/Users/jakravit/OneDrive - NASA/C-HARRIER_2021_C-AIR/C-AIR/today20211027/'
fname = '300205917.csv'
outpath = '/Users/jakravit/Desktop/Cair_figs/'

file = path+fname
data = pd.read_csv(file, sep=',', encoding='ISO-8859-1', index_col='DateTimeUTC')
data.index = pd.to_datetime(data.index)  
sensors = {'es': data.iloc[:,5:24],
            'li': data.iloc[:,24:43],
            'lt': data.iloc[:,43:]}

fig, ax = plt.subplots(figsize=(8,5))
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
labels = []

for i,b in enumerate(sensors[sensor].columns):
    ax.plot(data.index,data[b])
    labels.append('{}'.format(b.split(' ')[0]))

ax.legend(labels,loc='right',bbox_to_anchor=(1.2, .5),fontsize='medium')
plt.xticks(rotation=45)
ax.set_ylabel('uW/cm2/nm')
ax.set_title(sensor)
#ax.set_xlim(pd.Timestamp('2021-10-27 19:29:17.340000'), pd.Timestamp('2021-10-27 21:05:17.239000'))
# fig.savefig('/Users/jakravit/Desktop/quicklook.png',dpi=300,bbox_inches='tight')
