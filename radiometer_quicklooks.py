# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates

## CAPS SINGLE
path = '/Volumes/Untitled/today20211027_caps1/'
fname = 'CAP_L_211027_163507_URC.csv'
file = path+fname
sensor = 'es'

data = pd.read_csv(file, sep=',', error_bad_lines=False, index_col='DateTimeUTC')
sensors = {'es': data.iloc[:,5:24],
           'li': data.iloc[:,24:43],
           'lt': data.iloc[:,43:]}

fig, ax = plt.subplots(figsize=(8,5))
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
means = []
stds = []
labels = []
for i,b in enumerate(sensors[sensor].columns):
    data.index = pd.to_datetime(data.index)
    ax.scatter(data.index,data[b], marker='o',s=3)
    mean = data[b].mean()
    std = data[b].std()
    means.append(mean)
    stds.append(std)
    labels.append('{}, \u03BC={:.1e}, \u03C3={:.1e}'.format(b.split(' ')[0], mean, std))
#ax.axhline(statistics.mean(means),c='k')
#labels.append('overall mean')
ax.legend(labels,bbox_to_anchor=(1.02, 1.05),fontsize='medium')
ax.set_title('{} -- {}'.format(sensor,fname))
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
plt.xticks(rotation=45)
ax.set_ylabel('W/cm2/nm')


#%% 

## NO CAPS

path = '/Volumes/Untitled/today20211028/'
sensor = 'lt'
flist = os.listdir(path)

fig, ax = plt.subplots(figsize=(10,5))
suffixes = ('Aux.csv','Log.csv','bunk')
for f in flist:
    if not f.endswith(suffixes):
        if not f.startswith('.'):
            print(f)
            file = path+f
            try:
                data = pd.read_csv(file, sep=',', index_col='DateTimeUTC')
                data.index = pd.to_datetime(data.index)
            except:
                continue
            # data = pd.read_csv(file, sep=',', index_col='DateTimeUTC')
            # data.index = pd.to_datetime(data.index)  
            
            sensors = {'es': data.iloc[:,5:24],
                        'li': data.iloc[:,24:43],
                        'lt': data.iloc[:,43:]}
            
           
            colormap = plt.cm.gist_ncar
            plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))
            labels = []
            for i,b in enumerate(sensors[sensor].columns):
                ax.plot(data.index,data[b],)# marker='o',s=2)
                labels.append('{}'.format(b.split(' ')[0]))
    
ax.legend(labels,loc='right',bbox_to_anchor=(1.15, .5),fontsize='medium')
#ax.legend(labels,loc='upper right')
plt.xticks(rotation=45)
ax.set_ylabel('uW/cm2/nm')
ax.set_title(sensor)
ax.set_xlim(pd.Timestamp('2021-10-27 19:29:17.340000'), pd.Timestamp('2021-10-27 21:05:17.239000'))
#ax.set_ylim(0,5)
#ax.set_yscale('log')
fig.savefig('/Users/jakravit/Desktop/quicklook.png',dpi=300,
            bbox_inches='tight')


#%% 

## NO CAPS SINGLE

sensor = 'lt'
file = '/Volumes/Untitled/today20211027/300210417.csv'
data = pd.read_csv(file, sep=',', index_col='DateTimeUTC')
data.index = pd.to_datetime(data.index)
sensors = {'es': data.iloc[:,5:24],#.astype(float),
            'li': data.iloc[:,24:43],#.astype(float),
            'lt': data.iloc[:,43:]}#.astype(float)}

fig, ax = plt.subplots()
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, sensors[sensor].shape[1]))))

for i,b in enumerate(sensors[sensor].columns):
    ax.scatter(data.index,data[b], marker='o',s=5)
